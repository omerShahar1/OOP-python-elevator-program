import json
import csv
import sys
from call import Call
from elevator import Elevator
from building import Building


# return the id of the best elevator to use. also insert the call to the elevator calls list (and its data to the other lists)
def best_elevator(b: Building, call: Call) -> int:
    if len(b.elevators) == 1:
        return 0
    answer = 0
    bestTime = 0
    firstTime = True

    for elev in b.elevators:
        list1 = elev.upList.copy()
        list2 = elev.downList.copy()
        list3 = elev.newUpList.copy()
        list4 = elev.newDownList.copy()

        if firstTime:
            firstTime = False
            elevator_time(elev, call)
            answer = elev.id
            bestTime = elev.time
        else:
            elevator_time(elev, call)
            if elev.time < bestTime:
                answer = elev.id
                bestTime = elev.time
        # print(elev.id, ": ", elev.time)
        # print(b.elevators[0].upList)
        Elevator.zero_data(elev)
        elev.upList = list1.copy()
        elev.downList = list2.copy()
        elev.newUpList = list3.copy()
        elev.newDownList = list4.copy()

    # add the new call to the selected elevator calls list and return the elevator number.
    Elevator.add_call(b.elevators[answer], call)
    return answer


# return the elevator total time to run
def elevator_time(elevator: Elevator, call: Call):
    if len(elevator.calls) == 0:
        return case_0(elevator, call)

    return case_2(elevator, call)


def case_0(elevator: Elevator, call: Call):
    if elevator.current == call.src:
        elevator.time = elevator.time + elevator.openTime + elevator.closeTime
    else:
        move(elevator, elevator.current, call.src)
        elevator.current = call.src

    move(elevator, elevator.current, call.dest)
    elevator.current = call.dest


def case_2(elevator: Elevator, call: Call):
    if elevator.calls[0].type == 1:
        goUp(elevator, call)
    else:
        goDown(elevator, call)


# insert the call data (src and dest) to the correct floors list.
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


# send the elevator down
def goDown(elevator: Elevator, call: Call):
    elevator.sign = -1
    for floor in elevator.downList:
        if call.start:
            insert_floors(elevator, call)
        if len(elevator.upList) == 0:
            Elevator.switch_down_list(elevator)
            goUp(elevator, call)
        if elevator.current != floor:
            move(elevator, elevator.current, floor)
        elevator.current = floor
        elevator.downList.pop(0)


# send the elevator up
def goUp(elevator: Elevator, call: Call):
    elevator.sign = 1
    for floor in elevator.upList:
        if call.start:
            insert_floors(elevator, call)
        if len(elevator.upList) == 0:
            Elevator.switch_up_list(elevator)
            goDown(elevator, call)
        if elevator.current != floor:
            move(elevator, elevator.current, floor)
        elevator.current = floor
        elevator.upList.pop(0)


# change the time of the elevator as if it moved from one floor to another
def move(elev: Elevator, current: int, next: int):
    if current > next:
        dist = current - next
    else:
        dist = next - current
    elev.time = elev.time + (dist / elev.speed) + elev.startTime + elev.stopTime + elev.closeTime + elev.openTime


args1 = sys.argv[1]
args2 = sys.argv[2]
args3 = sys.argv[3]
# opening JSON file (Building.json) and load it in to a dictionary (data)

b = Building(args1)

# open csv file (calls)
with open(args2, 'r') as calls_file:
    csv_reader = csv.reader(calls_file)
    with open(args3, "w", newline='\n') as output:
        csvWriter = csv.writer(output)
        # go over all the lines in the csv file
        for row in csv_reader:
            call = Call(float(row[1]), int(row[2]), int(row[3]))
            answer = best_elevator(b, call)
            row[5] = answer
            csvWriter.writerow(row)


