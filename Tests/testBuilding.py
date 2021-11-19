import unittest
from building import Building
from elevator import Elevator

class testBuilding_test(unittest.TestCase):

    build_1 = Building("..\data\Ex1_input\Ex1_Buildings\B1.json")
    build_2 = Building("..\data\Ex1_input\Ex1_Buildings\B2.json")
    build_3 = Building("..\data\Ex1_input\Ex1_Buildings\B3.json")
    build_4 = Building("..\data\Ex1_input\Ex1_Buildings\B4.json")
    build_5 = Building("..\data\Ex1_input\Ex1_Buildings\B5.json")

    elev = Elevator(1, 2.0, -2, 10, 2.0, 2.0, 3.0, 3.0)

    def test_minFloor(self):
        self.assertEqual(self.build_1.minFloor, -2)
        self.assertEqual(self.build_2.minFloor, -2)
        self.assertEqual(self.build_3.minFloor, -10)
        self.assertEqual(self.build_4.minFloor, -10)
        self.assertEqual(self.build_5.minFloor, -10)

    def test_maxFloor(self):
        self.assertEqual(self.build_1.maxFloor, 10)
        self.assertEqual(self.build_2.maxFloor, 10)
        self.assertEqual(self.build_3.maxFloor, 100)
        self.assertEqual(self.build_4.maxFloor, 100)
        self.assertEqual(self.build_5.maxFloor, 100)

    def test_elevators(self):
        self.assertGreater(len(self.build_1.elevators),0)
        self.assertEqual(len(self.build_2.elevators),2)
        self.assertGreater(len(self.build_3.elevators),0)
        self.assertGreater(len(self.build_4.elevators),0)
        self.assertGreater(len(self.build_5.elevators),0)


if __name__ == '__main__':
    unittest.main()