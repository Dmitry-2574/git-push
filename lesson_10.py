import os
from turtle import title
os.system('cls')
# person = {
#     'first_name': 'Николай',
#     'last_name': 'Соболев',
#     'age': 30,
#     'city': 'Москва',
#     'phone': '+7(999)123-45-67',
#     'occupation': 'Программист',
#     'citizenship': 'РФ',
#     'passport': '4510 123456',
#     'gender': 'мужской'
# }

# months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')

from marvel import full_dict as fd
from pprint import pprint


# print(fd)

full_dict_list = []

# for ids, film in fd.items():
#     film['id'] = ids
#     full_dict_list.append(film)

for ids, film in fd.items():
    new_dict = {'id': ids, **film}
    full_dict_list.append(new_dict)
    
# pprint(full_dict_list, sort_dicts=False)

for film in full_dict_list:
    print(film['title'], film['year'])
    # print(id['year'])

filmsy = 'железный'

result = []

for film in full_dict_list:
    if film['title']:
        if filmsy.lower() in film["title"].lower():
            result.append(film)

pprint(result, sort_dicts=False)

stages = {
    '1': 'Первая фаза',
    '2': 'Вторая фаза',
    '3': 'Третья фаза',
    '4': 'Четвертая фаза',
    '5': 'Пятая фаза',
    '6': 'Шестая фаза',
}
user_input = '2'
result2 = []
for film in full_dict_list:
    if film['stage'] == stages[user_input]:
        result2.append(film['title'])
print(result2)

# years = '2024'
new_dict = {}

for film in full_dict_list:
    if film['year'] != 'TBA':
        if film['year'] not in new_dict:
            year = film['year']
            new_dict.append(film)
pprint(new_dict, sort_dicts=False)


        
