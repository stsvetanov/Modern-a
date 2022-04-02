# # Да се напише програма, която създава списък
# # Списъкът е от случайни числа в интервала от 1 до 10000 включително
#
# # Ламбда функциите трябва да отговарят на следните условия:
p_1=' Числата да бъдат кратни (да се делят точно) на 2'
p_2=' Числата да НЕ бъдат кратни (да НЕ се делят точно) на 2'
p_3=' Числата да съдържат цифрата 1'

# Всички lambda функции до тук (l_1, l_2, l_3) връщат True или False => ще ги използваме като филтър
l_1=lambda x:x%2==0
l_2=lambda x:x%2!=0
l_3=lambda x:'1' in str(x)

lambdas=[l_1,l_2,l_3]
text_to_print=[p_1,p_2,p_3]

from random import randint
L=[randint(1,1001) for i in range(20)]

for i in range(len(lambdas)):
    l_temp=list(filter(lambdas[i],L))
    l_temp_map=list(map(lambdas[i],L))
    # map(функция, контейнер (списък)) => връща същия брой елементи колкото са в списъка
    # filter(функция, контейнер(списък)) => връща <= брой елементи от колкото са в списъка
    print(text_to_print[i])
    print(L)
    print(l_temp_map)
    print(l_temp)

M=[]
def rec_1(L,m):
    if L==[]:
        return m
    else:
        # if L[0] % 2 ==0:
        if '1' in str(L[0]):
            m.append(L[0])
            return rec_1(L[1::],m)
        else:
            return rec_1(L[1::], m)

print("Рекурсия")
print(rec_1(L,M))
print(L)

# Да се генерират всички номера,
# съдържащи буквата Р в областния код и пореден номер с цифрите от 5 до 9.

XX=['А', 'Е', 'В', 'ВТ', 'ВН', 'ВР','ЕВ','ТХ','К','КН','ОВ','М','РА','РК',
'ЕН','РВ','РР','Р','СС','СН','СМ',"СО","С","СА","СВ","СТ",'Т','Х',"Н","У"]
YY=['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У','Х']
NNNN='56789'
# 555,556,557,565,566,567,577,576,575
# 666,656,657,675,676,677,655,665,667,
# 777,775,776,755,756,757,765,766,767
# от 6 възможни цифри, трябва да направи 4 цифрено число, повторенията са допустими

xx_lambda= lambda s: ('Р' in s) or ('P' in s)
XXf=list(filter(xx_lambda,XX))
s=""
NNNN_strings=[]
for s0 in NNNN:
    for s1 in NNNN:
        for s2 in NNNN:
            for s3 in NNNN:
                s=s0+s1+s2+s3
                NNNN_strings.append(s)
print(len(NNNN_strings))

YY_strings=[]
s=""
for s0 in YY:
    for s1 in YY:
        s = s0 + s1
        YY_strings.append(s)
print(len(YY_strings))
car_number=[]
for x in XXf:
    for n in NNNN_strings:
        for y in YY_strings:
            car_number.append(x+n+y)
print(len(car_number))
print(car_number[0:10])