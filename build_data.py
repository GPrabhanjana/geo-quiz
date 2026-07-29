"""Build the slim GeoQuiz data files from the raw Natural Earth source.

    python build_data.py

Reads  countries_197_with_capitals.geojson  and  blocked.geojson
Writes countries.geojson  and  blocked_slim.geojson

Three things happen here:

1. Properties are cut from 171 per feature down to 6 (name, name_alt, capital,
   capital_alt, capital_lonlat, continent). Country identity is by array index
   in index.htm, so no ISO code is carried.

2. Capital coordinates are replaced wholesale from country_table.py. The source
   file stored them in CIA-Factbook degrees-minutes read as decimal degrees, so
   all 197 were wrong (64 of them landed outside their own country). Every
   replacement is checked with point-in-polygon against the full-resolution
   geometry, and the build FAILS if any capital is not inside its country.

3. Geometry is shrunk for render performance: tiny islets are dropped, rings are
   simplified by mapshaper, and coordinates are rounded. Simplification goes
   through mapshaper specifically because 68k vertices are shared exactly
   between neighbouring countries -- simplifying each ring independently would
   tear visible gaps along shared borders, whereas mapshaper simplifies each
   shared arc once and rebuilds both sides from it.
"""

import json
import math
import os
import subprocess
import sys
import tempfile

from country_table import COUNTRIES

SRC_COUNTRIES = "countries_197_with_capitals.geojson"
SRC_BLOCKED = "blocked.geojson"
OUT_COUNTRIES = "countries.geojson"
OUT_BLOCKED = "blocked_slim.geojson"

# Coordinate decimals. 4dp is ~11m, far below one screen pixel at max zoom.
PRECISION = 4

# Drop polygons smaller than this (square degrees) ...
MIN_POLY_AREA = 0.001
# ... but never drop a country's largest polygon, and never leave it with fewer
# than this many, so archipelagos (Maldives, Marshall Islands) keep their shape.
MIN_POLYS_KEPT = 12

# Simplification tolerance in metres, applied in two passes (see simplify()).
# A single global pass is not usable here: any tolerance coarse enough to help
# Canada erases Tuvalu and the Maldives, whose islands are a few hundred metres
# across. Splitting by whether a country touches another lets island nations
# keep their shape without any risk to shared borders.
SIMPLIFY_INTERVAL_BORDER = 3000
SIMPLIFY_INTERVAL_ISLAND = 300

# How far outside its country a capital may sit before the build fails. Coastal
# and island capitals (Banjul, Malabo, Conakry, Funafuti) legitimately fall just
# offshore of the Natural Earth coastline, and Nicosia lands in the Northern
# Cyprus polygon that this dataset routes to blocked.geojson. Every one of those
# is under 10km, while the errors this check exists to catch ran from 45km to
# 1100km, so the gap is wide. Tolerated capitals are always listed, never silent.
CAPITAL_TOLERANCE_KM = 10


def ring_area(ring):
    """Unsigned shoelace area in square degrees."""
    a = 0.0
    for i in range(len(ring) - 1):
        a += ring[i][0] * ring[i + 1][1] - ring[i + 1][0] * ring[i][1]
    return abs(a) / 2.0


def polygons_of(geometry):
    if geometry["type"] == "Polygon":
        return [geometry["coordinates"]]
    return geometry["coordinates"]


def point_in_ring(x, y, ring):
    inside = False
    for i in range(len(ring) - 1):
        x1, y1 = ring[i][0], ring[i][1]
        x2, y2 = ring[i + 1][0], ring[i + 1][1]
        if (y1 > y) != (y2 > y):
            if x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
                inside = not inside
    return inside


def point_in_geometry(x, y, geometry):
    """True if (x, y) is inside the outer ring of some polygon and in no hole."""
    for poly in polygons_of(geometry):
        if point_in_ring(x, y, poly[0]):
            if not any(point_in_ring(x, y, hole) for hole in poly[1:]):
                return True
    return False


def km_to_geometry(x, y, geometry):
    """Rough great-circle distance in km from a point to the nearest vertex."""
    best = float("inf")
    coslat = math.cos(math.radians(y))
    for poly in polygons_of(geometry):
        for ring in poly:
            for px, py in ((p[0], p[1]) for p in ring):
                d = math.hypot((px - x) * coslat, py - y)
                if d < best:
                    best = d
    return best * 111.0


def drop_islets(geometry):
    """Remove polygons too small to see, protecting small island nations."""
    polys = polygons_of(geometry)
    if len(polys) == 1:
        return geometry, 0
    scored = sorted(((ring_area(p[0]), i) for i, p in enumerate(polys)), reverse=True)
    keep = {i for rank, (area, i) in enumerate(scored)
            if area >= MIN_POLY_AREA or rank < MIN_POLYS_KEPT}
    kept = [p for i, p in enumerate(polys) if i in keep]
    return {"type": "MultiPolygon", "coordinates": kept}, len(polys) - len(kept)


