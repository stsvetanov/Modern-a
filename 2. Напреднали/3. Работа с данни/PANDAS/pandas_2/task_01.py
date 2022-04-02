import pandas as pd
columns = ['id', 'country', 'city', 'ts', 'price']

dataset = pd.read_csv("sales.txt", names=columns)

print(dataset)
print(dataset.head(7))
