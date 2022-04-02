# f = open('./directory/lecture.txt')
# f = open('mbox-short.txt')
# print(type(f))
#
# print(next(f))
# print(next(f))
# print(next(f))
#
# for line in f:
#     print(line)
# f.close()

# with open('../Lecture_07_Files/mbox-short.txt') as f:
#     for line in f:
#         print(line)
#
# # За да презапишете съдържанието на файл, като елиминирате текущото му съдържание, при отваряне трябва да добавите допълнителен параметър - w:
# with open('numbers.txt', 'w') as f:   # с 'w' съдържанието на файла ще бъде изтрито, и ще започнем в пишем на празен файл
#     for i in range(20):
#         f.write(str(i))
#         f.write("\n")
#
# За да допълните съдържание във файл, като запазите текущото му съдържание, при отваряне трябва да добавите допълнителен параметър - а:
with open('numbers.txt', 'a') as f:   # с 'а' съдържанието на файла се запази, и писането в този файл ще допълва в края на файла
    for i in range(20):
        f.write(str(i))
        f.write("\n")