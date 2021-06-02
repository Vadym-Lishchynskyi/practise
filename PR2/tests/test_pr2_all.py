import pytest

from PR2.t1 import find_higher
from PR2.t3 import explore_eq_dev


# =========================== TASK 1 ===========================
@pytest.mark.parametrize("a, b, c, result", [(1, 2, 3, 1),
                                             (2, 3, 1, 1),
                                             (2, 2, 3, 2),
                                             (0, 0, 0, 0)])
def test_mul_modules(a, b, c, result):
    assert find_higher(a, b, c) == result


# =========================== TASK 3 ===========================
@pytest.mark.parametrize("a, b, result", [(10, 20, True),
                                          (21, 30, False),
                                          (21, 27, True),
                                          (0, 0, True)])
def test_mul_modules(a, b, result):
    assert explore_eq_dev(a, b) == result

