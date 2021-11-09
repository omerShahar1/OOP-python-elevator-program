import elevator


class Building(object):
    def __init__(self, minFloor: int, maxFloor: int):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = []

    def add_elevator(self, elevator):
        self.elevators.append(elevator)
