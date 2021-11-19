from call import Call


class Elevator:
    def __init__(self, id: int, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float,
                 startTime: float, stopTime: float):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime

        self.current = 0  # current floor of the elevator
        self.sign = 0  # up=1, down=-1 startMode=0
        self.time = 0.0  # how much time passed since the elevator started moving
        self.calls = []  # list of elevator current calls
        self.upList = []  # list of floors the elevator need to reach while going up
        self.newUpList = []  # list of floors the elevator need to reach in the next time it goes up
        self.downList = []  # list of floors the elevator need to reach while going down
        self.newDownList = []  # list of floors the elevator need to reach in the next time it goes down


    def zero_data(self):  # zero out all the data (make the elevator looks like it just now starting to move)
        self.current = 0
        self.time = 0
        self.sign = 0
        self.upList.clear()
        self.downList.clear()
        self.newUpList.clear()
        self.newDownList.clear()

    def add_call(self, call: Call):  # accept call and insert it to the calls list. then insert the call data to the correct floors list.
        if call.type == 1:
            if len(self.upList) == 0 or call.src > self.upList[-1]:  # if empty or if src bigger then last floor in the list just insert
                self.upList.append(call.src)
                self.upList.append(call.dest)
                return
            self.newUpList.append(call.src)
            self.newUpList.append(call.dest)
            self.newUpList.sort()
            return
        else:
            if len(self.downList) == 0 or call.src < self.downList[-1]:  # if empty or if src smaller then last floor in the list just insert
                self.downList.append(call.src)
                self.downList.append(call.dest)
                return
            self.newDownList.append(call.src)
            self.newDownList.append(call.dest)
            self.newDownList.sort()
            self.newDownList.reverse()
        self.calls.append(call)

    def switch_up_list(self):  # insert the newUpList values in to the empty upList
        self.upList.clear()
        for i in self.newUpList:
            self.upList.append(i)
        self.newUpList.clear()

    def switch_down_list(self):  # insert the newDownList values in to the empty downList
        self.downList.clear()
        for i in self.newDownList:
            self.downList.append(i)
        self.newDownList.clear()
