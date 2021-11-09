import json
from elevator import Elevator
from building import Building

# opening JSON file
with open('B2.json') as building_json:
    data = json.load(building_json)

# create building with the data from the json file
b = Building(data['_minFloor'], data['_maxFloor'])

for i in data['_elevators']:
    elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'], i['_startTime'], i['_stopTime'])
    Building.add_elevator(b, elev)