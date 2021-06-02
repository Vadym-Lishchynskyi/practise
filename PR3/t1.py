def sum_to_n(a: int) -> int:
    res = 0
    for i in range(a+1):
        res += i
    return res


if __name__ == '__main__':
    n = int(input('Enter number: '))
    print(sum_to_n(n))
