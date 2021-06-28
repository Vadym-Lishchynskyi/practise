from datetime import datetime

from project.config import dateFormatter


def enter_string(string, max_len=250):
    var = input(string + ': ')
    while len(var) > max_len:
        print('Wrong description! (max length 250)')
        var = input(string + ': ')
    return var


def enter_number(string, typ=int, var=None, err='Wrong number\n'):

    res = 1
    while res:
        try:
            num = int(input(string + ': '))
        except ValueError:
            print(err)
            continue

        if var:
            while int(num) not in range(0, var):
                print(err)
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
                start_date = datetime.now().strftime(dateFormatter)
                break
            datetime.strptime(start_date, dateFormatter)
            f = 0
        except Exception as e:
            f = 1
            print(e, end='\n')
            print('Something went wrong. Try again')

    return start_date