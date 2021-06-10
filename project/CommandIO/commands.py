from project.DataIO import ListExhibitions
from project.DataIO.ListExhibitions import all_categories
from project.Instances.Exhibition_category_inst import Category
from project.Instances.Exhibition_inst import Exhibition

from xml_marshaller import xml_marshaller

commands = {'Вийти': 0,
            'Створити тестові дані': 1,
            'Зберигти дані': 2,
            'Завантажити дані': 3,
            'Додати запис про виставку': 4,
            'Додати запис про категорію': 5,
            'Редагувати записи': 6
            }


def create_testing_data():
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


def add_exhibition():
    # TODO add module Entering
    # print("name: ")
    pass


def write_to_file():
    strXmlPerson = xml_marshaller.loads(all_categories)
    # print(strXmlPerson)
    with open('file.xml', "w") as f:
        f.write(strXmlPerson)
