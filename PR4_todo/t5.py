ukrainian_alphabet = [i for i in range(1040, 1103)
                      if i not in [1066, 1067, 1098, 1099]]
ukrainian_alphabet.extend([1030, 1031, 1110, 1111])


def all_ukrainian_letters(string, alpha):
    res = ''
    for i in string:
        if ord(i) in alpha:
            res += i
        else:
            pass
    return res


if __name__ == '__main__':
    s = input("Enter string: ")

    print(all_ukrainian_letters(s, ukrainian_alphabet))
