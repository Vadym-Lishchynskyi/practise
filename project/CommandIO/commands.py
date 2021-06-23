from project.DataIO import ListExhibitions
from project.DataIO.ListExhibitions import all_categories, all_exhibitions
from project.Instances.Exhibition_category_inst import Category
from project.Instances.Exhibition_inst import Exhibition

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

testing_data_objects = []


def create_testing_data():
    if not all_categories:
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
    for i in all_exhibitions:
        print(i.toJSON())


def get_from_file():
    pass
