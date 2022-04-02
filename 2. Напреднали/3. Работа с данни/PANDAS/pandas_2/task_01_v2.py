import csv
import pandas as pd

filename = 'sales.txt'
dense_tr = {}
columns = ['id', 'country', 'city', 'date/time', 'sum']
what_index = ['1', '2', '3', '4', '5']

with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            dense_tr = {'id': row[0], 'country': row[1], 'city': row[2], 'date/time': row[3], 'sum': row[4]}
            # print(dense_tr)

            my_pandas = pd.DataFrame(dense_tr, index=what_index, columns=columns)


print(my_pandas)