def rewind(geometry):
    """Force exterior rings clockwise and holes counter-clockwise.

    This is the opposite of what RFC 7946 specifies, and it is deliberate:
    d3-geo treats polygons as spherical and requires the reversed winding, which
    is the convention the source Natural Earth file already used. mapshaper
    emits spec-compliant counter-clockwise rings, and with those d3.geoCentroid
    and d3.geoBounds return the ANTIPODE of every country -- which silently
    sends rotateTo() in index.htm to the wrong side of the planet. The renderer
    normalises winding itself, so only the d3 calls care.
    """
    out = []
    for poly in polygons_of(geometry):
        rings = []
        for i, ring in enumerate(poly):
            a = 0.0
            for j in range(len(ring) - 1):
                a += ring[j][0] * ring[j + 1][1] - ring[j + 1][0] * ring[j][1]
            clockwise = a < 0
            want_clockwise = (i == 0)
            rings.append(ring if clockwise == want_clockwise else ring[::-1])
        out.append(rings)
    return {"type": "MultiPolygon", "coordinates": out}


def round_coords(node):
    if isinstance(node, list):
        if node and isinstance(node[0], (int, float)):
            return [round(v, PRECISION) for v in node]
        return [round_coords(c) for c in node]
    return node


def run_mapshaper(features, interval, label):
    """Simplify one batch. Everything passed in is simplified together, so any
    border shared inside the batch is simplified once and stays welded."""
    if not features:
        return []
    tmpdir = tempfile.mkdtemp(prefix="geoquiz_")
    src = os.path.join(tmpdir, "in.json")
    dst = os.path.join(tmpdir, "out.json")
    with open(src, "w", encoding="utf-8") as fh:
        json.dump({"type": "FeatureCollection", "features": features}, fh)

    cmd = ["npx", "--no-install", "mapshaper", src,
           "-simplify", "visvalingam", "weighted",
           "interval=%d" % interval, "keep-shapes",
           "-o", dst, "format=geojson"]
    proc = subprocess.run(cmd, capture_output=True, text=True, shell=(os.name == "nt"))
    if proc.returncode != 0 or not os.path.exists(dst):
        sys.exit("mapshaper failed on %s:\n%s\n%s" % (label, proc.stdout, proc.stderr))

    with open(dst, encoding="utf-8") as fh:
        out = json.load(fh)
    return out["features"]


def touching_countries(features):
    """Names of countries sharing at least one exact vertex with another country.

    Natural Earth stores borders as identical coordinate pairs on both sides, so
    an exact-match index is enough to tell a bordering country from an island.
    """
    owners = {}
    shared = set()
    for f in features:
        name = f["properties"]["name"]
        for poly in polygons_of(f["geometry"]):
            for ring in poly:
                for pt in ring:
                    key = (pt[0], pt[1])
                    prev = owners.setdefault(key, name)
                    if prev != name:
                        shared.add(name)
                        shared.add(prev)
    return shared


def simplify(features, label):
    """Simplify in two passes, split by whether a country touches another.

    Bordering countries all go through one pass together so shared arcs are
    simplified once. Island nations share no vertex with anything, so they can
    take a much finer tolerance without any risk of tearing a border.
    """
    touching = touching_countries(features)
    bordering = [f for f in features if f["properties"]["name"] in touching]
    islands = [f for f in features if f["properties"]["name"] not in touching]
    print("  %s: %d bordering, %d island" % (label, len(bordering), len(islands)))
    return (run_mapshaper(bordering, SIMPLIFY_INTERVAL_BORDER, label + "/bordering")
            + run_mapshaper(islands, SIMPLIFY_INTERVAL_ISLAND, label + "/islands"))


def count_vertices(features):
    return sum(len(ring)
               for f in features if f.get("geometry")
               for poly in polygons_of(f["geometry"])
               for ring in poly)


def count_polygons(features):
    return sum(len(polygons_of(f["geometry"]))
               for f in features if f.get("geometry"))


