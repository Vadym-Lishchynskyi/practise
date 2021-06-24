from project.CommandIO.commands import commands, create_testing_data, write_to_file, \
    delete_all, add_exhibition, create_new_category, create_new_exhibition
from project.ConsoleIO.display_commands import list_commands
from project.DataIO.ListExhibitions import all_categories, all_exhibitions

from prettytable import PrettyTable

from project.DataIO.SaveToFile import write_new_exhib_to_txt


def create_table():
    table_exhibitions = PrettyTable()
    table_categories = PrettyTable()
    table_exhibitions.field_names = ["№", "Name", "Category", "Start date", "Description"]
    table_categories.field_names = ["№", "Name", "Description"]

    return table_categories, table_exhibitions


while True:
    table_categories, table_exhibitions = create_table()

    for i in range(len(all_categories)):
        table_categories.add_row([i+1, all_categories[i].name, all_categories[i].description])

    for i in range(len(all_exhibitions)):
        table_exhibitions.add_row([i+1, all_exhibitions[i].name, all_exhibitions[i].category[0], all_exhibitions[i].start_date, all_exhibitions[i].description])

    if all_categories:
        print(table_categories)

    if all_exhibitions:
        print(table_exhibitions)

    list_commands(commands)

    print()
    command = int(input())

    # ~~~~~~~~~~~~~~~~~ Command verification ~~~~~~~~~~~~~~~~~
    if command == 0:
        break
    if command == 1:
        create_testing_data()
    if command == 2:
        delete_all()
    if command == 3:
        write_to_file()
    # if command == 4:
    #      add_category()
    if command == 5:
        create_new_exhibition()
    if command == 6:
        create_new_category()

