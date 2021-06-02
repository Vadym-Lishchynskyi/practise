from collections import Counter


def rewriting(a):
    gen_info = Counter(a).most_common()
    # print(gen_info)
    res = []
    for i in gen_info:
        if i[1] >= 3:
            for j in range(i[1]):
                res.append(i[0])
    return res


if __name__ == '__main__':
    array = [1, 2, 3, 4, 4, 4, 4, 2, 4, 56, 6, 1, 1, 2, 2, 2, 2, 4, 4, 7, 9, 0, 9, 0, 9, 9]
    print(rewriting(array))
