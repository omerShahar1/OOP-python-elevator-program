from call import Call


class Elevator:
    def __init__(self, id: int, speed: float, minFloor: int, maxFloor: int, closeTime: float, openTime: float, startTime: float, stopTime: float):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.current = 0
        self.sign = 0    # up=1, down=-1 startMode=0
        self.time = 0.0
        self.calls = []  # list of elevator current calls
        self.upList = []
        self.newUpList = []
        self.downList = []
        self.newDownList = []

    def zero_data(self):
        """
        :return:
        """
        self.current = 0
        self.time = 0
        if len(self.calls) == 0:
            self.sign = 0
        else:
            self.sign = self.calls[0].type
        self.upList.clear()
        self.downList.clear()
        self.newUpList.clear()
        self.newDownList.clear()

    # need to fix
    def fill_up_list(self):
        for call in self.calls:
            if len(self.upList) == 0:
                self.upList.append(call.src)
                self.upList.append(call.dest)
                continue
            if self.upList[0] > call.src:
                self.newUpList.append(call.src)
                self.newUpList.append(call.dest)
                self.newUpList.sort()
                continue
            self.upList.append(call.src)
            self.upList.append(call.dest)
            self.newUpList.sort()

    def switch_up_list(self):
        self.upList.clear()
        for i in self.newUpList:
            self.upList.append(i)
        self.newUpList.clear()

    def switch_down_list(self):
        self.downList.clear()
        for i in self.newDownList:
            self.downList.append(i)
        self.newDownList.clear()
