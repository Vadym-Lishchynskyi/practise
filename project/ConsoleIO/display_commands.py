from project.CommandIO import commands


def list_commands(commands):
    for keys, values in commands.items():
        print(f'{values} - {keys}')


# def list_data(arr):
#     for i in arr:
#         print(i)
