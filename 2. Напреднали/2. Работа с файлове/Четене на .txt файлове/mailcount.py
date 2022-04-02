# fname = raw_input('Enter file name: ')

file_name = 'mbox-short.txt'
file_handler = open(file_name)

c = dict()

for line in file_handler:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    print(email)
    c[email] = c.get(email, 0) + 1

print(c)
file_handler.close()
