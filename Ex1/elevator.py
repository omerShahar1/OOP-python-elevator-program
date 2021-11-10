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
        self.calls = []  # list of elevator current calls

    def add_call(self, call: Call):
        self.calls.append(call)
