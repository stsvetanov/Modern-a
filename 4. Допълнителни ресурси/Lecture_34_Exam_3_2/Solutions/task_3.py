import csv

x = float(input())
y = float(input())
z = float(input())

with open('../../Task3.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=",")
    ls = []
    for item in reader:

        ls.append({
           item[0]:item[1:]
       })

for item in ls:
    for key, value in item.items():
        count = 0
        for n in value:
            if x >= float(n):
                count += 1
            elif y >= float(n):
                count += 1
            elif z >= float(n):
                count += 1

            if count == 3:
                print(key)

if count < 3:
    print('INVALID INPUT')
