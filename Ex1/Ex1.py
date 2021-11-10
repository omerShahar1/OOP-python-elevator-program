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
    elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'], i['_startTime'], i['_stopTime'])
    Building.add_elevator(b, elev)

# open csv file (calls)
with open('calls.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# go over all the lines in the csv file
for i in csv_reader.line_num:
    row = next(csv_reader)
    call = Call(row[1], row[2], row[3])


def best_elevator(call: Call):
    """
    :param call:
    :return: elevator with lowset time to complete new call alongside the elevator current calls
    """
    answer = b.elevators[0].id
    if len(b.elevators) == 1:  # if we only have 1 elevator, return it
        return answer

    for elev in len(b.elevators):
        newAnswer = check_elevator_time(elev, call)
        if newAnswer < answer:
            answer = newAnswer
    return answer


# need to complete
def check_elevator_time(elev: Elevator, call: Call):
    return 0
