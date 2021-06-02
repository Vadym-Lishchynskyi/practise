def rounder(a: float, ver: int) -> float:
    a = str(a)
    verifier = 0
    for i in a[::-1]:
        if i == '1':
            verifier += 1
        else:
            break

    if verifier >= ver:
        a = a[:-verifier + 1]

    return float(a)


if __name__ == '__main__':
    em_to_verify = 3

    number = float(input('Enter number to round: '))
    print(rounder(number, em_to_verify))
