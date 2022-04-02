l = float(input('Въведете дължина: '))
w = float(input('Въведете широчина: '))
h = float(input('Въведете височина: '))

file = '../Task3.csv'
import pandas as pd

data = pd.read_csv(file, delimiter=',', names=['product', 'length', 'width', 'height'])

input_size = sorted([l, w, h])

d = dict(zip(data['product'], [data['length'], data['width'], data['height']]))
# print(d)
sorted_sizes = []
for key in d:
    sorted_sizes = sorted(d[key])
    print(sorted_sizes)
    if sorted_sizes[0] <= input_size[0] and sorted_sizes[1] <= input_size[1] and sorted_sizes[2] <= input_size[2]:
        print(key)
