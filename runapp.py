import os

from project.CommandIO.commands import commands_main, create_testing_data, write_to_file, \
    delete_all, add_exhibition, create_new_category, create_new_exhibition, commands_exhibition, commands_files, \
    commands_categories, delete_element, delete_category, edit_category, edit_exhibition, delete_exhibitions
from project.Common.Entering import enter_number
from project.ConsoleIO.display_commands import list_commands, letter_for_agreement
from project.DataIO.ListExhibitions import all_categories, all_exhibitions

from prettytable import PrettyTable

from project.DataIO.SaveToFile import write_new_exhib_to_txt
from project.config import error_message_for_commands


def create_table(to_show='all'):
    """
    Creation of main tables with data
    """

    table_exhibitions = PrettyTable()
    table_categories = PrettyTable()
    table_exhibitions.field_names = ["№", "Name", "Category", "Start date", "Description"]
    table_categories.field_names = ["№", "Name", "Description"]

    # return table_categories, table_exhibitions

    for i in range(len(all_categories)):
        table_categories.add_row([i, all_categories[i].name, all_categories[i].description])

    for i in range(len(all_exhibitions)):
        table_exhibitions.add_row([i, all_exhibitions[i].name, all_exhibitions[i].category[0], all_exhibitions[i].start_date, all_exhibitions[i].description])

    if all_categories and (to_show == 'categories' or to_show == 'all'):
        print(table_categories)

    if all_exhibitions and (to_show == 'exhibitions'or to_show == 'all'):
        print(table_exhibitions)

    print()


while True:
    """
    Main program circle
    """
    # ~~~~~~~~~~~~~~~~~ Clearing console ~~~~~~~~~~~~~~~~~
    os.system('CLS||clear')

    # ~~~~~~~~~~~~~~~~~ Creating tables with data ~~~~~~~~~~~~~~~~~
    create_table()

    # ~~~~~~~~~~~~~~~~~ Listing main commands ~~~~~~~~~~~~~~~~~
    list_commands(commands_main)

    command = enter_number('Enter_command', var=len(commands_main), err=error_message_for_commands)

    # ~~~~~~~~~~~~~~~~~ Command verification ~~~~~~~~~~~~~~~~~
    if command == 0:
        break

    if command == 1:
        create_testing_data()

    if command == 2:

        delete_all()

        # while 1:
        #     agreement = input('Are you sure? (yes / no): ')
        #     if agreement == 'yes':
        #         delete_all()
        #         break
        #     elif agreement == 'no':
        #         break
        #     else:
        #         print('Unknown decision')

    if command == 3:
        os.system('CLS||clear')

        create_table()

        list_commands(commands_files)
        s_command = enter_number('Enter_command', var=len(commands_main), err=error_message_for_commands)

    if command == 4:
        os.system('CLS||clear')

        create_table('categories')

        list_commands(commands_categories)
        s_command = enter_number('Enter_command', var=len(commands_categories), err=error_message_for_commands)

        if s_command == 0:
            continue

        if s_command == 1:
            create_new_category()

        if s_command == 2:
            cat_num = enter_number('Enter category number', var=len(all_categories))
            delete_category(cat_num)

        if s_command == 3:
            delete_all()

        if s_command == 4:
            cat_num = enter_number('Enter category number', var=len(all_categories))
            edit_category(cat_num)

        if s_command == 5:
            delete_all()

    if command == 5:
        os.system('CLS||clear')

        create_table('exhibitions')

        list_commands(commands_exhibition)
        s_command = enter_number('Enter_command', var=len(commands_exhibition), err=error_message_for_commands)

        if s_command == 0:
            continue

        if s_command == 1:
            create_new_exhibition()

        if s_command == 2:
            cat_num = enter_number('Enter exhibition number', var=len(all_exhibitions))
            delete_element(cat_num, all_exhibitions)

        if s_command == 3:
            delete_exhibitions()

        if s_command == 4:
            ex_num = enter_number('Enter exhibition number', var=len(all_exhibitions))
            edit_exhibition(ex_num)


    # if command == 3:
    #     write_to_file()
    # if command == 4:
    #     add_category()
    # if command == 5:
    #     create_new_exhibition()
    # if command == 6:
    #     create_new_category()


