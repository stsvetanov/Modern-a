# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not b)
# c = True
# print(a and not (b or c))

# id(1) == id(True)
# 1 is True
# Двата записа са еквивалентни

l=['банан','ябълка',"круша"]
m=''.join(l)
print(m)
m=', '.join(l)
print(m)
m.split(", ")
# резултат от m.split(", "): ['банан', 'ябълка', 'круша']


# 'ябълки и круши и "мандарини"'
# "ябълки и круши и 'мандарини'"

# shift+tab изтегля маркирания блок от команди на ляво
# tab премества навътре маркирания блок от команди
# ctrl+/ ще закоментира маркиран блок от команди или ще го разкоментира (ако вече е коментиран
# dd=25
# m=2
# y=2021
# st='петък'
# s="Днес %d.%d.%d е %s" % (25,2,2021,'петък')
# print(s)
#
# s="Днес "+str(dd)+"."+str(m)+"."+str(y)+" e "+st
# print(s)
#
# s="Днес %d.%d.%d е %s" % (dd,m,y,st)
# print(s)

# n=int(input("въведете число: "))
# L=[12,32,1,2,3,5,92]
# LL=L[::-1] #преобръща изписането на елементите в обратен ред
# print(L)
# print(LL)
# s=''
# for i in range(len(L)): # от [0 ; len(L)-1]
#     if n==L[i]: s+="("+str(i)
# for i in range(-len(L),0):
#     if n == L[i]: s += ", " + str(i)+")"
# print(s)
# print(L.index(n))
# print(L[:5])
# print(L[5:])

# # Задача за размяна на стойностите на две променливи
# x=5
# y=12
# def ab_1(x, y=0):
#     # размяна чрез трета променлива
#     # x и y са числа
#     # функцията връща редица от разменените стойности
#
#     c = x
#     x = y
#     y = c
#     # print(x,y)
#     return (x, y)
# def ab_2():
#     # размяна БЕЗ трета променлива
#     global x,y
#     x = x + y
#     y = x - y
#     x = x - y
#     return (x, y)
# print((x,y))
# print(ab_1(x,y))
# print((x,y))
# print(ab_2())
# print((x,y))
# x,y=y,x
# print((x,y))
# a,b=0,1
# # a=0
# # b=1

# s=''
# while b<10:
#     s+=str(b)+","
#     a,b=b,a+b
# # print(s[:-1])
# l=s[:-1].split(',')
# print(l)
# for i in range(len(l)):
#     l[i]=int(l[i])
# print(l)
#
# ll=[int(l[i]) for i in range(len(l))]
# print(ll)

# if <uslowie>:
#     <blok ot komandi>
# elif <uslovie>:
#     < blok ot komandi >
# ...
# elif <uslovie>:
#     < blok ot komandi >
# else:
#     < blok ot komandi >
#
# for k in l:
#     print(k)
# for i in range(len(l)):
#     print(l[i])
#
# s="hello 'world' "
# st='hello "world" '
# print(s)
# print(st)