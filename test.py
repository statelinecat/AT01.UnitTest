import unittest
from main import *


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_rem_div(self):
        self.assertEqual(rem_div(9, 7), 2)

    def test_rem_div_by_zero(self):
        self.assertRaises(ValueError, rem_div, 9, 0)
        self.assertRaises(TypeError, rem_div, 9, 0)





if __name__ == '__main__':
    unittest.main()