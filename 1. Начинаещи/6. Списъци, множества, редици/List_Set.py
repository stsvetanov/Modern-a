# множества (set)
A={'Младост','Стрелбище','Възраждане'}
B={'Младост','Аспарухово','Чайка'}

# кои квартали са общи (лог. И &)
print(A&B)
print(A.intersection(B))
print(B.intersection(A))

# кои квартали ги има в A, но ги няма в B (-)
print(A-B)
print(A.difference(B))
# кои квартали ги има в B, но ги няма в A (-)
print(B-A)
print(B.difference(A))
# кои са всички квартали от A и B (лог.ИЛИ |)
print(A|B)
print(A.union(B))
print(B.union(A))

import random as rd
# ако разполагаме с два списъка от по 20 случайни числа,
# 1) да се намерят онези, които присъстват и в двата списъка
# 2) колко са повтарящите се числа в двата списъка ?
# кратката форма на цикъл for
l1=[rd.randint(1,101) for i in range(20)]
# аналогични варианти за използване на функции (методи)
# от някакъв модул, в случая модулът е random

# from random import randint
# a=randint(1,101)

# import random
# random.randint(1,101)

# пълната форма на цикъл for
l2=[]
for i in range(20):
    l2.append(rd.randint(1,101))
print(l1)
print(l2)
# # създаване и едновременно запълване на два сразлични списъка със случайни цели числа в интервала [1,100]
# l3,l4=[],[]
# for i in range(20):
#     l1.append(rd.randint(1, 101))
#     l2.append(rd.randint(1,101))
#
# # да се създадат и запълнят два списъка от случайни числа, общия оброи на които е 20
# # като кратните на 3 се отделят в списъла l5, а останалите в списъка l6.
# # Колко и кои са кратните на 3 случайно генерирани числа?
# l5,l6=[],[]
# for i in range(20):
#     a=rd.randint(1, 101)
#     if a%3==0:l1.append(a)
#     else: l2.append(a)
# print(len(l5))
# print(l5)

l1_set=set(l1) # превръщаме в множество
l2_set=set(l2)
# 1) да се намерят онези, които присъстват и в двата списъка
l=l1_set&l2_set
print(l)
# 2) колко са повтарящите се числа в двата списъка ?
otg=(len(l1)-len(l1_set))+(len(l2)-len(l2_set))
print(otg)
# 3) изведете на екран сортираното множество от 1)
l_list=list(l)
l_list.sort(reverse=False)
print(l_list)
# l_list=sorted(l_list) #id-то на l_list ще бъде различно
# print(l_list)

len_1=len(l)
l.add(55)
len_2=len(l) # len(променлива-контейтер) - връща броя на елементите
if len_1==len_2: print('няма нови елементи')
else:
    k={55}
    print('добавен е един нов елемент')
    print(l.issubset(k)) # k задължително трябва да бъде контейнер
    print(l.difference(k))
    print(l.intersection(k))
    print(l.union({777}))

