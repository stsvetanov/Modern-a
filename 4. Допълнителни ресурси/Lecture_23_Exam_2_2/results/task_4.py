import csv


def Run(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        list_data = []

        for item in reader:
            next_timestamp = next(reader)
            if abs(float(item[1]) - float(next_timestamp[1])) > 4:
                list_data.append(next_timestamp[0])

    return list_data


file_name = 'fridge-temp.csv'
lists = Run(file_name)
for ls in lists:
    print(ls)