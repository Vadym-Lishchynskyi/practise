import math


def arctg1(x, e):
    res, n = 0, 0
    a = ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
    while abs(a) > e:
        res += a
        n += 1
        a = ((-1) ** n) * x ** (2 * n + 1) / (2 * n + 1)
        print(f'res: {res}')
        print(f'a: {a}')

    print()
    print(f'Custom function: {res}')
    print(f'With math module: {math.atan(x)}')


if __name__ == '__main__':
    arctg1(0.9, 0.00000001)
