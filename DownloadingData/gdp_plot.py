import json
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from countries import get_country_code

# Load the data into a list.
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Create a dictionary with only 2016 data.
gdp_2016 = {}
missing = []
for dataset in gdp_data:
    if dataset['Year'] == '2016-11-08':
        country_name = dataset['Country Name']
        country_gdp = int(float(dataset['Value']))
        code = get_country_code(country_name)
        if code:
            gdp_2016[code] = country_gdp
        else:
            missing.append(country_name)
            #print("Missing country code for: " + country_name)
number = str(len(missing))
print("Number of countries missing codes: " + number)

# Separate data into different GDP "levels".
level_1, level_2, level_3 = {}, {}, {}
for country_code, gdp in gdp_2016.items():
    gdp = int(gdp)
    if gdp < 100000000000:
        level_1[country_code] = gdp
    elif gdp < 1000000000000:
        level_2[country_code] = gdp
    else:
        level_3[country_code] = gdp
print(len(level_1), len(level_2), len(level_3))
# Plot the data.
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style, value_formatter=lambda x: '${:,}'.format(x))
wm.title = 'Gross Domestic Product (GDP) in 2016, by Country'
wm.add('GDP, <$100 bil.', level_1)
wm.add('GDP, >$100 bil.', level_2)
wm.add('GDP, >$1 tril.', level_3)

wm.render_to_file('gdp.svg')
