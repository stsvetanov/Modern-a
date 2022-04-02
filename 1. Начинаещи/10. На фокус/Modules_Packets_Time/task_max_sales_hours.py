import csv
from collections import defaultdict

from iso8601 import iso8601

TIME_STAMP = 3
PRICE = 4

# sales_by_hour = defaultdict(float)
sales_by_hour = {}

with open('sales.csv') as fp:
    reader = csv.reader(fp, delimiter=',')
    # next(reader) # skip the headers
    for line in reader:
        print(line)
        time_stamp = line[TIME_STAMP]
        ts = iso8601.parse_date(time_stamp)
        hour = ts.replace(minute=0, second=0, microsecond=0)
        price = float(line[PRICE])

        if hour not in sales_by_hour:  # slagame gi
            sales_by_hour[hour] = price  # v rechnika
        else:
            sales_by_hour[hour] = sales_by_hour.get(hour) + price  # uvelichava se cenata

        # sales_by_hour[hour] = sales_by_hour[hour] + price

    amounts_by_time_sorted = []
    for ts, total_amount in sales_by_hour.items():
        amounts_by_time_sorted.append((total_amount, ts))

    amounts_by_time_sorted.sort(reverse=True)

    print("""
        Сума на продажби по часове (top 5)
    -----------------------------
    """)

    for total_amount, ts in amounts_by_time_sorted[:5]:
        print("     {}: {:.2f} €".format(ts, total_amount))
