import csv
import json
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle
from countries import get_country_code

# Load the data into a list.
filename = 'energy_use_data.csv'
with open(filename) as f:
    energy_data = csv.reader(f)
    next(energy_data)
    next(energy_data)
    next(energy_data)
    next(energy_data)
    header_row = next(energy_data)

    # Show the column header with associated index for reference later.
    for index, header in enumerate(header_row):
        print(index, header)

    # Sort the countries with data into a dictionary for mapping
    energy_use, success, error = {}, [], []
    for row in energy_data:
        try:
            country_name = row[0]
            code = get_country_code(country_name)
            value = int(float(row[54]))
            success.append(country_name)
            energy_use[code] = value
        except ValueError:
            print("Error with following data: "+ country_name)
            error.append(country_name)
print(len(success), len(error))

# Sort into categories to improve map color comparison.
low, mid, high = {}, {}, {}
for key, value in energy_use.items():
    if value <1000:
        low[key] = value
    elif value < 5000:
        mid[key] = value
    else:
        high[key] = value

# Plot the data.
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'Energy Use per Country in 2010\nkg Oil Equiv. Per Capita'
wm.add('<1000', low)
wm.add('<5000', mid)
wm.add('>5000', high)

wm.render_to_file("energy_use.svg")
