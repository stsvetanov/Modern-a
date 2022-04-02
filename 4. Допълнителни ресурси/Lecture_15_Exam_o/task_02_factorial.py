number = input("Въведете число ")

# 5! = 5*4*3*2

if not number.isdigit():
    print("Трябва да въведете число положително число. Опитайте пак")
    exit()

factorial = 1
for i in range(2, int(number) + 1):
    factorial = factorial * i

print("{}! = {}".format(number, factorial))
