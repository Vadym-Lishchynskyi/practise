def even(k: int) -> bool:
    return True if k % 2 == 0 else False


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in a:
        print(even(i))
