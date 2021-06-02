def amount_of_zeros(k, n, l):
    res = []

    for i in l:
        res.append(i.count(0))

    return res


if __name__ == '__main__':
    arr = [[1, 2, 3, 0, 4, 5, 2, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 2, 3, 0, 1, 2, 0]]
    print(amount_of_zeros(1, 1, arr))
