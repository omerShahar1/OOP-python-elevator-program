import json
import csv
import math
from call import Call
from elevator import Elevator
from building import Building


def best_elevator(b: Building, call: Call):
    """
    :param b: the current building
    :param call: the new call we need to address
    :return: elevator with lowest time to complete new call alongside the elevator current calls
    """
    b.elevators[0].calls.append(call)
    answer = b.elevators[0].id
    b.elevators[0].calls.remove(call)
    if len(b.elevators) == 1:  # if we only have 1 elevator, return it
        return answer

    for elev in len(b.elevators):
        elev.calls.append(call)
        newAnswer = check_elevator_time(elev)
        elev.calls.remove(call)
        if newAnswer < answer:
            answer = newAnswer
    return answer


def check_elevator_time(elev: Elevator):
    if check_type(1, elev):
        return up(elev)
    if check_type(0, elev):
        return down(elev)
    if check_above(elev):
        return calls_are_above(elev)
    if check_under(elev):
        return calls_are_under(elev)


    highDown = find_highest_down_call(elev)
    lowUp = find_lowest_up_call(elev)
    if highDown <= 0:
        return down_up(highDown, lowUp,  elev)
    if lowUp >= 0:
        return up_down(highDown, lowUp,  elev)
    if dist(0, highDown) < dist(0, lowUp):
        return down_up(highDown, lowUp,  elev)
    else:
        return up_down(highDown, lowUp,  elev)



def dist(num1: int, num2: int):
    """
    :param num1: first integer
    :param num2:  second integer
    :return: return the distance between num1 and num2
    """
    if num1 > num2:
        return (num1 - num2)
    else:
        return (num2 - num1)


def check_time(elev: Elevator, current, next):
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
    return (dist / elev.speed + elev.startTime + elev.stopTime + elev.closeTime + elev.stopTime)


def check_type(elevator: Elevator):
    pass


def up(elevator: Elevator):
    pass


def down(elevator: Elevator):
    pass


def check_above(elevator: Elevator):
    pass


def check_under(elevator: Elevator):
    pass


def calls_are_above(elevator: Elevator):
    pass


def calls_are_under(elevator: Elevator):
    pass

#tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt


def find_highest_down_call(elevator: Elevator):
    """
    :param elevator:
    :return: find the down call with the highest src floor and return that floor
    """
    firstTime = True
    answer = 0
    for i in elevator.calls:
        if i.type() == 0:
            if firstTime:
                firstTime = False
                answer = i.src
            else:
                if i.src > answer:
                    answer = i.src
    return answer


def find_lowest_up_call(elevator: Elevator):
    """
    :param elevator:
    :return: find the up call with the lowest src floor and return that floor
    """
    firstTime = True
    answer = 0
    for i in elevator.calls:
        if i.type() == 1:
            if firstTime:
                firstTime = False
                answer = i.src
            else:
                if i.src < answer:
                    answer = i.src
    return answer


def up_down(highDown:int, lowUp:int, elevator: Elevator):
    current = 0
    time = 0
    if current != lowUp:
        time = time + check_time(elevator, 0, lowUp)
        current = lowUp




def down_up(highDown:int, lowUp:int, elevator: Elevator):
    return 0


# opening JSON file (Building.json) and load it in to a dictionary (data)
with open('Building.json') as json_file:
    data = json.load(json_file)

# create building b with the data from the json file
b = Building(data['_minFloor'], data['_maxFloor'])
# add elevators to the building object
for i in data['_elevators']:
    elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'],
                    i['_startTime'], i['_stopTime'])
    Building.add_elevator(b, elev)

# open csv file (calls)
with open('calls.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# go over all the lines in the csv file
for i in csv_reader.line_num:
    row = next(csv_reader)
    call = Call(row[1], row[2], row[3])
    answer = best_elevator(call)
