def sum_of_a_range(n: int, a: int) -> float:
    res = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(1, n+1):
        res += 1/i

    return round(res, a)


if __name__ == '__main__':
    a = 4
    n = int(input("Enter n: "))
    print(sum_of_a_range(a, n))
