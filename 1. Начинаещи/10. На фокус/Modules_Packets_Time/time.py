# import time
# print(time.time())

# # Обектът datetime от пакета datetime работи с информация за час и дата, с включено управление и на часови зони.
# from datetime import datetime
# #
# print(datetime.now())
# print(datetime(2016, 1, 19))
# print(datetime(2022, 1, 19, 20, 21, 22, 222425))
# print(datetime(month=5, year=2025, day=19, hour=20, minute=21, second=22, microsecond=222425))
#
# # Ако Ви е необходима работа само с дати (без час), можете да използвате datetime.date.
# from datetime import date
#
# print(date(2018, 1, 19))
# d = date.today()
# print(d)
#
from datetime import datetime
# dt = datetime.now()
# d = dt.date()  # създава нов обект date,  съдържащ само информацията за дата от обект datetime
# print(d)

# # За разпечатване/форматиране на datetime стойности можете да използвате няколко метода:
# from datetime import datetime
# d = datetime(2020, 1, 19, 20, 21, 22, 222425)
# print(str(d))
#
# # Parse на str към date / datetime обекти
# from datetime import datetime
# string_value = '2020-01-19 20:21:22.222425'
# datetime_value = datetime.strptime(string_value, '%Y-%m-%dT%H:%M:%S.%f')
# print(datetime_value)

# ISO8601 е международен стандарт за запис на дата/час в символен низ str
from datetime import datetime
d = datetime.now()
print(d.isoformat())
#
# Използваме външния пакет iso8601, за да направим конвертирането (parse) от ISO-8601 стринг към datetime обект
import iso8601
dt_str = '2019-06-05T18:45:20.330541'
d = iso8601.parse_date(dt_str)
print(d)

# # Аритметика с време
# from datetime import datetime, timedelta
# d = datetime.now()
# t = timedelta(hours=2)
# print(d + t)
# print(d - t)
# print(t)
#
# # # Аритметика с време
#
# from datetime import datetime, timedelta
# d = datetime.now()
# d_earlier = datetime(2018, 7, 26, 18, 00)
# td = d - d_earlier
#
# print(td)
# print(td.days)
# print(td.seconds)
# print(td.microseconds)
# print(td.total_seconds())

# # time zones
# from datetime import datetime
# import pytz
#
# z = pytz.timezone('Europe/Paris')
# d = datetime.now(tz=z)
#
# print(d.isoformat())

# import iso8601
# d = iso8601.parse_date('2016-01-19T20:23:14.608574+02:00')
# print(d)
# print(d.isoformat())

# https://www.programiz.com/python-programming/datetime
# from datetime import datetime
# import pytz
#
# local = datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
#
# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_NY)
# print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
#
# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


# # # Конвертиране
# from datetime import datetime
# import pytz
#
# z = pytz.timezone('Europe/Sofia')
# d = datetime.now(tz=z)
#
# print(d.astimezone(pytz.timezone('Asia/Tokyo'))
#
# print(d.astimezone(pytz.timezone('UTC')))


#
# from datetime import timezone
#
# print(d.astimezone(timezone.utc))



