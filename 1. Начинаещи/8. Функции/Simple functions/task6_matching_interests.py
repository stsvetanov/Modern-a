ivan = ['пушене', 'пиене', 'тия три неща', 'секс', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино', 'секс']


def common_interest(person1, person2):
    person1 = set(ivan)
    person2 = set(maria)

    return person1.intersection(person2)


ci = common_interest
print(ci(ivan, maria))





















# ivan = set(ivan)
# maria = set(maria)
#
# matching_interests = ivan.intersection(maria)
#
# print(matching_interests)