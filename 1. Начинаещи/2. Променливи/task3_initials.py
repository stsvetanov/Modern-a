# name = input('Enter your name: ')

name = "Simeon Emilov Tsvetanov Vood"
names = name.split()
print(names)
print(type(names))
#
initials = []

for n in names:
    name = n[0]
    # if name.isupper():
    initials.append(name)

print(initials)

for y in initials:
    y += "."
    print(y, end=" ")

