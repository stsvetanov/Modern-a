import datetime

input_date = input()
day = int(input_date.split('.')[0])
month = int(input_date.split('.')[1])
year = int(input_date.split('.')[2])


output_date = (datetime.date(day = day, month = month, year = year) - datetime.timedelta(1))
print(output_date.strftime('%d.%m.%Y'))


