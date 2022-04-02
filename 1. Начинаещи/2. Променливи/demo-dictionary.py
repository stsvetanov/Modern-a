# Ключовете в речника за множество
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D.get('spam'))
print(D.get('spam4'))
# print(D['spam4'])
print(D)

D["one"] = 5
print(D)
D["one"] = 7
print(D)
#
for i in D:
    print(i)

for key, value in D.items():
    print(key)
    print(value)
#
#
а = "асдфасдфа;алскдйф;аскдйфа;лкдсйфгастре"

d = dict()

for el in а:
    if d.get(el) is None:
        d[el] = 1
    else:
        d[el] = d.get(el) + 1
print(d)

# table = {'1975': 'Holy Grail', '1979': 'Life of Brian', '1983': 'The Meaning of Life'}
#
# for year in table:
#     print(year + '\t' + table[year])