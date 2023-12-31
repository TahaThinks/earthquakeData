import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data\eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))


mags,lons,lats,hover_texts=[],[],[],[]

# Extract Magnitude, Longitude  and Latitude of every Earthquake:

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lan = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lan)
    hover_texts.append(title)


# Map the earthquake:
# 'marker-size' icreases size
# 'marker-color' choose which data to apply coloring
# 'marker-colorscale' which color to use
# 'marker-colorbar' add a bar for reference
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'},
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='global_earthquake.html')