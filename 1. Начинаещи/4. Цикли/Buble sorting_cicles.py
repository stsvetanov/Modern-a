# Сортиране на елементите чрез размяна на стойности на място в масива (метод на балончето, buble sort)
print("Въведете брой на елементите n:")
n = int(input())
a = [0] * (n)

for i in range(0, n - 1 + 1, 1):
    a[i] = int(input())

# SWAP служи за размяна на стойности
print("Изберете посока на сортирането (+/-): ", end='', flush=True)
s = input()

# sorted e TRUE когато поредната стойност от масива е по-голяма от следващата. Ако вторият цикъл FOR приключи със sorted=False => има стойности, които не са подредени и DO се завърта отново с модифицирания масив. Ако вторият цикъл излезе със стойност sorted=True, означава че всяка една двойка съседни стойности са подредени в указания ред.
sorted = True

# Цикълът DO се изпълянва с условие докато sorted=False
if s == "-":
    
    # Сортира в намаляващ ред
    while True:    #This simulates a Do Loop
        
        # FOR цикъл до n-2, защото сравняваме с a[i] със a[i+1]
        # Цикъл 1: FOR за размяна на стойностите на два съседни елемента
        for i in range(0, n - 2 + 1, 1):
            if a[i] < a[i + 1]:
                swap = a[i]
                a[i] = a[i + 1]
                a[i + 1] = swap
            sorted = True
        
        # Цикъл 2: FOR проверява дали всички съседни двойки елементи са наредени правилно. Ако това е така, то sorted=True и се излиза от цикъла DO. Ако sorted=False, то се започва изпълнението на Цикъл 1 с текущото състояние на масива а.
        for j in range(0, n - 2 + 1, 1):
            if sorted == True:
                if a[j] >= a[j + 1]:
                    pass
                else:
                    sorted = False
        if not(sorted == False): break   #Exit loop
else:
    
    # Сортира в нарастващ ред
    while True:    #This simulates a Do Loop
        
        # FOR цикъл до n-2, защото сравняваме с a[i] със a[i+1]
        # Цикъл 1: FOR за размяна на стойностите на два съседни елемента
        for i in range(0, n - 2 + 1, 1):
            if a[i] > a[i + 1]:
                swap = a[i]
                a[i] = a[i + 1]
                a[i + 1] = swap
            sorted = True
        
        # Цикъл 2: FOR проверява дали всички съседни двойки елементи са наредени правилно. Ако това е така, то sorted=True и се излиза от цикъла DO. Ако sorted=False, то се започва изпълнението на Цикъл 1 с текущото състояние на масива а.
        for j in range(0, n - 2 + 1, 1):
            if sorted == True:
                if a[j] <= a[j + 1]:
                    pass
                else:
                    sorted = False
        if not(sorted == False): break   #Exit loop
print("Сортирани числа: ", end='', flush=True)
for i in range(0, n - 1 + 1, 1):
    print(str(a[i]) + " ", end='', flush=True)
