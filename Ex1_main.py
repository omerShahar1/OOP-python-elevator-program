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
    bestTime = b.elevators[0].time

    for elev in b.elevators:
        list1 = elev.upList.copy()
        list2 = elev.downList.copy()
        list3 = elev.newUpList.copy()
        list4 = elev.newDownList.copy()

        elevator_time(elev, call)
        if elev.time < bestTime:
            answer = elev.id
            bestTime = elev.time
        elev.time = 0.0
        elev.upList = list1.copy()
        elev.downList = list2.copy()
        elev.newUpList = list3.copy()
        elev.newDownList = list4.copy()
        if len(elev.calls) != 0:
            b.elevators[answer].sign = b.elevators[answer].calls[0].type


    # add the new call to the selected elevator calls list and return the elevator number.
    b.elevators[answer].calls.append(call)
    return answer


def elevator_time(elevator: Elevator, call: Call):
    if len(elevator.calls) == 0:
        return case_0(elevator, call)

    if call.type == 1 and elevator.sign == 1 and call.src > elevator.current:
        return case_1_up(elevator, call)

    if call.type == -1 and elevator.sign == -1 and call.src < elevator.current:
        return case_1_down(elevator, call)
    return case_2(elevator, call)


def case_0(elevator: Elevator, call: Call):
    pass


def case_1_up(elevator: Elevator, call: Call):
    pass


def case_1_down(elevator: Elevator, call: Call):
    pass


def case_2(elevator: Elevator, call: Call):
    if elevator.sign == 1:
        goUp(elevator, 0.0)
    else:
        goDown(elevator, 0.0)


def insert_floors(elevator: Elevator, call: Call):
    # if the time to insert the call hasn't arrived yet, then stop
    if call.time < elevator.time:
        return
    if call.type == 1:  # if call type up
        if elevator.current > call.src:
            elevator.newUpList.append(call.src)
            elevator.newUpList.append(call.dest)
            elevator.newUpList.sort()
        else:
            elevator.upList.append(call.src)
            elevator.upList.append(call.dest)
            elevator.upList.sort()
    else:  # if call type down
        if elevator.current < call.src:
            elevator.newDownList.append(call.src)
            elevator.newDownList.append(call.dest)
            elevator.newDownList.sort()
            elevator.newDownList.reverse()
        else:
            elevator.downList.append(call.src)
            elevator.downList.append(call.dest)
            elevator.downList.sort()
            elevator.newDownList.reverse()
    call.start = False


def goDown(elevator: Elevator, call: Call):
    elevator.sign = -1
    for floor in elevator.downList:
        if call.start:
            insert_floors(elevator, call)
        if len(elevator.upList) == 0:
            Elevator.switch_down_list(elevator)
            goUp(elevator)
        if elevator.current != floor:
            move(elevator, elevator.current, floor)
        elevator.current = floor
        elevator.downList.pop(0)


def goUp(elevator: Elevator, call: Call):
    elevator.sign = 1
    for floor in elevator.upList:
        if call.start:
            insert_floors(elevator, call)
        if len(elevator.upList) == 0:
            Elevator.switch_up_list(elevator)
            goDown(elevator)
        if elevator.current != floor:
            move(elevator, elevator.current, floor)
        elevator.current = floor
        elevator.upList.pop(0)


def move(elev: Elevator, current: int, next: int):
    if current > next:
        dist = current - next
    else:
        dist = next - current
    elev.time = elev.time + (dist / elev.speed) + elev.startTime + elev.stopTime + elev.closeTime + elev.stopTime


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
