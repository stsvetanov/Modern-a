import csv

TEMP_DIFFERENCE = 4

try:
    data_filename = input()

    with open(data_filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        previous_temperature = None
        for row in reader:
            # this will also validate that the CSV file has 2 columns
            current_ts, current_temp = row
            current_temp = float(current_temp)

            if previous_temperature is not None:
                if current_temp - previous_temperature >= TEMP_DIFFERENCE:
                    print(current_ts)

            previous_temperature = current_temp

except Exception as e:
    print("INVALID INPUT")