# from project.CommandIO import commands


def list_commands(commands):
    for keys, values in commands.items():
        print(f'{values} - {keys}')

    print()


# ~~~~~~~~~~~~~~~~~ Decorator to get agreement for non rollback actions ~~~~~~~~~~~~~~~~~
def letter_for_agreement(message=None):
    def agreement(func):

        def wrapper(*args, **kwargs):
            while 1:
                if message:
                    print(message)
                agree = input('Are you sure? (yes / no): ')
                if agree == 'yes':
                    return func(*args, **kwargs)
                elif agree == 'no':
                    break
                else:
                    print('Unknown decision')

        return wrapper
    return agreement
