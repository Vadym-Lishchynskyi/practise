from abc import ABC


# class CategoryBase(ABC):
#     """
#     Abstract class of Exhibition instance
#     """
#
#
#

class Category:
    """
    Class of ExhibitionCategory instance
    """

    def __init__(self, name, description):
        if name:
            self.__name = name
        else:
            self.__name = 'Unknown'

        if description:
            self.__description = description
        else:
            self.__description = 'Unknown'

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @name.setter
    def name(self, new_name):
        if len(new_name) > 50:
            print('Name is too long')
        else:
            self.__name = new_name

    @name.getter
    def name(self):
        return self.__name

    @description.setter
    def description(self, new_description):
        if len(new_description) > 500:
            print('Name is too long')
        else:
            self.__name = new_description

    @description.getter
    def description(self):
        return self.__description

    def __repr__(self):
        return f"Instance: Category\n" + \
               f"Name: {self.name}"
               # f"Category: {self.category}"