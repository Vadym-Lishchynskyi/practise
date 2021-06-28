from datetime import datetime

from project.config import dateFormatter


def enter_string(string, max_len=250):
    desc = input(string + ': ')
    while len(desc) > max_len:
        print('Wrong description! (max length 250)')
        desc = input(string + ': ')
    return desc


def enter_number(string, typ=int, var=None):
    num = input(string + ': ')
    if var:
        while int(num) not in range(1, var+1):
            print('No such category')
            num = input(string + ': ')
        return int(num)
    else:
        num = float(num)
    return num


def enter_date(string):
    f = 1
    while f:
        start_date = input(string + ': ')
        try:
            if start_date == '':
                start_date = None
                break
            datetime.strptime(start_date, dateFormatter)
            f = 0
        except Exception as e:
            f = 1
            print(e, end='\n')
            print('Something went wrong. Try again')

    return start_date