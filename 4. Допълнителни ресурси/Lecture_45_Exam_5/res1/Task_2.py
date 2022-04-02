total_duration = 0
list_durations = []

with open('path.txt') as file_travel_data:
    lines = file_travel_data.read().splitlines()
    for i in lines:
        start_km, end_km, speed = map(int, i.split(","))
        if start_km > 0:
            distance = end_km-start_km+1
        else:
            distance = end_km-start_km
        partial_duration = round(distance/speed, 2)
        list_durations.append(partial_duration)

for ele in range(0, len(list_durations)):
    total_duration = total_duration + list_durations[ele]

print("Времето за пристигане от град А до град Б е: ", total_duration)
