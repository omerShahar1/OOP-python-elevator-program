import csv
import sys
from call import Call
from elevator import Elevator
from building import Building


def best_elevator(b: Building, call: Call) -> int:
    """
    go over all the elvator in the building and return the id of the elevator who can complete the call in the best time.
    """
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


def elevator_time(elevator: Elevator, call: Call):
    """
    selector to check the elevator needed way of checking its time to complete calls
    """
    if len(elevator.calls) == 0:
        return case_0(elevator, call)

    return case_2(elevator, call)


def case_0(elevator: Elevator, call: Call):
    """
    if elevator has no previous calls then just check the new one from the floor 0 (elevator starting floor)
    """
    if elevator.current == call.src:
        elevator.time = elevator.time + elevator.openTime + elevator.closeTime
    else:
        move(elevator, elevator.current, call.src)
        elevator.current = call.src

    move(elevator, elevator.current, call.dest)
    elevator.current = call.dest


def case_2(elevator: Elevator, call: Call):
    """
    elevator at least 1 call. then check the elevator needed direction (first call type) and start moving in this direction.
    """
    if elevator.calls[0].type == 1:
        goUp(elevator, call)
    else:
        goDown(elevator, call)


def insert_floors(elevator: Elevator, call: Call):
    """
    insert the call data (src and dest) to the correct floors list.
    """
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
    """
    simulate the elevator down run. if finished run then insert data to next down run and start go up.
    """
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


def goUp(elevator: Elevator, call: Call):
    """
    simulate the elevator up run. if finished run then insert data to next up run and start go down.
    """
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


def move(elev: Elevator, current: int, next: int):
    """
    # change the time of the elevator as if it moved from one floor to another
    """
    if current > next:
        dist = current - next
    else:
        dist = next - current
    elev.time = elev.time + (dist / elev.speed) + elev.startTime + elev.stopTime + elev.closeTime + elev.openTime


args1 = sys.argv[1]
args2 = sys.argv[2]
args3 = sys.argv[3]

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


