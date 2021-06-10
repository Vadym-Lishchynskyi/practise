from abc import ABC
from datetime import datetime

from project.DataIO import ListExhibitions


# class ExhibitionBase(ABC):
#     """
#     Abstract class of Exhibition instance
#     """
#
#     def __init__(self):
#         self.__name = 'Unknown'
#         self.__description = None
#         self.__start_date = datetime.now()
#         self.__category = []


class Exhibition:
    """
    Class of Exhibition instance
    """

    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__start_date = datetime.now()
        if not category:
            self.__category = []
        else:
            self.__category = [category]

    # ~~~~~~~~~~~~~~~~~~~~~~ Attribute installation ~~~~~~~~~~~~~~~~~~~~~~
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @name.setter
    def name(self, new_name):
        if len(new_name) > 50:
            print('Name is too long')
        else:
            self.__name = new_name

    @name.getter
    def name(self):
        return self.__name

    @category.setter
    def category(self, new_category):
        if new_category in ListExhibitions.all_categories:
            self.__category.append(new_category)

    @category.getter
    def category(self):
        return self.__category

    @description.setter
    def description(self, new_description):
        if len(new_description) > 500:
            print('Name is too long')
        else:
            self.__name = new_description

    @description.getter
    def name(self):
        return self.__description

    # ~~~~~~~~~~~~~~~~~~~~~~ Other ~~~~~~~~~~~~~~~~~~~~~~

    def __repr__(self):
        return f"Instance: Exhibition\n" + \
               f"Name: {self.name}\n" + \
               f"Category: {self.category[0].name}"




