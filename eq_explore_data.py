import json

filename = 'data\eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))


mags,lons,lats=[],[],[]

# Extract Magnitude, Longitude  and Latitude of every Earthquake:

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lan = eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lan)


print(mags[:10])
print(lons[:10])
print(lats[:10])