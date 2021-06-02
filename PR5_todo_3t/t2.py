def add_left_digit(d: int):
    global k

    k = int(str(d) + str(k))


if __name__ == '__main__':
    k = int(input("Enter k: "))

    d1 = int(input('Enter D1: '))
    d2 = int(input('Enter D2: '))

    add_left_digit(d1)
    print(k)
    add_left_digit(d2)
    print(k)
