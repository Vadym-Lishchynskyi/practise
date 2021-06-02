def find_small_unpair(n: int, l: list) -> int:
    return len(list(filter(lambda x: (x < 0 and x % 2 == 1), l)))


if __name__ == '__main__':
    a = [1, 2, -3, -4, 3, 6, -1]
    print(find_small_unpair(0, a))
