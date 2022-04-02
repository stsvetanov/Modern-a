# # ПРИМЕР 1: Вложена анонимна функция в потребителски дефинирана функция
# def knights():
# 	title = 'Sir'
# 	action = (lambda x: title + ' ' + x)
# 	# title в lambda е от тялото на външната дефиниция
# 	return action # връща обект функция
# act = knights()
# print(act)
# # act: обект тип функция, всъщност това е lambda функцията, която очаква да й бъде подаден аргумент
# msg = act('Robin')
# # 'Robin' се подава на lambda функцията като аргумент
# print(msg)

# # ПРИМЕР 2: анонимна функция
# L = [lambda x: x ** 2, lambda x: x ** 3,lambda x: x ** 4]
# # Списък с 3 анонимни функции
# for f in L:
#     print(f(2)) # Извежда 4, 8, 16
# print(L[0](3)) # Извежда 9

# # ПРИМЕР 3: анонимна функция
# key = 'got'
# x=int(input())
# res={'already': (lambda x: x + 2), 'got': (lambda x: x*4),'one': (lambda x: x ** 6)}[key](x)
# # {'already': (lambda x: x + 2), 'got': (lambda x: x*4),'one': (lambda x: x ** 6)}[key]  ТОВА ВРЪЩА СТОЙНОСТТА ЗА КЛЮ§А got,
# # който е функцията lambda x: x*4
# # със (x) подаваме на ламбда въведената стойност от клавиатурата
# print(res)


# # ПРИМЕР 4: Вложени анонимни функции в други анонимни функции
# action = (lambda x: (lambda y: x + y))
# act = action(99) # задава външния параметър x и очаква да се подаде y
# act(3) # задава вътрешния параметър y и изчислява целия израз

# ПРИМЕР 4: функции от тип Обвивки (Closure)
# def build_taxer(rate):
# 	def taxer(amount):
# 		return round(amount * (float(rate) / 100),2)
# 	return taxer # в ретърна стои името на вътрешната функция
# vat1 = build_taxer(22) # rate=22
# vat2 = build_taxer(7)  # rate=7
# amount=10
# print(vat1(amount))
# print(vat2(amount))

# ПРИМЕР 5: map - прилага функцията върху всички елементи от контейнера
# print(list(map(lambda x: x**2, range(1,5))))
# еквивалент на:
# L=[x**2 for x in range(1,5)]
# # 1,4,9,16

# ПРИМЕР 6:
# def f(x):
#     def g(x): return x**1
#     def z(x): return x**(-1)
#     if x>=0: return g(x)
#     else: return z(x)
#
# import time
# import random
#
# x=[random.randint(-100,100)for x in range(100000)]
#
# t1=time.time()
# k=[f(y) for y in x]
# t2=time.time()
# a=list(map(f,x))
# t3=time.time()
# print(t1,'\n',t2,'\n',t3)
# print('време за изпълнение на цикъл: '+str(t2-t1))
# print('време за изпълнение на map: '+str(t3-t2))

# # ПРИМЕР 7:
# def f(x): return x % 2 != 0 and x % 3 != 0 # ДА НЕ СЕ ДЕЛИ ТОЧНО
# a=list(filter(f, range(2, 25)))
# # Е РАЗЛИЧНО ОТ:
# def g(x): return x % 6 != 0 # ДА НЕ СЕ ДЕЛИ ТОЧНО
# b=list(filter(g, range(2, 25)))
#
# print(a)
# print(b)
# if a==b: print("еднакъв резултат")
# else: print("различен резултат, т.е. x % 2 != 0 and x % 3 != 0 е различно от x % 6 != 0")

# ПРИМЕР 8:
from functools import reduce
def factorial1(n):
	def mult(a,b): return a*b
	return reduce(mult, range(1,n+1))
# print(factorial1(5)) # Връща 6, т.е. 1*2*3, защото range(1,4)

# # ПРИМЕР 9:
# def factorial1(l):
# 	def mult(a,b): return a*b
# 	return reduce(mult,l,1)
# l=[]
# print(factorial1(l)) # резултат 1, това е стойността по подразбиране ако списъкът е празен, и е 3-тия параметър в reduce
# #
# ПРИМЕР 10:
# използваме функцията от Пример 9 factorial1
ll=[n for n in range(1,11)]
zipped=zip(ll,list(map(factorial1,ll)))
print(list(zipped))
# необходимо е ll да бъде конвертиран до списък чрез list(), за да може да се използва от map