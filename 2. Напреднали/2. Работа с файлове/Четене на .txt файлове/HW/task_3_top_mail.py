'''
3. Напишете програма, която определя най-често получавания е-майл адрес от приложения файл.
'''

def prRed(skk): print("\033[91m {}\033[00m".format(skk))

list_line = []

f = open("../mbox-short.txt", "r", encoding="utf-8")
for i in f:
    if f.readline(1) in "F":
        list_line.append(f.readline()[5:-1])
f.close()

list_line.remove("Changed")
# print(list_line)
max_count = 0

for mail in list_line:
    if list_line.count(mail) > max_count:
        max_count = list_line.count(mail)
        top_mail = mail

prRed(f"Най-често получавания е-майл адрес e: {top_mail} - {max_count} пъти.")
