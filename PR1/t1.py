def mul_modules(a: float, b: float) -> float:
    return abs(a) * abs(b)


def dev_modules(a: float, b: float) -> float:
    return abs(a) / abs(b)


if __name__ == '__main__':
    f_n = int(input('Enter a: '))
    s_n = int(input('Enter b: '))

    print(dev_modules(f_n, s_n))
