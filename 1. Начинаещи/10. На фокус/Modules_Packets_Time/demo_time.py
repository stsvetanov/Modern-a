from datetime import datetime, date, timedelta

# dt = datetime.now()
# print(dt)
# #
# d = date.today()
# print(d)
# #
# dt = dt.replace(year=dt.year + 1) # bad practice, check relative delta
# print(dt)
# print(type(dt))


#
# dt1 = datetime(2020, 8, 17)
# dt1 = datetime(year=2020, month=8, day=17, hour=17, minute=56, second=8)
# dt2 = datetime(year=2025, month=8, day=2, hour=7, minute=56, second=8)
# print(dt1)
# print(dt2)
# #
# tdelta = dt2 - dt1
# print(tdelta)
#
#
dt = datetime.now()

print(str(dt)) # could be sorted
print(dt.isoformat())

print(dt.strftime('%H nescho %Y'))
print(dt.strftime('%Y - %H %M'))

date_str_iso = dt.isoformat()

import iso8601
print(dt.isoformat())

d_object = iso8601.parse_date(dt.isoformat())
print(d_object)
