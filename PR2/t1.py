def find_higher(a: float, b: float, c: float) -> float:
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c


if __name__ == '__main__':
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))

    print(find_higher(a, b, c))
