# Задача 1
from pprint import pprint

cook_book = {}
with open('files/recipes.txt', "r", encoding='utf-8') as file:
    for string in file:
        ingradient = file.readline()
        menu_list = []
        for i in range(int(ingradient)):
            x = file.readline().rstrip('\n').split(" | ")
            consistent = {
                'ingridient_name': x[0],
                'quantity': int(x[1]),
                'measure': x[2]
            }
            menu_list.append(consistent)
        file.readline()
        cook_book[
            string.strip()] = menu_list
    print('cook_book = ')
    pprint(cook_book, sort_dicts=None)

# Задача 2
print('Задача 2')

def get_shop_list_by_dishes(dishes, person_count):
    zakaz = []
    final = {}
    # ing_var = {}
    for i in dishes:
        zakaz += cook_book[i]
    for i in zakaz:
        j = 1
        if i['ingridient_name'] not in final.keys():
            final.update({
                i['ingridient_name']: {
                    'measure': i['measure'],
                    'quantity': i['quantity'] * person_count
                }
            })
        else:
            j += 1
            ing_var = {i['ingridient_name']: j}
            # print(ing_var,'')
            final.update({
                i['ingridient_name']: {
                    'measure': i['measure'],
                    'quantity': (i['quantity'] * j) * person_count
                }
            })
    return pprint(final)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Задача 3
print('Задача 3')

from pprint import pprint
import os

path_dir = "C:/Education/PycharmProjects/OOP2/files/"
file_in_dir = os.listdir(path_dir)

file_list = []

for file_i in file_in_dir:
    file_full_path = path_dir + file_i
    with open(file_full_path, 'rt', encoding = 'utf-8') as file:
        file_list.append(file.readlines())
i = 0
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, file_in_dir[i])
    i += 1
sorted_file = file_list.sort(key=lambda x:len(x))
with open ('/Education/PycharmProjects/OOP2/results/result.txt', 'w', encoding = 'utf-8') as file_all:
        file_all.write(file_list[0][0] + '\n' + str(file_list[0][1]) + '\n' + ''.join(file_list[0][2:]) + '\n')
        file_all.write(file_list[1][0] + '\n' + str(file_list[1][1]) + '\n' + ''.join(file_list[1][2:]) + '\n')
        file_all.write(file_list[2][0] + '\n' + str(file_list[2][1]) + '\n' + ''.join(file_list[2][2:]) + '\n')
with open('/Education/PycharmProjects/OOP2/results/result.txt', "rt", encoding='utf-8') as file:
    fine = file.read()
    print(fine)