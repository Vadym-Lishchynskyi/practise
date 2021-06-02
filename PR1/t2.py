def reversion(a: float) -> float:

    def gen(a):
        if a % 1 != 0:
            a = str(a).split('.')
            return a[1][::-1] + '.' + a[0][::-1]
        else:
            return str(int(a))[::-1]

    if a > 0:
        a = gen(a)
        return float(a)
    else:
        a = str(a)[1:]
        return float('-' + gen(a))


if __name__ == '__main__':
    number_to_reverse = float(input("Enter number to reverse: "))
    print(reversion(number_to_reverse))
