def mychr(number):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    allCaps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if number in range(97,123): ch = alpha[number-97]
    elif number in range(65,91): ch = allCaps[number-65]
    else: ch="@"
    return ch

def myord(ch):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    allCaps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = 97
    numA = 65
    if ch in alpha: number = num + alpha.index(ch)
    elif ch in allCaps: number = numA + allCaps.index(ch)
    else: number = 0
    return number

print(mychr(90))
print(myord('з'))
print(mychr(122))
print(myord('1'))
print(mychr(40))
print(myord('('))
# Main
s = input()
n = len(s)
sum = 0
for i in range(n):
    sum = sum + myord(s[i])
    # събира стойностите на всички символи
temp = str(float(sum) / n)
print(temp)
# изчислява средната стойност на всички символи
if temp=='0.0':temp2=0
elif temp[2] == ".":
    # ако средната стойност е реално число връща само цялата част
    temp2 = temp[0] + temp[1]
    # алтернативно:
    # temp2=int(float(temp))
else:
    # ако средната стойност е цяло число:
    temp2 = temp[0] + temp[1] + temp[2]
    # алтернативно:
    # temp2=int(temp)
temp = mychr(int(temp2)) # този ред при алтернативното пресмятане отпада

print(temp)

