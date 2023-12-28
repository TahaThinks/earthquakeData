import json

filename = 'data\eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)
