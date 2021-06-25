import os.path
import sys
from datetime import datetime

from project.config import dateFormatter, path_to_test_data

from project.DataIO import ListExhibitions
from project.DataIO.ListExhibitions import all_categories, all_exhibitions
from project.Instances.Exhibition_category_inst import Category
from project.Instances.Exhibition_inst import Exhibition
from project.DataIO.SaveToFile import write_all_to_txt, get_data_from_txt, write_new_cat_to_txt

from xml_marshaller import xml_marshaller
import json

commands = {'Вийти': 0,
            'Створити тестові дані': 1,
            'Видалити всі дані': 2,
            'Зберигти дані': 3,
            'Завантажити дані': 4,
            'Додати запис про виставку': 5,
            'Додати запис про категорію': 6,
            'Редагувати записи': 7
            }

commands_exhibition = {
    'Повернутись в головне меню': 0,
    'Видалити виставку': 1,
    'Видалити усі виставки': 2,
    'Сортувати за назвою': 3,
    'Сортувати за датою': 4,
    'Сортувати за категоріями': 5,
    'Фільтрувати за назвою': 6,
    'Фільтрувати за категорією': 7,
    'Фільтрувати за датою': 8,
}

commands_categories = {
    'Повернутись в головне меню': 0,
    'Видалити категорію': 1,
    'Видалити усі категорії': 2,
    'Сортувати за назвою': 3,
    'Фільтрувати за назвою': 4,
}

commands_txt = {

}

commands_xml = {

}

testing_data_objects = []


def create_testing_data():
    # path_to_test_data = 'Data/test_data.txt'
    # print(sys.argv[0])
    # path_to_test_data = os.path.join(os.getcwd(), 'project', 'Data', 'test_data.txt')
    # print(path_to_test_data)
    # print(os.listdir(path_to_test_data))

    try:
        print(path_to_test_data)
        get_data_from_txt(path_to_test_data)
    except (IOError, FileNotFoundError) as e:
        print(u'не удалось открыть файл')
        new_cat = Category("Виставка картин", "Примутні переважно ватвори мистецтва")
        ListExhibitions.new_category(new_cat)
        new_cat = Category("Технічна виставка", "Виставка приладів та прогрма")
        ListExhibitions.new_category(new_cat)
        new_cat = Category("Виставка автомобілів", "Виставка любих автомобілів - від тракторів до спорткарів")
        ListExhibitions.new_category(new_cat)
        new_exhib = Exhibition("Серпнева виставка", "Найбільша в світі цього року", all_categories[0])
        ListExhibitions.new_exhibition(new_exhib)
        new_exhib = Exhibition("Tech Expo", "Виставка компютерів та разнихї технічних пристроїв", all_categories[1])
        ListExhibitions.new_exhibition(new_exhib)
        new_exhib = Exhibition("Teh mobile", "Автомобільний концерн Ford", all_categories[2])
        ListExhibitions.new_exhibition(new_exhib)
    # else:
    #     with file:
    #         print(u'делаем что-то с файлом')
    #         get_data_from_txt(path_to_test_data)


def delete_testing_data():
    if testing_data_objects:
        for i in testing_data_objects:
            if i in all_categories:
                del all_categories[all_categories.index(i)]
            if i in all_exhibitions:
                del all_exhibitions[all_exhibitions.index(i)]


def delete_all():
    all_exhibitions.clear()
    all_categories.clear()


def add_exhibition():
    if not all_categories:
        print("Add category first")
    else:
        name = input("Enter exhibition name: ")
        description = input("Enter description: ")
        for i in range(len(all_categories)):
            print(f'{i+1}- {all_categories[i]}')
        category_name = input("Choose category(enter 1 to n): ")


def write_to_file():
    # strXmlPerson = xml_marshaller.loads(all_categories)
    # # print(strXmlPerson)
    # with open('file.xml', "w") as f:
    #     f.write(strXmlPerson)
    # for i in all_exhibitions:
    #     print(i.toJSON())
    write_all_to_txt()


def get_from_file():
    pass


def create_new_category():
    name = input('Enter name: ')
    description = input('Enter description: ')

    new_cat = Category(name, description)
    ListExhibitions.new_category(new_cat)

    write_new_cat_to_txt(new_cat)


def create_new_exhibition():
    name = input('Enter name: ')
    for num, i in enumerate(all_categories, 1):
        print(f'\t{num} - {i.name}')

    if not all_categories:
        print('Enter category first')
        return

    category_num = int(input('Choose category (number): '))
    if category_num > len(all_categories):
        print('No such category')

    # category = all_categories[category_num - 1]

    start_date = input('Enter start_date (2021-06-24-08:13 or Enter): ')
    f = 1
    while f:
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


    description = input('Enter description: ')

    new_exhib = Exhibition(name, description, all_categories[category_num-1])
    ListExhibitions.new_exhibition(new_exhib)

    write_new_cat_to_txt(new_exhib)


