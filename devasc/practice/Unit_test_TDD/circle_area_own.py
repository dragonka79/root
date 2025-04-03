from math import pi
from unitteszt import teszt


def area_of_circle(r):
    if r < 0:
        # raise ValueError('Negative radius value error')
        return ('Negative radius value error')
    return (pi * (r ** 2))


c = (10 ** -5)


def test_module():
    """ Test module for function area_of_circle """
    teszt(abs(area_of_circle(0) - 0) < c)
    teszt(abs(area_of_circle(1) - 3.141592653589793) < c)
    teszt(abs(area_of_circle(pi) - 31.006278) < c)
    teszt(area_of_circle(-2) == 'Negative radius value error')


test_module()
# print(area_of_circle(pi))
