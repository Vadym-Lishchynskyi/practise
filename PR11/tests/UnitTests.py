import pytest

from PR11.t1 import cals_displacement


def numbers_comparing(r1, r2, e=0.000000000000001):
    """
    Custom almost equal comparison function
    """
    difference = abs(r1) * e
    return abs(r1-r2) <= difference


@pytest.mark.parametrize("a, b, c, result", [(2, 5, 10, 135),
                                             (2, 5.14, 10, 142.3),
                                             (2, 0, 0, 0),
                                             (2, 15, 10, 1155)])
def test_mul_modules(a, b, c, result):
    assert cals_displacement(a, b, c) == pytest.approx(result, 0.01)
