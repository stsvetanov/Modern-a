import csv
with open('sales-h.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        time = row['timestamp']
        price = row['price']
        print(f'Time: {time} -> Price: {price}')  # Access by column header instead of column number
