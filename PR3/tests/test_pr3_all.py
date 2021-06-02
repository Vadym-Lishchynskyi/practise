import pytest

from PR3.t1 import sum_to_n
from PR3.t2 import sum_of_a_range
from PR3.t3 import find_small_unpair


# =========================== TASK 1 ===========================
@pytest.mark.parametrize("a, result", [(5, 15),
                                       (1, 1),
                                       (10, 55)])
def test_mul_modules(a, result):
    assert sum_to_n(a) == result


# =========================== TASK 2 ===========================
@pytest.mark.parametrize("a, b, result", [(0, 10, 0),
                                          (1, 2, 1),
                                          (3, 2, 1.83),
                                          (3, 4, 1.8333)])
def test_sum_range(a, b, result):
    assert sum_of_a_range(a, b) == result


# =========================== TASK 3 ===========================
@pytest.mark.parametrize("a, b, result", [(7, [1, 2, -3, -4, 3, 6, -1], 2),
                                          (4, [-3, -1, 0, 3], 2),
                                          (1, [0], 0),
                                          (6, [-1, -1, -1, -1, -1, -1], 6)])
def test_sum_range(a, b, result):
    assert find_small_unpair(a, b) == result

