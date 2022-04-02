# ЗАДАЧА 4:
number=int(input('Въведи цяло число'))

#Вариант 1: чрез стрингове
s=str(number)
s=s[::-1]
number_v1=int(s)
print(number_v1)

#Вариант 2: чрез списъци
s=str(number)
s1=[]
for i in s: s1.append(i)
#генрира списък от цифрите, но като символи
s1=s1.reverse() # ако не знаем за s[::-1]
print(s1)
s=''.join(s1)
number_v2=int(s)
print(number_v2)

#Вариант 3: чрез деление % и //
l=len(str(number)) # връща броя на цифрите в числото
new_num=[]
for i in range(l):
    new_num.append(number%10)
    number=number//10
new_num=[str(i) for i in new_num]
new_num=''.join(new_num)
new_num=int(new_num)
print(new_num)
