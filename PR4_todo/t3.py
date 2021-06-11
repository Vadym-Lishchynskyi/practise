import string

lead_letters = ['a', 'n', 'b', 'f', 'r', 't', 'v', 'N', '0']


def show_table():
    for i in range(32, 255, 16):
        for characters in range(i, i+16):
            print(f"{characters:2x} {chr(characters):<4}", end="")
        print()

    print()


def small_let_digits(a):
    res = ''
    for i in a:
        if i.isdigit() or (i.isalpha() and i.islower()):
           res += i
    return res


def except_lead(a, ll):
    res = ''
    for i in a:
        if i not in ll:
            res+=i

    return res


def small_letters_punc_spec(a):
    res = ''
    for i in a:
        if i in string.ascii_lowercase or i in string.punctuation:
            res += i

    return res


def lead_letters_spaces(a, ll):
    ll.append(' ')
    res = ''
    for i in a:
        if i in ll:
            res += f'{ord(i)} '

    return res


def digits_spaces(a):
    res = ''
    for i in a:
        if ord(i) in range(48, 59) or i == ' ':
            res += i

    return res


def digits_letters(a):
    res = ''
    for i in a:
        if i in string.ascii_letters or i in string.digits:
            res += i

    return res


def ever_except(a, ll):
    res = ''
    for i in a:
        if i not in string.punctuation and i not in ll and i != ' ':
            res += i

    return res


def digit_let_space(a):
    res = ''
    for i in a:
        if i in string.punctuation or i in string.digits or i == ' ':
            res += i

    return res


def small_punc(a):
    res = ''
    for i in a:
        if i in string.punctuation or i in string.ascii_lowercase:
            res += i

    return res


if __name__ == '__main__':
    print('ASCII Table'.center(110, '~'), end='\n\n')
    show_table()

    s = input("Enter your string: ")

    print(small_let_digits(s))
    print(except_lead(s, lead_letters))
    print(small_letters_punc_spec(s))
    print(lead_letters_spaces(s, lead_letters))
    print(digits_spaces(s))
    print(digits_letters(s))
    print(ever_except(s, lead_letters))
    print(digit_let_space(s))
    print(small_punc(s))
