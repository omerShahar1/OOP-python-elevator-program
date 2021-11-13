import json
import csv
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

    for elev in b.elevators:
        elev.calls.append(call)
        newAnswer = check_elevator_time(elev)
        elev.calls.remove(call)
        if newAnswer < answer:
            answer = newAnswer
    return answer


def check_elevator_time(elev: Elevator):
    """
    :param elev:
    :return: return the new time it will take the elevator to answer all its calls
    """
    if check_type(1, elev):
        return up(elev)
    if check_type(0, elev):
        return down(elev)
    if check_above(elev):
        return up_down(elev)
    if check_under(elev):
        return down_up(elev)
    highDown = find_highest_down_call(elev)
    lowUp = find_lowest_up_call(elev)
    if highDown <= 0:
        return down_up(elev)
    if lowUp >= 0:
        return up_down(elev)
    if dist(0, highDown) < dist(0, lowUp):
        return down_up(elev)
    else:
        return up_down(elev)



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


def check_type(direction:int, elevator: Elevator):
    """
    :param elevator:
    :return: return true if all calls in the elevator list are 'direction' type
    """
    for i in elevator.calls:
        if i.type() != direction:
            return False
    return True


def up(elevator: Elevator):
    """
    :param elevator:
    :return: return the time it will take for only up calls
    """
    upList = create_up_list(elevator)
    current = 0
    time = 0

    if current != upList[0]:
        time = time + check_time(elevator, current, upList[0])
        current = upList[0]
    upList.pop(0)
    for floor in upList:
        time = time + check_time(elevator, current, floor)
        current = floor
    return time


def down(elevator: Elevator):
    """
    :param elevator:
    :return: return the time it will take for only down calls
    """
    downList = create_down_list(elevator)
    current = 0
    time = 0

    if current != downList[0]:
        time = time + check_time(elevator, current, downList[0])
        current = downList[0]
    downList.pop(0)
    for floor in downList:
        time = time + check_time(elevator, current, floor)
        current = floor
    return time


def check_above(elevator: Elevator):
    """""
    :param elevator:
    :return: check if all the src and dest floors are above 0
    """
    for i in elevator.calls:
        if i.src < 0 or i.dest < 0:
            return False
    return True


def check_under(elevator: Elevator):
    """""
    :param elevator:
    :return: check if all the src and dest floors are under 0
    """
    for i in elevator.calls:
        if i.src > 0 or i.dest > 0:
            return False
    return True


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


def up_down(elevator: Elevator):
    upList = create_up_list(elevator)
    downList = create_down_list(elevator)
    current = 0
    time = 0

    if current != upList[0]:
        time = time + check_time(elevator, current, upList[0])
        current = upList[0]
    upList.pop(0)
    for floor in upList:
        time = time + check_time(elevator, current, floor)
        current = floor

    if current != downList[0]:
        time = time + check_time(elevator, current, downList[0])
        current = downList[0]
    downList.pop(0)
    for floor in downList:
        time = time + check_time(elevator, current, floor)
        current = floor
    return time


def down_up(elevator: Elevator):
    upList = create_up_list(elevator)
    downList = create_down_list(elevator)
    current = 0
    time = 0

    if current != downList[0]:
        time = time + check_time(elevator, current, downList[0])
        current = downList[0]
    downList.pop(0)
    for floor in downList:
        time = time + check_time(elevator, current, floor)
        current = floor

    if current != upList[0]:
        time = time + check_time(elevator, current, upList[0])
        current = upList[0]
    upList.pop(0)
    for floor in upList:
        time = time + check_time(elevator, current, floor)
        current = floor
    return time


def create_up_list(elevator:Elevator):
    """
    :param elevator:
    :return: sorted list (small to big) of floors for the elevator while going up
    """
    list = []
    for call in elevator.calls:
        if call.type() == 1:
            list.append(call.src)
            list.append(call.dest)
    list.sort()
    return list


def create_down_list(elevator:Elevator):
    """
    :param elevator:
    :return: sorted list (big to small) of floors for the elevator while going down
    """
    list = []
    for call in elevator.calls:
        if call.type() == 0:
            list.append(call.src)
            list.append(call.dest)
    list.sort()
    list.reverse()
    return list


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
for i in csv_reader:
    row = next(csv_reader)
    if (row[2] <= b.maxFloor) & (row[2] >= b.minFloor) & (row[3] <= b.maxFloor) & (row[3] >= b.minFloor):
        call = Call(row[1], row[2], row[3])
        answer = best_elevator(b, call)
