import unittest
from call import Call



class testCall_test(unittest.TestCase):

    call_1 = Call(0.437472729, 0, -1)
    call_2 = Call(2.20940563015935, 0, -1)
    call_3 = Call(18.7729931796688, -1, -2)
    call_4 = Call(19.5908696496569, 0, 7)
    call_5 = Call(29.5794335668149, 0, 7)


    def test_time(self):
        self.assertEqual(self.call_1.time, 0.437472729)
        self.assertEqual(self.call_2.time, 2.20940563015935)
        self.assertEqual(self.call_3.time, 18.7729931796688)
        self.assertEqual(self.call_4.time, 19.5908696496569)
        self.assertEqual(self.call_5.time, 29.5794335668149)

    def test_src(self):
        self.assertEqual(self.call_1.src, 0)
        self.assertEqual(self.call_2.src, 0)
        self.assertEqual(self.call_3.src, -1)
        self.assertEqual(self.call_4.src, 0)
        self.assertEqual(self.call_5.src, 0)

    def test_dest(self):
        self.assertEqual(self.call_1.dest, -1)
        self.assertEqual(self.call_2.dest, -1)
        self.assertEqual(self.call_3.dest, -2)
        self.assertEqual(self.call_4.dest, 7)
        self.assertEqual(self.call_5.dest, 7)

if __name__ == '__main__':
    unittest.main()