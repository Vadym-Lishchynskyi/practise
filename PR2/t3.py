def explore_eq_dev(a: float, b: float) -> bool:
    return True if ((a % 2 == 0 and b % 2 == 0) or
                    (a % 2 == 1 and b % 2 == 1)) else False


print(explore_eq_dev(12, 14))