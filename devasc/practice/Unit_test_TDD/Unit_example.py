import math
import unittest


def calcCircumfrence(r):
    return r * 2 * math.pi


class TestCode(unittest.TestCase):
    def test_circumfrence(self):
        self.assertAlmostEqual(calcCircumfrence(1), 6.28318530)


unittest.main()
