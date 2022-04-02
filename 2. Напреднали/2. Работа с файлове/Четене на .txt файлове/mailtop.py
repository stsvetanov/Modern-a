# fname = raw_input('Enter file name: ')
fname = 'mbox-short.txt'

with open(fname) as f:
    c = dict()
    for line in f:
        if not line.startswith('From '):
            continue
        pieces = line.split()
        email = pieces[1]
        c[email] = c.get(email, 0) + 1

top_key = None
top_value = None
for word in c:
    value = c[word]
    if top_key is None or value > top_key:
        top_value = word
        top_key = value

print(top_value, top_key)

