l=[1,2,3,0,4,5,0]
k=[]
# for i in range(len(l)):
#     try:
#         a=l[i]/l[i+1]
#         m=round(a,2)
#     except:
#         m=-1
#     finally:
#         k.append(m)
# print(k)
# print(k.count(-1))
# #
# k=[]
# for i in range(len(l)):
#     try:
#         m=round(l[i]/l[i+1],2)
#     except:
#         m=-1
#     k.append(m)
# print(k)
# # [0.5, 0.67, -1, 0.0, 0.8, -1, -1]
#
# for i in range(len(l)):
#     try:
#         m=round(l[i]/l[i+1],2)
#     except:
#         pass
#     k.append(m)
# print(k)
# # [0.5, 0.67, 0.67, 0.0, 0.8, 0.8, 0.8]
# # командата pass не прави нищо, и затова когато има изключение
# # към k се добавя елемент със стойност равна на последната изчислена за m
# k=[]
# for i in range(len(l)):
#     try:
#         m=round(l[i]/l[i+1],2)
#         k.append(m)
#     except:
#         pass
# print(k)
# # [0.5, 0.67, 0.0, 0.8]

# k=[]
# for i in range(len(l)):
#     try:
#         m=round(l[i]/l[i+1],2)
#         # k.append(m)
#     except:
#         # pass
#         m=-1
#     else:
#         k.append(17)
#         # за всеки възможен try, освен резултата от try се изпълняват и командите в клаузата else
#     finally:
#         k.append(m)
# print(k)
# print('Брой грешки: '+str(k.count(-1)))
# print('Брой успешни обработки: '+str(k.count(17)))
# # [0.5,   17, 0.67, 17,  0.0, 17, 0.8, 17]

# k=[]
# for i in range(len(l)):
#     try:
#         l[i]/l[i+1]
#     except:
#         pass
#     else:
#         m = round(l[i] / l[i + 1], 2)
#         k.append(m)
#         # за всеки възможен try, освен резултата от try се изпълняват и командите в клаузата else
# print(k)
# # [0.5, 0.67, 0.0, 0.8]
#
# try: print(3/0)
# except ZeroDivisionError: print('Деление на 0')
# else: print("Няма грешки")
# finally:print("Край!")

l=[10,9,8,7,6,11]
# Проверка дали l е сортиран в намаляващ ред
class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass
# n=True
# for i in range(len(l)-1):
#     try:
#         if l[i]<l[i+1]:
#             n=False
#             raise CustomError()
#         else:pass
#
#     except CustomError:
#         print('Редицата не е намаляваща...')
#         break
# # if n: print('Редицата е намаляваща')
# #
# # Алтернативен вариант без try/except/raise
# n=True
# for i in range(len(l)-1):
#     if l[i]<l[i+1]:
#         n=False
#         print('Редицата не е намаляваща...')
#         break
# if n: print('Редицата е намаляваща')
#
# # Друг пример за потребителски дефинирани изключения
# import sys
# class FooError(Exception):
#     """Base class for exceptions in this module."""
#     pass
# def foobar (x):
#     # Функцията няма нужда от return
#     # тя само определя условията, при които се вдига конкретна грешка
#     if x < 0:
#         raise FooError()
# try:
#     foobar(-1)
# except FooError:
#     print('Грешка: x<0')
#     # sys.exit()

# Да се въведат от клавиатурата 5 цели числа, по-големи от 5
# i=0 # брояч
# k=[]
# while i<5:
#     try:
#         m=int(input()) # реално е проверка дали сме въвели цяло число
#     except:
#         pass
#     else:
#         # По-добрият вариант е вместо всичко да бъде в TRY секцията,
#         # защото по този начин:
#         #   1) намаляваме броя на проверяваните команди и
#         #   2) сме сигурни, че условието, което проверяваме е едно,
#         #   в противен случай няма да сме сигурни къде е грешката
#         if m>5:
#             k.append(m)
#             i+=1
# print(k)
#
# while i<5:
#     try:
#         m=int(input()) # реално е проверка дали сме въвели цяло число
#         if m>5:
#             k.append(m)
#             i+=1
#     except:
#         pass
#
# print(k)

# # Дефиниране на функция, която проверява дали дадена друга функция връща грешка или не, чрез използване
# # на try/except в тялото на функцията. Форматът на използване е: ako f(x), то проверката дали f(x)
# # ще може да се изпълни ще бъде iserror(f,x)
# def iserror(func, *args, **kw): # булева функция, връща True/False
#     # False означава, че няма грешка
#     # True означава, че има грешка
#     try:
#         func(*args, **kw)
#         return False
#         # т.е. Не, не връща грешка
#     except Exception:
#         return True
#         # т.е. Да, връща грешка
#
# i=0
# k=[]
# while i<5:
#     f=input()
#     m=iserror(int,f)
#     if m==False:
#         l=int(f)
#         if l>5:
#             k.append(l)
#             i+=1
# print(k)

