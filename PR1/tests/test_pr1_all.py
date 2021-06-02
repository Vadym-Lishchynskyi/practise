import pytest

from PR1.t1 import mul_modules, dev_modules
from PR1.t2 import reversion
from PR1.t3 import rounder


# =========================== TASK 1 ===========================
@pytest.mark.parametrize("a, b, result", [(-2, 5, 10),
                                          (2, 5, 10),
                                          (-2, 0, 0),
                                          (-2, -5, 10)])
def test_mul_modules(a, b, result):
    assert mul_modules(a, b) == result


@pytest.mark.parametrize("a, b, result", [(5, 2, 2.5),
                                          (10, 2, 5),
                                          (10, -2, 5),
                                          ])
def test_dev_modules(a, b, result):
    assert dev_modules(a, b) == result


@pytest.mark.parametrize("a, b, result", [(2, 0, ZeroDivisionError),
                                          (-2, -0, ZeroDivisionError)
                                          ])
def test_dev_modules(a, b, result):
    with pytest.raises(result):
        dev_modules(a, b)


# =========================== TASK 2 ===========================
@pytest.mark.parametrize("a, result", [(0.1121111, 1111211.0),
                                       (2.12, 21.2),
                                       (-2.11, -11.2),
                                       (0, 0),
                                       (-3.24, -42.3)])
def test_rounder(a, result):
    assert reversion(a) == result


# =========================== TASK 3 ===========================
@pytest.mark.parametrize("a, result", [(0.1121111, 0.1121),
                                       (2.121212, 2.121212),
                                       (-2.111111111, -2.1),
                                       (0, 0)])
def test_rounder(a, result):
    assert rounder(a, 3) == result
