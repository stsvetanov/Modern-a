def checkHarshad(n, base):
    # function to check Harshad Number
    sum = 0
    temp = n
    while temp > 0:
        sum = sum + temp % base
        temp = float(temp) / base
    if n % sum == 0:
        result = True
    else:
        result = False
    
    return result

# Main
# An integer number in base 10 which is divisible by sum of it digits is said to be a Harshad Number. An n-harshad number is an integer number divisible by sum of its digit in base n.
nonhash = [0] * (20)
ishash = [0] * (20)

print("*********  Harshad Numbers  **********")
print("Проверка на първите 20 числа за пълен Харшаз, за бази 2, 8, 10, 16")
for i in range(0, 19 + 1, 1):
    ishash[i] = 0
    nonhash[i] = 0
for i in range(0, 19 + 1, 1):
    b = checkHarshad(i + 1, 2)
    o = checkHarshad(i + 1, 8)
    d = checkHarshad(i + 1, 10)
    h = checkHarshad(i + 1, 16)
    if b and d and o and h:
        ishash[i] = i + 1
    else:
        nonhash[i] = i + 1
print("Числата, които са пълен Харшад са: ")
for i in range(0, 19 + 1, 1):
    if ishash[i] != 0:
        print(ishash[i])
print("Числата, които не са пълен Харшад са: ")
for i in range(0, 19 + 1, 1):
    if nonhash[i] != 0:
        print(nonhash[i])
