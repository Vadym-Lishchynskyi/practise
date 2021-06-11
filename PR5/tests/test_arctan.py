import pytest

from PR5_todo_3t.t4 import arctg1


# =========================== TASK 1 ===========================
@pytest.mark.parametrize("x, e, result", [(-2, 5, 10),
                                          (2, 5, 10),
                                          (-2, 0, 0),
                                          (-2, -5, 10)])
def test_mul_modules(x, e, result):
    assert arctg1(x, e) == result


