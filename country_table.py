# Curated country/capital table for GeoQuiz.
#
# Keyed by the ADMIN property of the source Natural Earth file. Each entry is:
#   name      primary country name shown and expected in the quiz
#   alt       accepted alternative country names (see conventions below)
#   capital   primary capital name
#   cap_alt   accepted alternative capital names
#   lon, lat  capital location in TRUE decimal degrees
#
# The source file stored capitals in CIA-Factbook degrees-minutes (12.29 meaning
# 12 deg 29 min) misread as decimal degrees, so every coordinate here was
# re-entered by hand. build_data.py asserts each one falls inside its own
# country polygon, so mistakes fail the build rather than ship.
#
# Alias conventions follow the Sporcle "Countries of the World" quiz:
#   - genuine alternative names (Ivory Coast / Cote d'Ivoire, Myanmar / Burma)
#   - formal long names (Kingdom of Bhutan)
#   - only widely-known abbreviations: UK, USA, UAE, DRC, CAR, PNG, NZ
#   - never 2-letter ISO codes (no "IN" for India, no "DE" for Germany)
#   - capitals: simplifications (Washington for Washington, D.C.),
#     alternative transliterations (Kiev for Kyiv), and second or former
#     seats of government (Cape Town for Pretoria)
#
# norm() in index.htm already folds case, diacritics, punctuation, spacing,
# "&"/"and", "st"/"saint" and a leading "the", so those variants are NOT
# listed here.

