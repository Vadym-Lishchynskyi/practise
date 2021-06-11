def cals_displacement(v0, t, a):
    return v0 * t + a * t ** 2 / 2


if __name__ == '__main__':
    a = float(input("Enter v0: "))
    b = float(input("Enter t: "))
    c = float(input("Enter a: "))

    print(cals_displacement(a, b, c))
