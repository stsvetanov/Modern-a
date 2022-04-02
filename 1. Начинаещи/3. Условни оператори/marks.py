# score = float(input())
# if score < 2.5:
#     print("Слаб (2)")
# if 2.5 <= score < 3.5:
#     print("Среден (3)")
# if 3.5 <= score < 4.5:
#     print("Добър (4)")
# if 4.5 <= score < 5.5:
#     print("Много добър (5)")
# if 5.5 <= score:
#     print("Отличен (6)")

# user_input = float(input("Enter mark: "))
#
# if user_input < 2.5:
#     print("Слаб (2)")
# elif user_input < 3.5:
#     print("Среден (3)")
# elif user_input < 4.5:
#     print("Добър (4)")
# elif user_input < 5.5:
#     print("Мн. Добър (5)")
# else:
#     print("Отличен (6)")


user_input = float(input("Enter mark: "))

if user_input < 2.5:
    print(f"Слаб ({round(user_input)})")
elif user_input < 3.5:
    print(f"Среден ({round(user_input)})")
elif user_input < 4.5:
    print(f"Добър ({round(user_input)})")
elif user_input < 5.5:
    print(f"Мн. добър ({round(user_input)})")
else:
    print(f"Отличен ({round(user_input)})")
