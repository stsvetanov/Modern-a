from datetime import datetime
from datetime import timedelta

date_input = input("Въведете дата:")
converted_to_datetype = datetime.strptime(date_input, "%d.%m.%Y")
date_1_day_ago = converted_to_datetype-timedelta(days=1)

print(datetime.strftime(date_1_day_ago,"%d.%m.%Y"))

