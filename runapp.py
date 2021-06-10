from project.CommandIO.commands import commands, create_testing_data, write_to_file
from project.ConsoleIO.display_commands import list_commands
from project.DataIO.ListExhibitions import all_categories, all_exhibitions

while True:
    for i in all_categories:
        print(i)
        print()

    for i in all_exhibitions:
        print(i)
        print()

    list_commands(commands)

    print()
    command = int(input())

    # ~~~~~~~~~~~~~~~~~ Command verification ~~~~~~~~~~~~~~~~~
    if command == 0:
        break
    if command == 1:
        create_testing_data()
    if command == 2:
        write_to_file()
    # if command == 4:
    #     add_exhibition()
    # if command == 5:
    #     add_category()

