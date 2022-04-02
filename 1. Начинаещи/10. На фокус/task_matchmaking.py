# Match people with common interests

people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': ['история', 'покер', 'пътуване', 'автомобили'],
        'gender': "male",
    },
]

# people_len = len(people)
# matches = []
#
# for idx_person_one, person_one in enumerate(people):
#     if person_one.get("gender") is "male":
#         search_gender = "female"
#     if person_one.get("gender") is "female":
#         search_gender = "male"
#
#         for idx_person_two in range(idx_person_one + 1, people_len):
#             person_two = people[idx_person_two]
#
#             if search_gender is not person_two.get("gender"):
#                 continue
#
#             person_one_interests = person_one.get("interests")
#             person_two_interests = person_two.get("interests")
#             common_interests = set.intersection(set(person_one_interests), set(person_two_interests))
#
#             if common_interests:
#                 matches.append([person_one.get("name"), person_two.get("name"), common_interests])
#
# for match in matches:
#     print(match[0] + " и " + match[1] + ": " + ", ".join(match[2]))

import itertools
print([
    (p1['name'], p2['name'])
    for p1, p2 in itertools.combinations(people, 2)
    if p1['gender'] != p2['gender'] and set(p1['interests']) and set(p2['interests'])
])


# Това е един израз
# print([(p1['name'], p2['name']) for p1, p2 in itertools.combinations(people, 2) if p1['gender'] != p2['gender'] and set(p1['interests']) & set(p2['interests'])])
