'''
3. Напишете програма, която определя най-често получавания е-майл адрес от приложения файл.
'''


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


emails = {}

file_handler = open("../mbox-short.txt", "r", encoding="utf-8")

for line in file_handler:
    if not line.startswith('From '):
        continue
    else:
        email = line.split()[1]
        if emails.get(email) is None:
            emails[email] = 1
        else:
            emails[email] = emails.get(email) + 1

file_handler.close()

print(emails)

max_count = 0
for key, count in emails.items():
    if count > max_count:
        max_count = count
        top_mail = key

prRed(f"Най-често получавания е-майл адрес e: {top_mail} - {max_count} пъти.")