# задача: да се намери средното на всички елементи от списъка, които са числа
# l=[1,2,3,'0',4,5,'0',True,[1,2,3],(1,2)]
# print(l)
# try/except върху mean(l)
# isinstance(l[i],int) or isinstance(l[i],float)

# try:
#     mean=round(sum(l)/len(l),2)
# except:
#     i=len(l)-1
#     while i>0:
#         condition_1=((not isinstance(l[i],int)) and (not isinstance(l[i],float)))
#         condition_2=isinstance(l[i],bool) # 1 също се преброява като TRUE !!!
#         condition=condition_1 or condition_2
#         print(condition)
#         if condition:
#             l.remove(l[i])
#         i=i-1
#     mean=round(sum(l)/len(l),2)
# finally:
#     print(mean)
#
# print(l)

# задача: да се намери средното на всички елементи от списъка, които са числа
# ако има елементи от тип стринг, да се вземе:
# ако е възможно int стойността
# ако е възможно float стойността
# кода на стринга
# ако не е възможно, да се пропуснат
l=[1,2,3,'0',4,5,'0','u','jk']
print(l)
# try/except върху mean(l)
# isinstance(l[i],int) or isinstance(l[i],float)
k=[]
f=[]
try:
    sum(l)
except:
    for i in range(len(l)):
        if isinstance(l[i],str):k.append(l[i])
    if len(k)>0:
        for i in k:
            l.remove(i)
    print(l)
    print(k)
    if len(k)>0:
        for i in range(len(k)):
            try: int(k[i])
            except:
                try: float(k[i])
                except:
                    try: ord(k[i])
                    except:f.append(k[i])
                    else: k[i]=ord(k[i])
                else:
                    k[i]=float(k[i])
            else:
                k[i]=int(k[i])
        print(k)
        if len(f)>0:
            for i in f:
                k.remove(i)
        mean=round((sum(l)+sum(k))/(len(l)+len(k)),2)
    else:
        mean=round(sum(l)/len(l),2)
else:
    mean = round(sum(l) / len(l), 2)
finally:
    print(mean)

# алтернатовно решение 1
# print(l)
# s=0
# n=0
# f=[] # във f отделяме всичко, което може да бъде представено като число
# #Събиране първо на float(l) числа, защото всяко число може да се сведе до float
# for i in l:
#     try: float(i)
#     except: pass
#     else: f.append(i) # във f са всички събираеми
# for i in f:
#     l.remove(i) # във l остават само стрингове, между които може да има такива, които да направим с ord()
#
# if len(l)>0:
#     # Изделяне на ord(i) във f
#     for i in l:
#         try: ord(i)
#         except: pass
#         else: f.append(ord(i))
#
# print(sum(f),round(sum(f)/len(f),2))

# алтернатовно решение 2
# l=[1, 2, 3, '0', 4, 5, '0', 'u', 'jk']
# print(l)
# f=[]
# n,s=0,0
# def tryex_1(func):
#     # входният параметър func представлява функция, която ще се опитва да обработва пореден елемент от списък
#     # func може да бъде всяка една вградена функция или всяка друга потребителски дефинирана
#     global l,n,s
#     # l, f, n, s са глобални променливи, т.е. изменяеми в процеса на работата на функцията
#     # l: първоначалния списък
#     # n: брояч на елементи
#     # s: сума на елементи
#     if len(l) > 0:
#         f = [] # локален помощен списък, чрез който премахваме вече събраните елементи
#         for i in l:
#             try:s = s + func(i)
#             except:pass
#             else:
#                 f.append(i)
#                 n += 1
#         for i in f:
#             l.remove(i)
#
# def tryex_2(func):
#     # входният параметър func представлява функция, която ще се опитва да обработва пореден елемент от списък
#     # func може да бъде всяка една вградена функция или всяка друга потребителски дефинирана
#     global l,f
#     # l, f, n, s са глобални променливи, т.е. изменяеми в процеса на работата на функцията
#     # l: първоначалния списък
#     # f: списък, съдържащ само елементите, които биха могли да преобразувани в числа
#     if len(l) > 0:
#         for i in l:
#             try:func(i)
#             except:pass
#             else:
#                 l[l.index(i)]='обходено'
#                 # променяме стойността на обходения елемент, с подходяща, така че не се обхожда отново
#                 f.append(func(i))
#     # Функцията натрупва всички елементи числа или техните числени стойности в списъка f
#
# # Прилагаме функцията tryex_1 последователно със float и ord, което променя последователно и l и s и n
# tryex_1(float)
# tryex_1(ord)
# print(l)
# print(s, round(s / n, 2))
#
# # Прилагаме функцията tryex_2 последователно със float и ord, което променя последователно и l и f
# l=[1, 2, 3, '0', 4, 5, '0', 'u', 'jk']
# tryex_2(float)
# tryex_2(ord)
# print(l)
# print(f)
# print(sum(f),round(sum(f)/len(f),2))