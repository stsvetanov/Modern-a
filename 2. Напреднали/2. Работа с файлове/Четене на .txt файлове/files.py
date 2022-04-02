# f = open('HW.txt/my_file.txt')
# f = open('../my_file.txt')

f = open('my_file.txt')
for line in f:
    print(line)
f.close()

with open('my_file.txt') as f:
    for line in f:
        print(line)
        split_line = line.split()
        print(split_line)


