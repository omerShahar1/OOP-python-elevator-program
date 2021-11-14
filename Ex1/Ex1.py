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
    # if we only have 1 elevator, return it and add the call to the elevator calls list.
    if len(b.elevators) == 1:
        b.elevators[0].calls.append(call)
        return b.elevators[0].id

    # we assume the building has at least 1 elevator, so we start by claiming the first is the best elevator.
    answer = b.elevators[0].id
    b.elevators[0].calls.append(call)
    bestTime = check_elevator_time(b.elevators[0])
    b.elevators[0].calls.remove(call)

    # go over all the elevators in the building, add the new call to their calls list and check new time for each.
    for elev in b.elevators:
        elev.calls.append(call)
        newTime = check_elevator_time(elev)
        elev.calls.remove(call)
        if newTime < bestTime:
            answer = elev.id
            bestTime = newTime

    # add the new call to the selected elevator calls list and return the elevator number.
    b.elevators[answer].calls.append(call)
    return answer


def check_elevator_time(elev: Elevator):
    """
    :param elev:
    :return: return the new time it will take the elevator to answer all its calls
    """
    # check if all calls are up type
    if check_type(1, elev):
        return up(elev)
    # check if all calls are down type
    if check_type(0, elev):
        return down(elev)
    # check if all calls are above 0 (starting floor)
    if check_above(elev):
        return up_down(elev)
    # check if all calls are under 0 (starting floor)
    if check_under(elev):
        return down_up(elev)
    highDown = find_highest_down_call(elev)
    lowUp = find_lowest_up_call(elev)
    # check if highest src floor with down call is under 0 (starting floor)
    if highDown <= 0:
        return down_up(elev)
    # check if lowest src floor with up call is above 0 (starting floor)
    if lowUp >= 0:
        return up_down(elev)
    # check who is closer, the highest src floor with down call or the lowest src floor with up call.
    if dist(0, highDown) < dist(0, lowUp):
        return down_up(elev)
    else:
        return up_down(elev)


def dist(num1: int, num2: int) -> int:
    """
    :param num1: first integer
    :param num2:  second integer
    :return: return the distance between num1 and num2
    """
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


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
    return (dist / elev.speed + elev.startTime + elev.stopTime + elev.closeTime + elev.stopTime)


def check_type(direction: int, elevator: Elevator) -> int:
    """
    :param direction: up (1) or down (0)
    :param elevator:
    :return: return true if all calls in the elevator list are 'direction' type
    """
    for call in elevator.calls:
        if Call.type(call) != direction:
            return False
    return True


def up(elevator: Elevator) -> float:
    """
    :param elevator:
    :return: return the time it will take for only up calls
    """
    upList = create_up_list(elevator)
    current = 0
    time = 0.0

    for floor in upList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor
    return time


def down(elevator: Elevator) -> float:
    """
    :param elevator:
    :return: return the time it will take for only down calls
    """
    downList = create_down_list(elevator)
    current = 0
    time = 0.0

    for floor in downList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor
    return time


def check_above(elevator: Elevator) -> bool:
    """""
    :param elevator:
    :return: check if all the src and dest floors are above or equal 0
    """
    for i in elevator.calls:
        if i.src < 0 or i.dest < 0:
            return False
    return True


def check_under(elevator: Elevator) -> bool:
    """""
    :param elevator:
    :return: check if all the src and dest floors are under 0
    """
    for i in elevator.calls:
        if i.src > 0 or i.dest > 0:
            return False
    return True


def find_highest_down_call(elevator: Elevator) -> int:
    """
    :param elevator:
    :return: find the down call with the highest src floor and return that floor
    """
    firstTime = True
    answer = 0
    for call in elevator.calls:
        if Call.type(call) == 0:
            if firstTime:
                firstTime = False
                answer = call.src
            else:
                if call.src > answer:
                    answer = call.src
    return answer


def find_lowest_up_call(elevator: Elevator) -> int:
    """
    :param elevator:
    :return: find the up call with the lowest src floor and return that floor
    """
    firstTime = True
    answer = 0
    for call in elevator.calls:
        if Call.type(call) == 1:
            if firstTime:
                firstTime = False
                answer = call.src
            else:
                if call.src < answer:
                    answer = call.src
    return answer


def up_down(elevator: Elevator) -> float:
    upList = create_up_list(elevator)
    downList = create_down_list(elevator)
    current = 0
    time = 0.0

    for floor in upList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor

    for floor in downList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor
    return time


def down_up(elevator: Elevator) -> float:
    upList = create_up_list(elevator)
    downList = create_down_list(elevator)
    current = 0
    time = 0.0

    for floor in downList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor

    for floor in upList:
        if current != floor:
            time = time + check_time(elevator, current, floor)
        current = floor
    return time


def create_up_list(elevator: Elevator) -> list:
    """
    :param elevator:
    :return: sorted list (small to big) of floors for the elevator while going up
    """
    list = []
    for call in elevator.calls:
        if Call.type(call) == 1:
            list.append(call.src)
            list.append(call.dest)
    list.sort()
    return list


def create_down_list(elevator: Elevator) -> list:
    """
    :param elevator:
    :return: sorted list (big to small) of floors for the elevator while going down
    """
    list = []
    for call in elevator.calls:
        if Call.type(call) == 0:
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
    elev = Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'], i['_startTime'], i['_stopTime'])
    Building.add_elevator(b, elev)

# open csv file (calls)
with open('calls.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# go over all the lines in the csv file
for row in csv_reader:
    if (row[2] <= b.maxFloor) and (row[2] >= b.minFloor) and (row[3] <= b.maxFloor) and (row[3] >= b.minFloor):
        call = Call(row[1], row[2], row[3])
        answer = best_elevator(b, call)

