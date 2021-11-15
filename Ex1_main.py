import json
import csv
import pandas
from call import Call
from elevator import Elevator
from building import Building


def best_elevator(b: Building, call: Call) -> int:
    if len(b.elevators) == 1:
        Elevator.add_call(b.elevators[0], call)
        return 0

    answer = 0
    newTime = 0
    bestTime = elevator_time(b.elevators[0], call)

    for elev in b.elevators:
        newTime = elevator_time(elev, call)
        if newTime < bestTime:
            answer = elev.id
            bestTime = newTime

    # add the new call to the selected elevator calls list and return the elevator number.
    b.elevators[answer].calls.append(call)
    return answer


def elevator_time(elevator: Elevator, call:Call):
    pass


def check_time(elev: Elevator, current: int, next: int) -> float:
    """
    :param elev: elevator we are testing
    :param current: current floor of elevator
    :param next: next floor of elevator
    :return: the total time it will take the elevator to get to 'next' floor
    """
    if current > next:
        dist = current - next
    else:
        dist = next - current
    return (dist / elev.speed) + elev.startTime + elev.stopTime + elev.closeTime + elev.stopTime




def main(a: list):
    args1 = a[1]
    args2 = a[2]
    args3 = a[3]
    # opening JSON file (Building.json) and load it in to a dictionary (data)
    with open(args1) as json_file:
        data = json.load(json_file)
        # create building b with the data from the json file
        b = Building(data['_minFloor'], data['_maxFloor'])
        # add elevators to the building object
        for i in data['_elevators']:
            elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'],
                            i['_startTime'], i['_stopTime'])
            Building.add_elevator(b, elev)

    # open csv file (calls)
    calls_file = open(args2, 'r')
    csv_reader = csv.reader(calls_file)
    output = pandas.read_csv(args3)
    count = 0
    # go over all the lines in the csv file
    for row in csv_reader:
        if b.maxFloor >= int(row[2]) >= b.minFloor and b.maxFloor >= int(row[3]) >= b.minFloor:
            call = Call(float(row[1]), int(row[2]), int(row[3]))
            answer = best_elevator(b, call)
            row[5] = answer
        output.loc[count] = row
        count = count + 1
    output.to_csv(args3, index=False)

    calls_file.close()
