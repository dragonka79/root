import math
import unittest


def calcCircumference(r):
    return r * 2 * math.pi


class TestCode(unittest.TestCase):
    def test_circumfrence(self):
        self.assertAlmostEqual(calcCircumference(1), 6.28318530)


unittest.main()
