lat_small_letters = [97, 123]
lat_large_letters = [65, 91]
numbers = [48, 58]
cirilic_small = [1072, 1104]
cirilic_large = [1040, 1072]


def find_symbols(start=0, stop=1, step=1):
    return [chr(i) for i in range(start, stop, step)]


def find_all_letters(l1, l2):
    res = []
    for i in range(len(l1)):
        res.extend((l1[i], l2[i]))

    return res


print(find_symbols(*lat_small_letters))
print(find_symbols(*lat_large_letters))
print(find_symbols(*numbers))
print(find_symbols(*cirilic_small))
print(find_symbols(*cirilic_large))
print(find_all_letters(find_symbols(*lat_large_letters), find_symbols(*lat_small_letters)))
