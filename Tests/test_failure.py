
import math


def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) != 4


def test_square_failure():
    num = 7
    assert num*num == 49


def test_equality_failure():
    assert 10 != 11
