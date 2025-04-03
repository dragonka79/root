import unittest
from math import pi


def area_of_circle(r):
    if r < 0:
        raise ValueError('Negative radius value error')
    return pi*(r**2)


class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        # Test radius >=0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area_of_circle, -1)

    def test_invalid_input(self):
        self.assertRaises(area_of_circle("Zolcs"))

    def myfunc(self):
        return "Hello"


unittest.main()
