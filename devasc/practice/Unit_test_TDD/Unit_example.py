from math import pi
import unittest


def calcCircumference(r):
    return r * 2 * pi


class TestCode(unittest.TestCase):
    def test_circumfrence(self):
        self.assertAlmostEqual(calcCircumference(1), 6.28318530)

    def test_circumferenceInvalid(self):
        self.assertRaises(calcCircumference('pí'))


unittest.main()
