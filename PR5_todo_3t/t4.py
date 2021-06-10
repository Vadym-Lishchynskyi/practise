import math


def arctg1(x, e):
    res = 0

    n = 0
    a = ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
    while abs(a) > e:
        a = ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
        res += a
        n += 1
        print(res)
        print(f'a: {a}')

    print(res)
    print(math.atanh(x))


if __name__ == '__main__':
    arctg1(0.9, 0.000001)
