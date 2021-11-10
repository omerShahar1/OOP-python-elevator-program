import json
import csv
from call import Call
from elevator import Elevator
from building import Building

# opening JSON file (Building.json) and load it in to a dictionary (data)
with open('Building.json') as json_file:
    data = json.load(json_file)

# create building b with the data from the json file
b = Building(data['_minFloor'], data['_maxFloor'])
# add elevators to the building object
for i in data['_elevators']:
    elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'],i['_startTime'], i['_stopTime'])
    Building.add_elevator(b, elev)


# open csv file (calls)
with open('calls.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# go over all the lines in the csv file
for i in csv_reader.line_num:
    row = next(csv_reader)

#%%%%%%%%%%%%%%%%%%%5
