from project.DataIO import ListExhibitions
from project.DataIO.ListExhibitions import all_categories, all_exhibitions
from project.Instances.Exhibition_category_inst import Category
from project.Instances.Exhibition_inst import Exhibition
from project.config import dateFormatter

general_category_counter = 0
general_exhibition_counter = 0


def get_data_from_txt(path):
    res = []
    with open(path, 'r') as file:
        result = file.readlines()
        # for i in file.readlines():
        #     res.append(i)
        #     # print(i)
        for i in range(1, len(result), 3):
            if result[i] == '\n':
                break
            else:
                name = result[i+1].split('\tName: ')[-1][:-1]
                description = result[i+2].split('\tDescription: ')[-1][:-1]

                new_cat = Category(name, description)
                # print(new_cat)
                ListExhibitions.new_category(new_cat)

        for i in range(13, len(result), 5):

            name = result[i].split('\tName: ')[-1][:-1]
            category = result[i + 1].split('\tCategory: ')[-1][:-1]
            start_date = result[i + 2].split('\tStart date: ')[-1][:-1]
            description = result[i + 3].split('\tDescription: ')[-1][:-1]

            new_exhib = Exhibition(name, description, category, start_date)
            ListExhibitions.new_exhibition(new_exhib)


        # print(res)


def write_all_to_txt():
    with open('test_data.txt', 'w') as file:
        file.writelines('Категорії виставок\n')
        for num, i in enumerate(all_categories):
            file.writelines(f'№: {num}\n')
            file.writelines('\tName: ' + i.name + '\n' +
                            '\tDescription: ' + i.description + '\n')

        file.writelines('\nВиставки\n')
        for num, i in enumerate(all_exhibitions):
            file.writelines(f'№: {num}\n')
            file.writelines('\tName: ' + i.name + '\n' +
                            '\tCategory: ' + i.category[0].name + '\n'
                            '\tStart date: ' + str(i.start_date.strftime(dateFormatter)) + '\n'
                            '\tDescription: ' + i.description + '\n')


def write_new_cat_to_txt(obj):
    with open('data_categories.txt', 'a') as file:
        file.writelines(f'№: {len(all_categories) - 1}\n')
        file.writelines('\tName: ' + obj.name + '\n' +
                        '\tDescription: ' + obj.description + '\n')


def write_new_exhib_to_txt(obj):
    with open('data_exhibitions.txt', 'a') as file:
        file.writelines(f'№: {len(all_categories) - 1}\n')
        file.writelines('\tName: ' + obj.name + '\n' +
                        '\tCategory: ' + obj.category[0].name + '\n'
                        '\tStart date: ' + str(obj.start_date.strftime(dateFormatter)) + '\n' +
                        '\tDescription: ' + obj.description + '\n')


def get_from_txt():
    pass

