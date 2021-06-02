def middle_arifm(a, start, stop):
    n = stop - start + 1
    res = sum(a[start:stop+1])/n
    return round(res,2)


if __name__ == '__main__':
    start = 3
    stop = 9

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 32, 56, 2, 8, 2, 1, 1, 3]

    print(middle_arifm(array, start, stop))
