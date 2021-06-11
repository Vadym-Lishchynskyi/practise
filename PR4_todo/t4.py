import string

input_string = input("Enter string: ")


def except_letters(a):
    res = ''
    for i in a:
        if i.isalpha():
            pass
        else:
            res += i
    return res


def except_punctuation(a):
    res = ''
    for i in a:
        if i in string.punctuation:
            pass
        else:
            res += i
    return res


def digits_witespaces(a):
    res = ''
    for i in a:
        if i in string.digits or i == ' ':
            res += i
        else:
            pass
    return res


def with_white_spaces(a):
    a = list(a)
    a = [i for i in a if i != ' ']
    a = ' '.join(a)
    return a


def digit_to_space(a):
    res = ''
    for i in a:
        if i.isdigit():
            res += ' '
        else:
            res += i

    return res


def small_letters(a):
    res = ''
    for i in a:
        if i in string.ascii_lowercase:
            res += i

    return res


def digit_codes(a, tp):
    res = ''
    for i in a:
        if i.isdigit():
            if tp == 10:
                res += f'{ord(i)} '
            elif tp == 16:
                res += f'{hex(ord(i))} '

    return res


print(except_letters(input_string))
print(except_punctuation(input_string))
print(digits_witespaces(input_string))
print(with_white_spaces(input_string))
print(with_white_spaces(digits_witespaces(input_string)))
print(digit_to_space(input_string))
print(small_letters(input_string))
print(small_letters(input_string))
print(digit_codes(input_string, 10))
print(digit_codes(input_string, 16))
