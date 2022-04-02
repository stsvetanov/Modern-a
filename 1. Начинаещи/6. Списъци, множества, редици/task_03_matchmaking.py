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

people_len = len(people)

for index_p1, p1 in enumerate(people):
    for index_p2 in range(index_p1 + 1, people_len):
        gender_p1 = p1.get('gender')
        gender_p2 = people[index_p2].get('gender')
        if gender_p1 == gender_p2:
            continue

        interests_p1 = p1.get('interests')
        interests_p2 = people[index_p2].get('interests')

        common_interests = set(interests_p1).intersection(set(interests_p2))
        if common_interests:
            name_p1 = p1.get('name')
            name_p2 = people[index_p2].get('name')
            print(f"{name_p1} + {name_p2} -> {common_interests}")




# for idx_person_one, person_one in enumerate(people):
#     if person_one.get("gender") is "male":
#         search_gender = "female"
#     if person_one.get("gender") is "female":
#         search_gender = "male"
#
#     for idx_person_two in range(idx_person_one + 1, len(people)):
#         person_two = people[idx_person_two]
#
#         if search_gender != person_two['gender']:
#             continue
#
#         person_one_interests = set(person_one['interests'])
#         person_two_interests = set(person_two['interests'])
#
#         common_interests = person_one_interests.intersection(person_two_interests)
#
#         if common_interests:
#             print("{} и {} - общи интереси {}".format(person_one.get("name"),
#                                                         person_two.get("name"),
#                                                         common_interests))
