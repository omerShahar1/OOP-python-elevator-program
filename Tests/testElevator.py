import unittest
from elevator import Elevator


class testElevator_test(unittest.TestCase):

    elev_1 = Elevator(0, 1.0, -2, 10, 2.0, 2.0, 3.0, 3.0)
    elev_2 = Elevator(1, 2.0, -2, 10, 2.0, 2.0, 3.0, 3.0)
    elev_3 = Elevator(2, 7.0, -10, 100, 1.4285714285714286, 1.4285714285714286, 2.142857142857143, 2.142857142857143)
    elev_4 = Elevator(3, 3.0, -10, 100, 2.0, 2.0, 3.0, 3.0)
    elev_5 = Elevator(4, 9.0,-10, 100, 1.1111111111111112, 1.1111111111111112, 1.6666666666666667, 1.6666666666666667)


    def test_id(self):
        self.assertEqual(self.elev_1.id, 0)
        self.assertEqual(self.elev_2.id, 1)
        self.assertEqual(self.elev_3.id, 2)
        self.assertEqual(self.elev_4.id, 3)
        self.assertEqual(self.elev_5.id, 4)


    def test_speed(self):
        self.assertEqual(self.elev_1.speed, 1)
        self.assertEqual(self.elev_2.speed, 2.0)
        self.assertEqual(self.elev_3.speed, 7.0)
        self.assertEqual(self.elev_4.speed, 3)
        self.assertEqual(self.elev_5.speed, 9.0)


    def test_minFloor(self):
        self.assertNotEqual(self.elev_1.minFloor, 1)
        self.assertEqual(self.elev_2.minFloor, -2.0)
        self.assertEqual(self.elev_3.minFloor, -10)
        self.assertNotEqual(self.elev_4.minFloor, -1)
        self.assertEqual(self.elev_5.minFloor, -10)

    def test_maxFloor(self):
        self.assertEqual(self.elev_1.maxFloor, 10)
        self.assertEqual(self.elev_2.maxFloor, 10)
        self.assertEqual(self.elev_3.maxFloor, 100)
        self.assertEqual(self.elev_4.maxFloor, 100)
        self.assertEqual(self.elev_5.maxFloor, 100)

    def add_call(self):
        self.elev_1.add_call()
        self.assertNotEqual(self.elev_1.call.type, 1)

    def test_zero(self):
        self.elev_1.zero_data()
        self.assertEqual(self.elev_1.time, 0)
        self.assertEqual(self.elev_1.current, 0)
        self.assertEqual(self.elev_1.downList, [])

    def test_switch_down_list(self):
        self.elev_3.switch_down_list()
        self.assertEqual(self.elev_3.downList, [])

    def test_switch_up_list(self):
        self.elev_3.switch_up_list()
        self.assertEqual(self.elev_3.upList, [])

if __name__ == '__main__':
    unittest.main()