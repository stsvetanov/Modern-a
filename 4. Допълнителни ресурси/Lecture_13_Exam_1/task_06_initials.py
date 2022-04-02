# name = input('Enter your name: ')
# print(type(name))
#
# # name = "Simeon Емилов Tsvetanov"
# names = name.split()
# print(type(names))
# # print(names)
#
# initials = []
#
# for n in names:
#     name = n[0]
#     initials.append(name)
#
# for y in initials:
#     y += "."
#     print(y, end=" ")
#

inpstring = input('Въведете име: ')
inpstring = inpstring.strip()
inpstring = inpstring.split()
initials = ''
for name in inpstring[:3]:
    initials = initials + name[0]+'.'
print(initials)
