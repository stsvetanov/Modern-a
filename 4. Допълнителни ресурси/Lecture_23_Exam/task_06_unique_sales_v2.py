import csv
from collections import defaultdict

ID = 0
CITY = 2

file_handler = open('../sales_001.csv')
csv_reader = csv.reader(file_handler)

sales_by_id = defaultdict(set)
for line in csv_reader:
    sales_by_id[line[ID]].add(line[CITY])

unique_sale_by_city = defaultdict(set)
for sale_id, city_names in sales_by_id.items():
    if len(city_names) == 1:
        city_name = city_names.pop()
        unique_sale_by_city[city_name].add(sale_id)

for city_name, sales in sorted(unique_sale_by_city.items()):
    print(', '.join([city_name] + sorted(sales)))

