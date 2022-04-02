ivan = ['пушене', 'пиене', 'тия три неща', 'секс', 'коли', 'facebook', 'игри', 'разходки по плажа',
        'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино', 'секс']


# def common_interests(person1, person2):
#     common = []
#
#     for interest_p1 in person1:
#         if interest_p1 in person2:
#             common.append(interest_p1)
#
#     return common
#
#
# print(common_interests(ivan, maria))

# ivan = set(ivan)
# maria = set(maria)
# print(ivan.intersection(maria))
# print(ivan.difference(maria))
#
# print(sorted(ivan))


def list_1():
    l1 = list()
    while True:
        interest = input('Persone_1 - Въведи интерес: ')
        if interest == 'stop':
            break
        l1.append(interest)
    return l1


def list_2():
    l2 = list()
    while True:
        interest = input('Persone_2 - Въведи интерес: ')
        if interest == 'stop':
            break
        l2.append(interest)
    return l2


def element_in_list(arg1, arg2):
   for i in arg1:
       if i in arg2:
           print(f'Има съвпадение : {i}')
       else:
           print('Няма съвпадение')


# a = list_1()
# b = list_2()
element_in_list(ivan, maria)
