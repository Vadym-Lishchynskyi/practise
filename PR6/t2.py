def change_local_max(array):
    res = []

    if array[0] > array[1]:
        res.append(0)
    else:
        res.append(array[0])

    for i in range(1, len(array)):
        if array[i - 1] < array[i] > array[i + 1]:
            res.append(0)
        else:
            res.append(array[i])

    return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 2, 3, 5, 6, 2, 4, 1]
    print(change_local_max(a))