def build_countries():
    with open(SRC_COUNTRIES, encoding="utf-8") as fh:
        src = json.load(fh)
    features = src["features"]

    src_names = {f["properties"]["ADMIN"] for f in features}
    missing = src_names - set(COUNTRIES)
    extra = set(COUNTRIES) - src_names
    if missing or extra:
        sys.exit("country_table.py out of sync with source.\n"
                 "  in source but not table: %s\n"
                 "  in table but not source: %s" % (sorted(missing), sorted(extra)))

    print("source: %d features, %d polygons, %d vertices"
          % (len(features), count_polygons(features), count_vertices(features)))

    # Verify capitals against FULL-RESOLUTION geometry, before any simplification,
    # so this tests the coordinate data rather than the simplification tolerance.
    failures, tolerated = [], []
    for f in features:
        entry = COUNTRIES[f["properties"]["ADMIN"]]
        if point_in_geometry(entry["lon"], entry["lat"], f["geometry"]):
            continue
        dist = km_to_geometry(entry["lon"], entry["lat"], f["geometry"])
        row = (entry["name"], entry["capital"], entry["lon"], entry["lat"], dist)
        (tolerated if dist <= CAPITAL_TOLERANCE_KM else failures).append(row)

    if failures:
        print("\nCAPITALS OUTSIDE THEIR COUNTRY (%d):" % len(failures), file=sys.stderr)
        for name, cap, lon, lat, dist in sorted(failures, key=lambda r: -r[4]):
            print("  %-30s %-22s lon=%9.4f lat=%9.4f  %.1f km out"
                  % (name, cap, lon, lat, dist), file=sys.stderr)
        sys.exit("\nFix these in country_table.py.")

    print("capitals: %d verified inside their country, %d just offshore"
          % (len(features) - len(tolerated), len(tolerated)))
    for name, cap, _, _, dist in sorted(tolerated, key=lambda r: -r[4]):
        print("    %-24s %-20s %.1f km" % (name, cap, dist))

    slim = []
    dropped = 0
    for f in features:
        entry = COUNTRIES[f["properties"]["ADMIN"]]
        geometry, n = drop_islets(f["geometry"])
        dropped += n
        slim.append({
            "type": "Feature",
            "properties": {
                "name": entry["name"],
                "name_alt": entry["alt"],
                "capital": entry["capital"],
                "capital_alt": entry["cap_alt"],
                "capital_lonlat": [round(entry["lon"], PRECISION),
                                   round(entry["lat"], PRECISION)],
                "continent": f["properties"]["CONTINENT"],
            },
            "geometry": geometry,
        })
    print("islets: dropped %d polygons, %d remain" % (dropped, count_polygons(slim)))

    simplified = simplify(slim, "countries")
    print("simplify: %d -> %d vertices"
          % (count_vertices(slim), count_vertices(simplified)))

    # simplify() returns the two passes concatenated, so the order differs from
    # the input. index.htm keys countries by array index, so restoring the
    # original order here is load-bearing, not cosmetic.
    by_name = {f["properties"]["name"]: f for f in simplified}
    ordered = []
    for f in slim:
        out = by_name[f["properties"]["name"]]
        out["properties"] = f["properties"]
        out["geometry"] = round_coords(rewind(out["geometry"]))
        ordered.append(out)

    # Report the countries that lost the most shape. In "countries" mode the
    # outline IS the question, so silent shape loss would make the quiz wrong.
    retained = []
    for before, after in zip(slim, ordered):
        was = sum(ring_area(p[0]) for p in polygons_of(before["geometry"]))
        now = sum(ring_area(p[0]) for p in polygons_of(after["geometry"]))
        retained.append((now / was * 100 if was else 100.0, after["properties"]["name"]))
    retained.sort()
    print("area retained: %.1f%% mean, lowest:" % (sum(r[0] for r in retained) / len(retained)))
    for pct, name in retained[:6]:
        print("    %-24s %5.1f%%" % (name, pct))

    write(OUT_COUNTRIES, ordered)


def build_blocked():
    with open(SRC_BLOCKED, encoding="utf-8") as fh:
        src = json.load(fh)

    slim = []
    for f in src["features"]:
        if not f.get("geometry"):
            continue
        geometry, _ = drop_islets(f["geometry"])
        slim.append({
            "type": "Feature",
            "properties": {"name": f["properties"].get("ADMIN")
                           or f["properties"].get("NAME")},
            "geometry": geometry,
        })

    # One pass is fine here: the blocked layer renders below the country layer,
    # which covers any small mismatch along the borders they share.
    simplified = run_mapshaper(slim, SIMPLIFY_INTERVAL_BORDER, "blocked")
    for f in simplified:
        f["geometry"] = round_coords(rewind(f["geometry"]))
    write(OUT_BLOCKED, simplified)


def write(path, features):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"type": "FeatureCollection", "features": features},
                  fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote %s: %.1f MB, %d features, %d polygons, %d vertices\n"
          % (path, os.path.getsize(path) / 1e6, len(features),
             count_polygons(features), count_vertices(features)))


if __name__ == "__main__":
    build_countries()
    build_blocked()
