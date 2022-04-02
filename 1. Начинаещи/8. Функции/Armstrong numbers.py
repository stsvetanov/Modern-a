import random

def digits(number):
    ns = str(number)
    dig = len(ns)
    
    return dig

def isArm(number):
    original = number
    k = digits(number)
    sum = 0
    for i in range(1, k + 1, 1):
        sum = sum + (number % 10) ** k
        number = float(number) / 10
    if original == sum:
        check = True
    else:
        check = False
    
    return check

# Main
random.seed()   #Prepare random number generator

# Armstrong number, Нарцистични числа
# Ако к е броя на цифрите в числото, то числото трябва да бъде равно на сумата от всяка цифра повдигната на степен к
# 
# 153 = 1^3 + 5^3 + 3^3
i = 1
while i < 4:
    num = int(random.random() * 1001)
    b = isArm(num)
    if b == True:
        print(num)
        i = i + 1