COUNTRIES = {
    "Egypt": dict(
        name="Egypt", alt=["Arab Republic of Egypt"],
        capital="Cairo", cap_alt=[], lon=31.2357, lat=30.0444),
    "Indonesia": dict(
        name="Indonesia", alt=["Republic of Indonesia"],
        capital="Jakarta", cap_alt=["Nusantara"], lon=106.8456, lat=-6.2088),
    "Malaysia": dict(
        name="Malaysia", alt=[],
        capital="Kuala Lumpur", cap_alt=["Putrajaya"], lon=101.6869, lat=3.1390),
    "Chile": dict(
        name="Chile", alt=["Republic of Chile"],
        capital="Santiago", cap_alt=["Santiago de Chile"], lon=-70.6693, lat=-33.4489),
    "Bolivia": dict(
        name="Bolivia", alt=["Plurinational State of Bolivia"],
        capital="La Paz", cap_alt=["Sucre"], lon=-68.1193, lat=-16.4897),
    "Peru": dict(
        name="Peru", alt=["Republic of Peru"],
        capital="Lima", cap_alt=[], lon=-77.0428, lat=-12.0464),
    "Argentina": dict(
        name="Argentina", alt=["Argentine Republic"],
        capital="Buenos Aires", cap_alt=[], lon=-58.3816, lat=-34.6037),
    "Cyprus": dict(
        name="Cyprus", alt=["Republic of Cyprus"],
        capital="Nicosia", cap_alt=["Lefkosia"], lon=33.3823, lat=35.1856),
    "India": dict(
        name="India", alt=["Republic of India", "Bharat"],
        capital="New Delhi", cap_alt=["Delhi"], lon=77.2090, lat=28.6139),
    "China": dict(
        name="China", alt=["Peoples Republic of China", "PRC"],
        capital="Beijing", cap_alt=["Peking"], lon=116.4074, lat=39.9042),
    "Israel": dict(
        name="Israel", alt=["State of Israel"],
        capital="Jerusalem", cap_alt=["Tel Aviv"], lon=35.2137, lat=31.7683),
    "Lebanon": dict(
        name="Lebanon", alt=["Lebanese Republic"],
        capital="Beirut", cap_alt=["Beyrouth"], lon=35.5018, lat=33.8938),
    "Ethiopia": dict(
        name="Ethiopia", alt=["Federal Democratic Republic of Ethiopia", "Abyssinia"],
        capital="Addis Ababa", cap_alt=[], lon=38.7578, lat=9.0192),
    "South Sudan": dict(
        name="South Sudan", alt=["Republic of South Sudan"],
        capital="Juba", cap_alt=[], lon=31.5713, lat=4.8594),
    "Somalia": dict(
        name="Somalia", alt=["Federal Republic of Somalia"],
        capital="Mogadishu", cap_alt=["Muqdisho"], lon=45.3182, lat=2.0469),
    "Kenya": dict(
        name="Kenya", alt=["Republic of Kenya"],
        capital="Nairobi", cap_alt=[], lon=36.8219, lat=-1.2921),
    "Malawi": dict(
        name="Malawi", alt=["Republic of Malawi"],
        capital="Lilongwe", cap_alt=[], lon=33.7741, lat=-13.9626),
    "United Republic of Tanzania": dict(
        name="Tanzania", alt=["United Republic of Tanzania"],
        capital="Dodoma", cap_alt=["Dar es Salaam"], lon=35.7516, lat=-6.1630),
    "Syria": dict(
        name="Syria", alt=["Syrian Arab Republic"],
        capital="Damascus", cap_alt=["Dimashq"], lon=36.2765, lat=33.5138),
    "France": dict(
        name="France", alt=["French Republic"],
        capital="Paris", cap_alt=[], lon=2.3522, lat=48.8566),
    "Suriname": dict(
        name="Suriname", alt=["Republic of Suriname", "Surinam"],
        capital="Paramaribo", cap_alt=[], lon=-55.2038, lat=5.8520),
    "Guyana": dict(
        name="Guyana", alt=["Co-operative Republic of Guyana"],
        capital="Georgetown", cap_alt=[], lon=-58.1553, lat=6.8013),
    "South Korea": dict(
        name="South Korea", alt=["Republic of Korea", "ROK"],
        capital="Seoul", cap_alt=[], lon=126.9780, lat=37.5665),
    "North Korea": dict(
        name="North Korea", alt=["Democratic Peoples Republic of Korea", "DPRK"],
        capital="Pyongyang", cap_alt=[], lon=125.7625, lat=39.0392),
    "Morocco": dict(
        name="Morocco", alt=["Kingdom of Morocco"],
        capital="Rabat", cap_alt=[], lon=-6.8498, lat=34.0209),
    "Costa Rica": dict(
        name="Costa Rica", alt=["Republic of Costa Rica"],
        capital="San Jose", cap_alt=[], lon=-84.0907, lat=9.9281),
    "Nicaragua": dict(
        name="Nicaragua", alt=["Republic of Nicaragua"],
        capital="Managua", cap_alt=[], lon=-86.2514, lat=12.1150),
    "Republic of the Congo": dict(
        name="Republic of the Congo", alt=["Congo", "Congo-Brazzaville"],
        capital="Brazzaville", cap_alt=[], lon=15.2429, lat=-4.2634),
    "Democratic Republic of the Congo": dict(
        name="Democratic Republic of the Congo",
        alt=["DRC", "DR Congo", "Congo-Kinshasa", "Zaire"],
        capital="Kinshasa", cap_alt=[], lon=15.2663, lat=-4.4419),
    "Bhutan": dict(
        name="Bhutan", alt=["Kingdom of Bhutan"],
        capital="Thimphu", cap_alt=[], lon=89.6390, lat=27.4728),
    "Ukraine": dict(
        name="Ukraine", alt=[],
        capital="Kyiv", cap_alt=["Kiev"], lon=30.5234, lat=50.4501),
    "Belarus": dict(
        name="Belarus", alt=["Republic of Belarus", "Byelorussia"],
        capital="Minsk", cap_alt=[], lon=27.5615, lat=53.9006),
    "Namibia": dict(
        name="Namibia", alt=["Republic of Namibia"],
        capital="Windhoek", cap_alt=[], lon=17.0832, lat=-22.5609),
    "South Africa": dict(
        name="South Africa", alt=["Republic of South Africa", "RSA"],
        capital="Pretoria", cap_alt=["Cape Town", "Bloemfontein"], lon=28.1881, lat=-25.7479),
    "Oman": dict(
        name="Oman", alt=["Sultanate of Oman"],
        capital="Muscat", cap_alt=["Masqat"], lon=58.5453, lat=23.5880),
    "Uzbekistan": dict(
        name="Uzbekistan", alt=["Republic of Uzbekistan"],
        capital="Tashkent", cap_alt=["Toshkent"], lon=69.2401, lat=41.2995),
    "Kazakhstan": dict(
        name="Kazakhstan", alt=["Republic of Kazakhstan"],
        capital="Astana", cap_alt=["Nur-Sultan", "Akmola"], lon=71.4704, lat=51.1605),
    "Tajikistan": dict(
        name="Tajikistan", alt=["Republic of Tajikistan"],
        capital="Dushanbe", cap_alt=[], lon=68.7870, lat=38.5598),
    "Lithuania": dict(
        name="Lithuania", alt=["Republic of Lithuania"],
        capital="Vilnius", cap_alt=[], lon=25.2797, lat=54.6872),
    "Brazil": dict(
        name="Brazil", alt=["Federative Republic of Brazil", "Brasil"],
        capital="Brasilia", cap_alt=[], lon=-47.8825, lat=-15.7942),
    "Uruguay": dict(
        name="Uruguay", alt=["Oriental Republic of Uruguay"],
        capital="Montevideo", cap_alt=[], lon=-56.1645, lat=-34.9011),
    "Mongolia": dict(
        name="Mongolia", alt=[],
        capital="Ulaanbaatar", cap_alt=["Ulan Bator"], lon=106.9057, lat=47.8864),
    "Russia": dict(
        name="Russia", alt=["Russian Federation"],
        capital="Moscow", cap_alt=["Moskva"], lon=37.6173, lat=55.7558),
    "Czechia": dict(
        name="Czechia", alt=["Czech Republic"],
        capital="Prague", cap_alt=["Praha"], lon=14.4378, lat=50.0755),
    "Germany": dict(
        name="Germany", alt=["Federal Republic of Germany", "Deutschland"],
        capital="Berlin", cap_alt=[], lon=13.4050, lat=52.5200),
    "Estonia": dict(
        name="Estonia", alt=["Republic of Estonia"],
        capital="Tallinn", cap_alt=[], lon=24.7536, lat=59.4370),
    "Latvia": dict(
        name="Latvia", alt=["Republic of Latvia"],
        capital="Riga", cap_alt=[], lon=24.1052, lat=56.9496),
    "Norway": dict(
        name="Norway", alt=["Kingdom of Norway"],
        capital="Oslo", cap_alt=[], lon=10.7522, lat=59.9139),
    "Sweden": dict(
        name="Sweden", alt=["Kingdom of Sweden"],
        capital="Stockholm", cap_alt=[], lon=18.0686, lat=59.3293),
    "Finland": dict(
        name="Finland", alt=["Republic of Finland"],
        capital="Helsinki", cap_alt=["Helsingfors"], lon=24.9384, lat=60.1699),
    "Vietnam": dict(
        name="Vietnam", alt=["Socialist Republic of Vietnam", "Viet Nam"],
        capital="Hanoi", cap_alt=[], lon=105.8342, lat=21.0278),
    "Cambodia": dict(
        name="Cambodia", alt=["Kingdom of Cambodia", "Kampuchea"],
        capital="Phnom Penh", cap_alt=[], lon=104.8922, lat=11.5564),
    "Luxembourg": dict(
        name="Luxembourg", alt=["Grand Duchy of Luxembourg"],
        capital="Luxembourg", cap_alt=["Luxembourg City"], lon=6.1296, lat=49.6116),
    "United Arab Emirates": dict(
        name="United Arab Emirates", alt=["UAE"],
        capital="Abu Dhabi", cap_alt=[], lon=54.3773, lat=24.4539),
    "Belgium": dict(
        name="Belgium", alt=["Kingdom of Belgium"],
        capital="Brussels", cap_alt=["Bruxelles", "Brussel"], lon=4.3517, lat=50.8503),
    "Georgia": dict(
        name="Georgia", alt=[],
        capital="Tbilisi", cap_alt=[], lon=44.7830, lat=41.7151),
    "North Macedonia": dict(
        name="North Macedonia", alt=["Macedonia", "Republic of North Macedonia"],
        capital="Skopje", cap_alt=[], lon=21.4254, lat=41.9981),
    "Albania": dict(
        name="Albania", alt=["Republic of Albania"],
        capital="Tirana", cap_alt=["Tirane"], lon=19.8187, lat=41.3275),
    "Azerbaijan": dict(
        name="Azerbaijan", alt=["Republic of Azerbaijan"],
        capital="Baku", cap_alt=["Baki"], lon=49.8671, lat=40.4093),
    "Turkey": dict(
        name="Turkey", alt=["Turkiye", "Republic of Turkiye"],
        capital="Ankara", cap_alt=[], lon=32.8597, lat=39.9334),
    "Spain": dict(
        name="Spain", alt=["Kingdom of Spain", "Espana"],
        capital="Madrid", cap_alt=[], lon=-3.7038, lat=40.4168),
    "Laos": dict(
        name="Laos", alt=["Lao PDR", "Lao Peoples Democratic Republic"],
        capital="Vientiane", cap_alt=[], lon=102.6331, lat=17.9757),
    "Kyrgyzstan": dict(
        name="Kyrgyzstan", alt=["Kyrgyz Republic", "Kirghizia"],
        capital="Bishkek", cap_alt=["Frunze"], lon=74.5698, lat=42.8746),
    "Armenia": dict(
        name="Armenia", alt=["Republic of Armenia"],
        capital="Yerevan", cap_alt=[], lon=44.5152, lat=40.1872),
    "Denmark": dict(
        name="Denmark", alt=["Kingdom of Denmark"],
        capital="Copenhagen", cap_alt=["Kobenhavn"], lon=12.5683, lat=55.6761),
    "Libya": dict(
        name="Libya", alt=["State of Libya"],
        capital="Tripoli", cap_alt=[], lon=13.1913, lat=32.8872),
    "Tunisia": dict(
        name="Tunisia", alt=["Republic of Tunisia"],
        capital="Tunis", cap_alt=[], lon=10.1815, lat=36.8065),
    "Romania": dict(
        name="Romania", alt=["Rumania"],
        capital="Bucharest", cap_alt=["Bucuresti"], lon=26.1025, lat=44.4268),
    "Hungary": dict(
        name="Hungary", alt=[],
        capital="Budapest", cap_alt=[], lon=19.0402, lat=47.4979),
    "Slovakia": dict(
        name="Slovakia", alt=["Slovak Republic"],
        capital="Bratislava", cap_alt=[], lon=17.1077, lat=48.1486),
    "Poland": dict(
        name="Poland", alt=["Republic of Poland", "Polska"],
        capital="Warsaw", cap_alt=["Warszawa"], lon=21.0122, lat=52.2297),
    "Ireland": dict(
        name="Ireland", alt=["Republic of Ireland", "Eire"],
        capital="Dublin", cap_alt=["Baile Atha Cliath"], lon=-6.2603, lat=53.3498),
    "United Kingdom": dict(
        name="United Kingdom", alt=["UK", "Great Britain", "Britain",
                                    "United Kingdom of Great Britain and Northern Ireland"],
        capital="London", cap_alt=[], lon=-0.1276, lat=51.5074),
    "Greece": dict(
        name="Greece", alt=["Hellenic Republic", "Hellas"],
        capital="Athens", cap_alt=["Athina"], lon=23.7275, lat=37.9838),
    "Zambia": dict(
        name="Zambia", alt=["Republic of Zambia", "Northern Rhodesia"],
        capital="Lusaka", cap_alt=[], lon=28.3228, lat=-15.3875),
    "Sierra Leone": dict(
        name="Sierra Leone", alt=["Republic of Sierra Leone"],
        capital="Freetown", cap_alt=[], lon=-13.2317, lat=8.4657),
    "Guinea": dict(
        name="Guinea", alt=["Republic of Guinea", "Guinea-Conakry"],
        capital="Conakry", cap_alt=[], lon=-13.7122, lat=9.6412),
    "Liberia": dict(
        name="Liberia", alt=["Republic of Liberia"],
        capital="Monrovia", cap_alt=[], lon=-10.7969, lat=6.2907),
    "Central African Republic": dict(
        name="Central African Republic", alt=["CAR"],
        capital="Bangui", cap_alt=[], lon=18.5582, lat=4.3947),
    "Sudan": dict(
        name="Sudan", alt=["Republic of the Sudan"],
        capital="Khartoum", cap_alt=["Al Khartum"], lon=32.5599, lat=15.5007),
    "Djibouti": dict(
        name="Djibouti", alt=["Republic of Djibouti"],
        capital="Djibouti", cap_alt=["Djibouti City"], lon=43.1456, lat=11.5721),
    "Eritrea": dict(
        name="Eritrea", alt=["State of Eritrea"],
        capital="Asmara", cap_alt=["Asmera"], lon=38.9251, lat=15.3229),
    "Austria": dict(
        name="Austria", alt=["Republic of Austria", "Osterreich"],
        capital="Vienna", cap_alt=["Wien"], lon=16.3738, lat=48.2082),
    "Iraq": dict(
        name="Iraq", alt=["Republic of Iraq"],
        capital="Baghdad", cap_alt=[], lon=44.3661, lat=33.3152),
    "Italy": dict(
        name="Italy", alt=["Italian Republic", "Italia"],
        capital="Rome", cap_alt=["Roma"], lon=12.4964, lat=41.9028),
    "Switzerland": dict(
        name="Switzerland", alt=["Swiss Confederation", "Helvetia"],
        capital="Bern", cap_alt=["Berne"], lon=7.4474, lat=46.9480),
    "Iran": dict(
        name="Iran", alt=["Islamic Republic of Iran", "Persia"],
        capital="Tehran", cap_alt=["Teheran"], lon=51.3890, lat=35.6892),
    "Netherlands": dict(
        name="Netherlands", alt=["Holland", "Kingdom of the Netherlands"],
        capital="Amsterdam", cap_alt=["The Hague", "Den Haag"], lon=4.9041, lat=52.3676),
    "Liechtenstein": dict(
        name="Liechtenstein", alt=["Principality of Liechtenstein"],
        capital="Vaduz", cap_alt=[], lon=9.5209, lat=47.1410),
    "Ivory Coast": dict(
        name="Ivory Coast", alt=["Cote d'Ivoire"],
        capital="Yamoussoukro", cap_alt=["Abidjan"], lon=-5.2767, lat=6.8276),
    "Republic of Serbia": dict(
        name="Serbia", alt=["Republic of Serbia"],
        capital="Belgrade", cap_alt=["Beograd"], lon=20.4489, lat=44.7866),
    "Mali": dict(
        name="Mali", alt=["Republic of Mali"],
        capital="Bamako", cap_alt=[], lon=-8.0029, lat=12.6392),
    "Senegal": dict(
        name="Senegal", alt=["Republic of Senegal"],
        capital="Dakar", cap_alt=[], lon=-17.4677, lat=14.7167),
    "Nigeria": dict(
        name="Nigeria", alt=["Federal Republic of Nigeria"],
        capital="Abuja", cap_alt=["Lagos"], lon=7.4951, lat=9.0765),
    "Benin": dict(
        name="Benin", alt=["Republic of Benin", "Dahomey"],
        capital="Porto-Novo", cap_alt=["Cotonou"], lon=2.6289, lat=6.4969),
    "Angola": dict(
        name="Angola", alt=["Republic of Angola"],
        capital="Luanda", cap_alt=[], lon=13.2343, lat=-8.8390),
    "Croatia": dict(
        name="Croatia", alt=["Republic of Croatia", "Hrvatska"],
        capital="Zagreb", cap_alt=[], lon=15.9819, lat=45.8150),
    "Slovenia": dict(
        name="Slovenia", alt=["Republic of Slovenia"],
        capital="Ljubljana", cap_alt=[], lon=14.5058, lat=46.0569),
    "Qatar": dict(
        name="Qatar", alt=["State of Qatar"],
        capital="Doha", cap_alt=["Ad Dawhah"], lon=51.5310, lat=25.2854),
    "Saudi Arabia": dict(
        name="Saudi Arabia", alt=["Kingdom of Saudi Arabia", "KSA"],
        capital="Riyadh", cap_alt=["Ar Riyad"], lon=46.6753, lat=24.7136),
    "Botswana": dict(
        name="Botswana", alt=["Republic of Botswana", "Bechuanaland"],
        capital="Gaborone", cap_alt=[], lon=25.9231, lat=-24.6282),
    "Zimbabwe": dict(
        name="Zimbabwe", alt=["Republic of Zimbabwe", "Rhodesia"],
        capital="Harare", cap_alt=["Salisbury"], lon=31.0530, lat=-17.8252),
    "Pakistan": dict(
        name="Pakistan", alt=["Islamic Republic of Pakistan"],
        capital="Islamabad", cap_alt=[], lon=73.0479, lat=33.6844),
    "Bulgaria": dict(
        name="Bulgaria", alt=["Republic of Bulgaria"],
        capital="Sofia", cap_alt=["Sofiya"], lon=23.3219, lat=42.6977),
    "Thailand": dict(
        name="Thailand", alt=["Kingdom of Thailand", "Siam"],
        capital="Bangkok", cap_alt=["Krung Thep"], lon=100.5018, lat=13.7563),
    "San Marino": dict(
        name="San Marino", alt=["Republic of San Marino"],
        capital="San Marino", cap_alt=["City of San Marino"], lon=12.4578, lat=43.9424),
    "Haiti": dict(
        name="Haiti", alt=["Republic of Haiti"],
        capital="Port-au-Prince", cap_alt=[], lon=-72.3388, lat=18.5944),
    "Dominican Republic": dict(
        name="Dominican Republic", alt=[],
        capital="Santo Domingo", cap_alt=[], lon=-69.9312, lat=18.4861),
    "Chad": dict(
        name="Chad", alt=["Republic of Chad", "Tchad"],
        capital="N'Djamena", cap_alt=["Ndjamena", "Fort-Lamy"], lon=15.0557, lat=12.1348),
    "Kuwait": dict(
        name="Kuwait", alt=["State of Kuwait"],
        capital="Kuwait City", cap_alt=["Kuwait", "Al Kuwayt"], lon=47.9774, lat=29.3759),
    "El Salvador": dict(
        name="El Salvador", alt=["Republic of El Salvador"],
        capital="San Salvador", cap_alt=[], lon=-89.2182, lat=13.6929),
    "Guatemala": dict(
        name="Guatemala", alt=["Republic of Guatemala"],
        capital="Guatemala City", cap_alt=["Guatemala", "Ciudad de Guatemala"],
        lon=-90.5133, lat=14.6349),
    "East Timor": dict(
        name="East Timor", alt=["Timor-Leste"],
        capital="Dili", cap_alt=[], lon=125.5603, lat=-8.5569),
    "Brunei": dict(
        name="Brunei", alt=["Brunei Darussalam"],
        capital="Bandar Seri Begawan", cap_alt=[], lon=114.9481, lat=4.9031),
    "Monaco": dict(
        name="Monaco", alt=["Principality of Monaco"],
        capital="Monaco", cap_alt=["Monaco-Ville", "Monte Carlo"], lon=7.4246, lat=43.7384),
    "Algeria": dict(
        name="Algeria", alt=["Peoples Democratic Republic of Algeria"],
        capital="Algiers", cap_alt=["Alger", "El Djazair"], lon=3.0588, lat=36.7538),
    "Mozambique": dict(
        name="Mozambique", alt=["Republic of Mozambique"],
        capital="Maputo", cap_alt=["Lourenco Marques"], lon=32.5732, lat=-25.9692),
    "eSwatini": dict(
        name="Eswatini", alt=["Swaziland", "Kingdom of Eswatini"],
        capital="Mbabane", cap_alt=["Lobamba"], lon=31.1367, lat=-26.3054),
    "Burundi": dict(
        name="Burundi", alt=["Republic of Burundi"],
        capital="Gitega", cap_alt=["Bujumbura"], lon=29.9246, lat=-3.4271),
    "Rwanda": dict(
        name="Rwanda", alt=["Republic of Rwanda"],
        capital="Kigali", cap_alt=[], lon=30.0619, lat=-1.9441),
    "Myanmar": dict(
        name="Myanmar", alt=["Burma"],
        capital="Naypyidaw", cap_alt=["Nay Pyi Taw", "Rangoon", "Yangon"],
        lon=96.0785, lat=19.7633),
    "Bangladesh": dict(
        name="Bangladesh", alt=["Peoples Republic of Bangladesh"],
        capital="Dhaka", cap_alt=["Dacca"], lon=90.4125, lat=23.8103),
    "Andorra": dict(
        name="Andorra", alt=["Principality of Andorra"],
        capital="Andorra la Vella", cap_alt=[], lon=1.5218, lat=42.5063),
    "Afghanistan": dict(
        name="Afghanistan", alt=["Islamic Emirate of Afghanistan"],
        capital="Kabul", cap_alt=[], lon=69.2075, lat=34.5553),
    "Montenegro": dict(
        name="Montenegro", alt=["Crna Gora"],
        capital="Podgorica", cap_alt=["Titograd"], lon=19.2594, lat=42.4304),
    "Bosnia and Herzegovina": dict(
        name="Bosnia and Herzegovina", alt=["Bosnia"],
        capital="Sarajevo", cap_alt=[], lon=18.4131, lat=43.8563),
    "Uganda": dict(
        name="Uganda", alt=["Republic of Uganda"],
        capital="Kampala", cap_alt=[], lon=32.5825, lat=0.3476),
    "Cuba": dict(
        name="Cuba", alt=["Republic of Cuba"],
        capital="Havana", cap_alt=["La Habana"], lon=-82.3666, lat=23.1136),
    "Honduras": dict(
        name="Honduras", alt=["Republic of Honduras"],
        capital="Tegucigalpa", cap_alt=[], lon=-87.1921, lat=14.0723),
    "Ecuador": dict(
        name="Ecuador", alt=["Republic of Ecuador"],
        capital="Quito", cap_alt=[], lon=-78.4678, lat=-0.1807),
    "Colombia": dict(
        name="Colombia", alt=["Republic of Colombia"],
        capital="Bogota", cap_alt=[], lon=-74.0721, lat=4.7110),
    "Paraguay": dict(
        name="Paraguay", alt=["Republic of Paraguay"],
        capital="Asuncion", cap_alt=[], lon=-57.5759, lat=-25.2637),
    "Portugal": dict(
        name="Portugal", alt=["Portuguese Republic"],
        capital="Lisbon", cap_alt=["Lisboa"], lon=-9.1393, lat=38.7223),
    "Moldova": dict(
        name="Moldova", alt=["Republic of Moldova"],
        capital="Chisinau", cap_alt=["Kishinev"], lon=28.8638, lat=47.0105),
    "Turkmenistan": dict(
        name="Turkmenistan", alt=[],
        capital="Ashgabat", cap_alt=["Ashkhabad"], lon=58.3261, lat=37.9601),
    "Jordan": dict(
        name="Jordan", alt=["Hashemite Kingdom of Jordan"],
        capital="Amman", cap_alt=[], lon=35.9106, lat=31.9454),
    "Nepal": dict(
        name="Nepal", alt=["Federal Democratic Republic of Nepal"],
        capital="Kathmandu", cap_alt=["Katmandu"], lon=85.3240, lat=27.7172),
    "Lesotho": dict(
        name="Lesotho", alt=["Kingdom of Lesotho", "Basutoland"],
        capital="Maseru", cap_alt=[], lon=27.4869, lat=-29.3151),
    "Cameroon": dict(
        name="Cameroon", alt=["Republic of Cameroon"],
        capital="Yaounde", cap_alt=[], lon=11.5021, lat=3.8480),
    "Gabon": dict(
        name="Gabon", alt=["Gabonese Republic"],
        capital="Libreville", cap_alt=[], lon=9.4673, lat=0.4162),
    "Niger": dict(
        name="Niger", alt=["Republic of the Niger"],
        capital="Niamey", cap_alt=[], lon=2.1254, lat=13.5127),
    "Burkina Faso": dict(
        name="Burkina Faso", alt=["Upper Volta"],
        capital="Ouagadougou", cap_alt=[], lon=-1.5197, lat=12.3714),
    "Togo": dict(
        name="Togo", alt=["Togolese Republic"],
        capital="Lome", cap_alt=[], lon=1.2255, lat=6.1725),
    "Ghana": dict(
        name="Ghana", alt=["Republic of Ghana", "Gold Coast"],
        capital="Accra", cap_alt=[], lon=-0.1870, lat=5.6037),
    "Guinea-Bissau": dict(
        name="Guinea-Bissau", alt=["Republic of Guinea-Bissau"],
        capital="Bissau", cap_alt=[], lon=-15.5977, lat=11.8817),
    "United States of America": dict(
        name="United States", alt=["USA", "US", "America",
                                   "United States of America"],
        capital="Washington, D.C.", cap_alt=["Washington", "DC", "Washington DC"],
        lon=-77.0369, lat=38.9072),
    "Canada": dict(
        name="Canada", alt=[],
        capital="Ottawa", cap_alt=[], lon=-75.6972, lat=45.4215),
    "Mexico": dict(
        name="Mexico", alt=["United Mexican States"],
        capital="Mexico City", cap_alt=["Ciudad de Mexico", "Mexico"],
        lon=-99.1332, lat=19.4326),
    "Belize": dict(
        name="Belize", alt=["British Honduras"],
        capital="Belmopan", cap_alt=[], lon=-88.7713, lat=17.2510),
    "Panama": dict(
        name="Panama", alt=["Republic of Panama"],
        capital="Panama City", cap_alt=["Panama", "Ciudad de Panama"],
        lon=-79.5199, lat=8.9824),
    "Venezuela": dict(
        name="Venezuela", alt=["Bolivarian Republic of Venezuela"],
        capital="Caracas", cap_alt=[], lon=-66.9036, lat=10.4806),
    "Papua New Guinea": dict(
        name="Papua New Guinea", alt=["PNG"],
        capital="Port Moresby", cap_alt=[], lon=147.1803, lat=-9.4438),
    "Yemen": dict(
        name="Yemen", alt=["Republic of Yemen"],
        capital="Sanaa", cap_alt=["Sana"], lon=44.2067, lat=15.3694),
    "Mauritania": dict(
        name="Mauritania", alt=["Islamic Republic of Mauritania"],
        capital="Nouakchott", cap_alt=[], lon=-15.9785, lat=18.0735),
    "Equatorial Guinea": dict(
        name="Equatorial Guinea", alt=["Republic of Equatorial Guinea"],
        capital="Malabo", cap_alt=["Ciudad de la Paz", "Djibloho", "Oyala"],
        lon=8.7832, lat=3.7523),
    "Gambia": dict(
        name="Gambia", alt=["Republic of the Gambia"],
        capital="Banjul", cap_alt=["Bathurst"], lon=-16.5790, lat=13.4549),
    "Australia": dict(
        name="Australia", alt=["Commonwealth of Australia"],
        capital="Canberra", cap_alt=[], lon=149.1300, lat=-35.2809),
    "Fiji": dict(
        name="Fiji", alt=["Republic of Fiji"],
        capital="Suva", cap_alt=[], lon=178.4419, lat=-18.1416),
    "New Zealand": dict(
        name="New Zealand", alt=["NZ", "Aotearoa"],
        capital="Wellington", cap_alt=[], lon=174.7762, lat=-41.2865),
    "Madagascar": dict(
        name="Madagascar", alt=["Republic of Madagascar"],
        capital="Antananarivo", cap_alt=["Tananarive"], lon=47.5079, lat=-18.8792),
    "Philippines": dict(
        name="Philippines", alt=["Republic of the Philippines"],
        capital="Manila", cap_alt=["Quezon City"], lon=120.9842, lat=14.5995),
    "Sri Lanka": dict(
        name="Sri Lanka", alt=["Democratic Socialist Republic of Sri Lanka", "Ceylon"],
        capital="Colombo", cap_alt=["Sri Jayawardenepura Kotte", "Kotte"],
        lon=79.8612, lat=6.9271),
    "The Bahamas": dict(
        name="Bahamas", alt=["Commonwealth of the Bahamas"],
        capital="Nassau", cap_alt=[], lon=-77.3554, lat=25.0443),
    "Japan": dict(
        name="Japan", alt=["Nippon", "Nihon"],
        capital="Tokyo", cap_alt=["Edo"], lon=139.6917, lat=35.6895),
    "Iceland": dict(
        name="Iceland", alt=["Republic of Iceland"],
        capital="Reykjavik", cap_alt=[], lon=-21.9426, lat=64.1466),
    "Seychelles": dict(
        name="Seychelles", alt=["Republic of Seychelles"],
        capital="Victoria", cap_alt=[], lon=55.4513, lat=-4.6191),
    "Kiribati": dict(
        name="Kiribati", alt=["Republic of Kiribati"],
        capital="Tarawa", cap_alt=["South Tarawa", "Bairiki"], lon=172.9717, lat=1.3278),
    "Marshall Islands": dict(
        name="Marshall Islands", alt=["Republic of the Marshall Islands"],
        capital="Majuro", cap_alt=[], lon=171.1845, lat=7.0897),
    "Trinidad and Tobago": dict(
        name="Trinidad and Tobago", alt=["Trinidad"],
        capital="Port of Spain", cap_alt=["Port-of-Spain"], lon=-61.5189, lat=10.6549),
    "Grenada": dict(
        name="Grenada", alt=[],
        capital="Saint George's", cap_alt=[], lon=-61.7519, lat=12.0561),
    "Saint Vincent and the Grenadines": dict(
        name="Saint Vincent and the Grenadines", alt=["Saint Vincent"],
        capital="Kingstown", cap_alt=[], lon=-61.2248, lat=13.1600),
    "Barbados": dict(
        name="Barbados", alt=[],
        capital="Bridgetown", cap_alt=[], lon=-59.6132, lat=13.1132),
    "Saint Lucia": dict(
        name="Saint Lucia", alt=[],
        capital="Castries", cap_alt=[], lon=-60.9875, lat=14.0101),
    "Dominica": dict(
        name="Dominica", alt=["Commonwealth of Dominica"],
        capital="Roseau", cap_alt=[], lon=-61.3870, lat=15.3092),
    "Antigua and Barbuda": dict(
        name="Antigua and Barbuda", alt=["Antigua"],
        capital="Saint John's", cap_alt=[], lon=-61.8456, lat=17.1274),
    "Saint Kitts and Nevis": dict(
        name="Saint Kitts and Nevis", alt=["Saint Kitts", "Saint Christopher and Nevis"],
        capital="Basseterre", cap_alt=[], lon=-62.7177, lat=17.3026),
    "Jamaica": dict(
        name="Jamaica", alt=[],
        capital="Kingston", cap_alt=[], lon=-76.7936, lat=17.9714),
    "Mauritius": dict(
        name="Mauritius", alt=["Republic of Mauritius"],
        capital="Port Louis", cap_alt=[], lon=57.5012, lat=-20.1609),
    "Comoros": dict(
        name="Comoros", alt=["Union of the Comoros"],
        capital="Moroni", cap_alt=[], lon=43.2551, lat=-11.7172),
    "São Tomé and Principe": dict(
        name="Sao Tome and Principe", alt=[],
        capital="Sao Tome", cap_alt=[], lon=6.7273, lat=0.3302),
    "Cabo Verde": dict(
        name="Cape Verde", alt=["Cabo Verde", "Republic of Cabo Verde"],
        capital="Praia", cap_alt=[], lon=-23.5087, lat=14.9330),
    "Malta": dict(
        name="Malta", alt=["Republic of Malta"],
        capital="Valletta", cap_alt=[], lon=14.5146, lat=35.8989),
    "Singapore": dict(
        name="Singapore", alt=["Republic of Singapore"],
        capital="Singapore", cap_alt=["Singapore City"], lon=103.8198, lat=1.3521),
    "Tonga": dict(
        name="Tonga", alt=["Kingdom of Tonga"],
        capital="Nuku'alofa", cap_alt=[], lon=-175.1982, lat=-21.1393),
    "Samoa": dict(
        name="Samoa", alt=["Independent State of Samoa", "Western Samoa"],
        capital="Apia", cap_alt=[], lon=-171.7514, lat=-13.8333),
    "Solomon Islands": dict(
        name="Solomon Islands", alt=[],
        capital="Honiara", cap_alt=[], lon=159.9729, lat=-9.4456),
    "Tuvalu": dict(
        name="Tuvalu", alt=["Ellice Islands"],
        capital="Funafuti", cap_alt=[], lon=179.1942, lat=-8.5211),
    "Maldives": dict(
        name="Maldives", alt=["Republic of Maldives"],
        capital="Male", cap_alt=[], lon=73.5093, lat=4.1755),
    "Nauru": dict(
        name="Nauru", alt=["Republic of Nauru"],
        capital="Yaren", cap_alt=[], lon=166.9209, lat=-0.5477),
    "Federated States of Micronesia": dict(
        name="Micronesia", alt=["Federated States of Micronesia", "FSM"],
        capital="Palikir", cap_alt=[], lon=158.1610, lat=6.9248),
    "Vanuatu": dict(
        name="Vanuatu", alt=["Republic of Vanuatu", "New Hebrides"],
        capital="Port Vila", cap_alt=["Port-Vila"], lon=168.3273, lat=-17.7333),
    "Palau": dict(
        name="Palau", alt=["Republic of Palau", "Belau"],
        capital="Ngerulmud", cap_alt=["Melekeok"], lon=134.6243, lat=7.5006),
    "Bahrain": dict(
        name="Bahrain", alt=["Kingdom of Bahrain"],
        capital="Manama", cap_alt=["Al Manamah"], lon=50.5877, lat=26.2285),
    "Palestine": dict(
        name="Palestine", alt=["State of Palestine"],
        capital="Ramallah", cap_alt=["East Jerusalem", "Jerusalem"],
        lon=35.2064, lat=31.9038),
    "Kosovo": dict(
        name="Kosovo", alt=["Republic of Kosovo"],
        capital="Pristina", cap_alt=["Prishtina"], lon=21.1655, lat=42.6629),
    "Vatican": dict(
        name="Vatican City", alt=["Vatican", "Holy See"],
        capital="Vatican City", cap_alt=["Vatican"], lon=12.4534, lat=41.9029),
    "Taiwan": dict(
        name="Taiwan", alt=["Republic of China", "Chinese Taipei", "Formosa"],
        capital="Taipei", cap_alt=[], lon=121.5654, lat=25.0330),
}
