from project.DataIO import ListExhibitions
from project.DataIO.ListExhibitions import all_categories, all_exhibitions
from project.Instances.Exhibition_category_inst import Category
from project.Instances.Exhibition_inst import Exhibition


def get_data_from_txt(path):
    res = []
    with open(path, 'r') as file:
        result = file.readlines()
        # for i in file.readlines():
        #     res.append(i)
        #     # print(i)
        for i in range(1, len(result), 3):
            if result[i] == '\n':
                name = result[i + 1].split('\tName: ')[-1][:-1]
                category = result[i + 2].split('\tDescrCategoryiption: ')[-1][:-1]
                start_date = result[i + 3].split('\tStart date:: ')[-1][:-1]
                description = result[i + 4].split('\tDescription: ')[-1][:-1]

                new_exhib = Exhibition(name, description, all_categories[2])
                ListExhibitions.new_exhibition(new_exhib)

            else:
                name = result[i+1].split('\tName: ')[-1][:-1]
                description = result[i+2].split('\tDescription: ')[-1][:-1]

                new_cat = Category(name, description)
                print(new_cat)
                ListExhibitions.new_category(new_cat)



        # print(res)


def write_all_to_txt():
    with open('data.txt', 'w') as file:
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
                            '\tStart date: ' + str(i.start_date.strftime('%Y-%m-%d-%H:%M')) + '\n'
                            '\tDescription: ' + i.description + '\n')


def write_new_to_txt():
    with open('data.txt', 'a') as file:
        pass


def get_from_txt():
    pass

