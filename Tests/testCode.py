import unittest
import Ex1_main
from call import Call
from elevator import Elevator
from building import Building


class testCode_test(unittest.TestCase):
    elev_1 = Elevator(0, 1.0, -2, 10, 2.0, 2.0, 3.0, 3.0)
    elev_2 = Elevator(1, 11.859, -2, 10, 2.0, 2.0, 3.0, 3.0)
    elev_3 = Elevator(1, 100, -2, 10, 2.0, 2.0, 3.0, 3.0)

    call_1 = Call(18.7729931796688, -1, -2)
    call_2 = Call(19.5908696496569, 0, 7)

    build_1 = Building("..\data\Ex1_input\Ex1_Buildings\B1.json")
    build_2 = Building("..\data\Ex1_input\Ex1_Buildings\B2.json")

    def test_move(self):
        Ex1_main.move(self.elev_1, 1, 2)
        self.assertEqual(self.elev_1.time, 11.0)

        Ex1_main.move(self.elev_2, 8, 2)
        self.assertEqual(self.elev_2.time, 10.505944852011131)

    def test_goUp(self):
        Ex1_main.goUp(self.elev_1, self.call_1)
        self.assertEqual(self.elev_1.sign, 1)

        Ex1_main.goUp(self.elev_2, self.call_2)
        self.assertNotEqual(self.elev_2.sign, 5)

        Ex1_main.goUp(self.elev_1, self.call_2)
        self.assertEqual(self.elev_1.current, 0)

    def test_goDown(self):
        Ex1_main.goDown(self.elev_1, self.call_1)
        self.assertEqual(self.elev_1.sign, -1)

        Ex1_main.goDown(self.elev_2, self.call_1)
        self.assertNotEqual(self.elev_2.sign, 1)

    def test_insert_floors(self):
        Ex1_main.insert_floors(self.elev_1, self.call_1)
        self.assertNotEqual(self.call_1.time, self.elev_1.time)

        Ex1_main.insert_floors(self.elev_2, self.call_1)
        self.assertGreater(self.call_1.time, self.elev_2.time)

        self.assertEqual(Ex1_main.insert_floors(self.elev_3, self.call_1), None)

        Ex1_main.insert_floors(self.elev_3, self.call_1)
        self.assertEqual(self.call_1.start, False)

    def test_best_elevator(self):
        Ex1_main.best_elevator(self.build_1, self.call_1)
        self.assertEqual(len(self.build_1.elevators), 1)
        self.assertNotEqual(len(self.build_2.elevators), 1)

        self.assertEqual(Ex1_main.best_elevator(self.build_1, self.call_1), 0)
        self.assertEqual(Ex1_main.best_elevator(self.build_2, self.call_2), 1)


if __name__ == '__main__':
    unittest.main()
























"""import csv
import unittest
from Ex1_main import *
from call import Call
from elevator import Elevator
from building import Building

class TestCode(unittest.TestCase):

    def test_case_1(self):
        building_data = "C:/Users/Talia/IdeaProjects/Ex1_oop_ariel/data/Ex1_input/Ex1_Buildings/B2.json"
        calls_data    = "C:/Users/Talia/IdeaProjects/Ex1_oop_ariel/data/Ex1_Calls_case_2_b.csv"

        building = Building(building_data)
        print(building.elevators)
        #self.assertEqual(building.elevators, 2)



        with open(calls_data, 'r') as calls_file:
            csv_reader = csv.reader(calls_file)
            rows       = []
            for row in csv_reader:
                rows.append(row)

            # Call 1
            call = Call(float(rows[0][1]), int(rows[0][2]), int(rows[0][3]))
            answer = best_elevator(building, call)
            rows[0][5] = answer
            self.assertEqual(answer, 2)


if __name__ == '__main__':
    unittest.main()"""
