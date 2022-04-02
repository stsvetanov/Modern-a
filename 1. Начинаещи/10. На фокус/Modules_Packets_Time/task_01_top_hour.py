import iso8601

sales_time = open("sales.txt")
sales_count_by_hour = {}

for t in sales_time:
    dt = iso8601.parse_date(t)
    dt = dt.replace(minute=0, second=0, microsecond=0)   # с точност до час

    if dt not in sales_count_by_hour:
        sales_count_by_hour[dt] = 1
    else:
        sales_count_by_hour[dt] += 1

bigc = None
bigv = None

for word in sales_count_by_hour:
    value = sales_count_by_hour[word]
    if bigc is None or value > bigc:
        bigv = word
        bigc = value

print(f"Top hour: {bigv} - sales: {bigc}")
