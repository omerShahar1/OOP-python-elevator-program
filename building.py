import json
from elevator import Elevator


class Building:
    def __init__(self, building_json):

        with open(building_json, "r") as f:
            reader = json.load(f)
            self.minFloor = reader["_minFloor"]
            self.maxFloor = reader["_maxFloor"]
            self.elevators = []
            for i in reader["_elevators"]:
                self.elevators.append(
                    Elevator(i['_id'], i['_speed'], i['_minFloor'], i['_maxFloor'], i['_closeTime'], i['_openTime'],
                             i['_startTime'], i['_stopTime']))
