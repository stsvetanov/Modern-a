def catholicEastern(year):
    if year <= 2099:
        m = 24
        n = 5
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    if d + e < 10:
        day = d + e + 22
        month = 3
    else:
        day = d + e - 9
        month = 4
    if day == 26 and month == 4:
        day = 19
        month = 4
    if day == 25 and month == 4 and d == 28 and e == 6 and a > 10:
        day = 18
        month = 4
    data = "Католическият Великден е на: " + str(day) + "/" + str(month) + "/" + str(year) + chr(13) + chr(10)
    
    return data

# Main
# Намира датата на католическия Великден
print("Въведете година: ")
year = int(input())
print(catholicEastern(year))
