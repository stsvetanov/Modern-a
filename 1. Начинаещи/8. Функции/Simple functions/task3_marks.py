def print_mark(mark):
    if mark < 2.5:
        print("Слаб (2)")
    elif mark < 3.5:
        print("Среден")
    elif mark < 4.5:
        print("Добър (4)")
    elif mark < 5.5:
        print("Мн. Добър (5)")
    else:
        print("Отличен (6)")


# mark = input("Enter mark: ")

mark = 4.5
print_mark(mark)




