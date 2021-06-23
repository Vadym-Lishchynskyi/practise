import json
from abc import ABC
from datetime import datetime

from project.DataIO import ListExhibitions
import uuid


class ExhibitionBase(ABC):
    """
    Abstract class of Exhibition instance
    """

    def __init__(self):
        self.__name = 'Unknown'
        self.__description = None
        self.__start_date = datetime.now()
        self.__category = []


class Exhibition(ExhibitionBase):
    """
    Class of Exhibition instance
    """

    def __init__(self, name, description, category, start_date):
        self.__name = name
        self.__description = description
        if not start_date:
            self.__start_date = datetime.now()
        else:
            self.__start_date = start_date
        if not category:
            self.__category = []
        else:
            self.__category = [category]
        # self.__uuid = uuid.uuid4()

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

    @property
    def start_date(self):
        return self.__start_date

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
    def description(self):
        return self.__description

    @start_date.getter
    def start_date(self):
        return self.__start_date

    # ~~~~~~~~~~~~~~~~~~~~~~ Other ~~~~~~~~~~~~~~~~~~~~~~
    def json_default(self):
        if isinstance(self.start_date, datetime):
            return dict(year=self.start_date.year, month=self.start_date.month, day=self.start_date.day)
        else:
            return self.__dict__

    def toJSON(self):
        return json.dumps(self, default=lambda o: self.json_default(),
                          sort_keys=True, indent=4)

    def __repr__(self):
        return f"Instance: Exhibition\n" + \
               f"Name: {self.name}\n" + \
               f"Category: {self.category[0].name}"
