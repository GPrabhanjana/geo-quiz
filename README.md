# GeoQuiz

A geography quiz on an interactive 3D globe. Name all 197 countries, their
capitals, or both.

Built by [Prabhanjana](https://gprabhanjana.netlify.app/).

## Play

The page fetches its data over HTTP, so opening `index.htm` straight from disk
will not work. Serve the folder instead:

```sh
python -m http.server 8777
```

Then open <http://localhost:8777/index.htm>.

## Modes

| Mode | You see | You type |
|---|---|---|
| Countries | the outline on the globe | the country |
| Capitals | the country name | the capital |
| Countries & Capitals | the outline | both |

Any mode can be limited to a single continent from the dropdown.

## Controls

| | |
|---|---|
| drag / scroll | rotate and zoom the globe |
| click a country | jump to it |
| `←` `→` | previous / next country |
| `Ctrl` + `←` `→` | previous / next, even while typing |
| `Ctrl` + `↑` `↓` | switch between the country and capital boxes |
| `Enter` | on a solved country, move to the next |

Answers are forgiving. Case, accents, punctuation and spacing are ignored, and
common alternatives are accepted — `uk`, `usa`, `drc`, `cote d'ivoire`, `burma`,
`holland` and `swaziland` all work, as do `kiev` for Kyiv and `washington` for
Washington, D.C. Two-letter country codes are deliberately *not* accepted. Once
an answer is right the box rewrites itself to the country's primary name.

Countries too small to see — Vatican City, Monaco, Nauru, the Maldives and 37
others — get a locator ring that tightens onto the country as you zoom in. The
ring is clickable, which is the only practical way to select them.

## Files

| | |
|---|---|
| `index.htm` | the whole game — no build step, nothing to install |
| `countries.geojson` | 197 countries: shape, name, capital, aliases |
| `blocked_slim.geojson` | disputed areas and Antarctica, drawn but not playable |
| `build_data.py` | regenerates both files from the raw source |
| `country_table.py` | the hand-maintained name / capital / alias table |

## Rebuilding the data

Only needed if you edit `country_table.py` or the simplification settings.
Requires Python 3 and [mapshaper](https://github.com/mbloch/mapshaper):

```sh
npm install
python build_data.py
```

This reads `countries_197_with_capitals.geojson` (a Natural Earth export) and
writes the two slim files above, cutting 171 properties per country down to 6,
and 22.8 MB down to 4.4 MB.

Two things the build does that are worth knowing about:

- **It verifies every capital.** The source stored capitals in degrees-minutes
  but read them as decimal degrees, so all 197 were wrong and 64 landed outside
  their own country. Coordinates now come from `country_table.py`, and the build
  fails if any capital does not fall inside its country's borders.
- **It simplifies in two passes.** Neighbouring countries share their border
  vertices exactly, so simplifying each country on its own would tear visible
  gaps along every border. Countries that touch another country are simplified
  together in one pass; island nations, which cannot tear anything, get a much
  finer tolerance so archipelagos like Tuvalu and the Maldives keep their shape.

## Credits

Country shapes from [Natural Earth](https://www.naturalearthdata.com/).
Rendered with [three.js](https://threejs.org/),
[d3-geo](https://github.com/d3/d3-geo) and
[earcut](https://github.com/mapbox/earcut), all loaded from a CDN.
