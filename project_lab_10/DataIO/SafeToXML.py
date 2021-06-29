import os
import platform
import xml.etree.ElementTree as xml

from project.DataIO.ListExhibitions import all_categories, all_exhibitions


def createXML_category(filename):
    """
    Создаем XML файл.
    """

    a_categories = xml.Element("a_categories")
    for i in range(len(all_categories)):
        category = xml.Element(f"category")
        a_categories.append(category)

        num = xml.SubElement(category, "num")
        num.text = str(i)

        name = xml.SubElement(category, "name")
        name.text = all_categories[i].name

        description = xml.SubElement(category, "description")
        description.text = all_categories[i].description

    tree = xml.ElementTree(a_categories)
    with open(filename, "wb") as fh:
        tree.write(fh)


def createXML_exhibitions(filename):
    """
    Создаем XML файл.
    """

    a_exhibitions = xml.Element("a_exhibitions")
    for i in range(len(all_exhibitions)):
        exhibition = xml.Element(f"exhibition")
        a_exhibitions.append(exhibition)

        # создаем дочерний суб-элемент.
        name = xml.SubElement(exhibition, "name")
        name.text = all_exhibitions[i].name

        category = xml.SubElement(exhibition, "category")
        category.text = str(all_categories.index(all_exhibitions[i].category[0]))

        start_date = xml.SubElement(exhibition, "start_date")
        start_date.text = all_exhibitions[i].start_date

        description = xml.SubElement(exhibition, "description")
        description.text = all_exhibitions[i].description

    tree = xml.ElementTree(a_exhibitions)
    with open(filename, "wb") as fh:
        tree.write(fh)



if __name__ == "__main__":
    createXML_category("categories_data.xml")