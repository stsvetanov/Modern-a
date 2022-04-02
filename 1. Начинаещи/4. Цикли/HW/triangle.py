# m = int(input("Въведете число: "))

# for n in range(1, m + 1):
#     print(" " * (m - n) + "* " * n)


# for i in range(m):
#     print(' ' * (m - (i + 1)), '*' * (2 * i + 1));


# number=int(input("Въведете число: "))
#
# for i in range(number+1):
#     for j in range(i):
#         print("*", end='')
#     print()


number=int(input("Въведете число: "))
space = number - 1
leaf = 1
for i in range(0, number):
    for j in range(0, space):
        print(' ', end='')
    for j in range(0, leaf):
        print('*', end='')
    for j in range(0, space):
        print(' ', end='')
    leaf = leaf + 2
    space = space - 1
    print()

