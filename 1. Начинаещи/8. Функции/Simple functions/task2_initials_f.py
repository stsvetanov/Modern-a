def initials(name):
    names = name.split()

    initials = []

    for n in names:
        name = n[0]
        initials.append(name)

    # print(initials)

    for y in initials:
        y += "."
        print(y, end=" ")
    print()

# name = input('Enter your name: ')
initials("Ivan Petrov Ivanov")
initials("Петър Георгиев Маринов")
initials("Петър Георгиев Маринов")
initials("Петър Георгиев Маринов")