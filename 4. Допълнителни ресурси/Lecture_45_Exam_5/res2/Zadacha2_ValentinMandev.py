def calculate(start, end, speed):
    time = (end + 1 - start) / speed
    return time


parts = list()

with open('task2.txt') as file:
    for lines in file:
        parts.append(lines.split(','))
file.close()

total_time = float()
for part in range(len(parts)):
    total_time += calculate(int(parts[part][0]), int(parts[part][1]), int(parts[part][2]))

print(round(total_time, 2))


