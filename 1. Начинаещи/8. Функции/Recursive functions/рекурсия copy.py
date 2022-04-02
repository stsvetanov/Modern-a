# def arithm_pro_n(a,d,n):
# # n-член от аритметична прогресия
#     if n==1: return a
#     else:
#         return d+arithm_pro_n(a,d,n-1)
# print("n-ти член на аритметична прогресия: " +str(arithm_pro_n(1,2,5)))
#
# def arithm_pro_sum(a,d,n):
# # сума на числата от аритметична прогресия
#     if n==0: return 0
#     else:
#         return a+arithm_pro_sum(a+d,d,n-1)
# print("Сума член на аритметична прогресия: " +str(arithm_pro_sum(1,2,5)))
#
# def arithm_pro_multiply(a,d,n):
# # произведение на числата от аритметична прогресия
#     if n==1: return a
#     else:
#         return a*arithm_pro_multiply(a+d,d,n-1)
# print("Произведение на аритметична прогресия: " +str(arithm_pro_multiply(1,2,5)))
#
# def geo_pro_n(a,q,n):
# # n-член от геометрична прогресия
#     if n==1: return a
#     else:
#         return geo_pro_n(a*q,q,n-1)
# print("n-ти член на геометрична прогресия: " +str(geo_pro_n(1,2,5)))
#
# def geo_pro_sum(a,q,n):
# # сума на числата от геометрична прогресия
#     if n==1: return a
#     else:
#         return a*q**(n-1)+geo_pro_sum(a,q,n-1)
# print("Сума на геометрична прогресия: " +str(geo_pro_sum(3,2,5)))
#
# def geo_pro_multiply(a,q,n):
# # произведение на числата от геометрична прогресия
#     if n==1: return a
#     else:
#         return a*q**(n-1)*geo_pro_multiply(a,q,n-1)
# print("произведение на геометрична прогресия: " +str(geo_pro_multiply(1,2,5)))
#
# def rec_list_sum(L):
#
#     if not L: # L се скъсява на всяко ниво на рекурсия
#         return 0
#     else:
#         return L[0] + rec_list_sum(L[1:])
# print("Сума на числа от списък: "+str(rec_list_sum([1, 2, 3, 4, 5])))
#
# def rec_list_power(L):
#
#     if not L: # L се скъсява на всяко ниво на рекурсия
#         return 1
#     else:
#         return L[0] * rec_list_power(L[1:])
# print("Произведение на числа от списък: "+str(rec_list_power([1, 2, 3, 4, 5])))
#
# def power(n):
# # Лекция 10, слайд 28
#   if n==0:
#     return 1
#   else:
#     return 2 ** power(n-1)
# print("2 на 3-та степен: "+str(power(3)))
# # n=5: 2** [n=4: 2** [n=3: 2** [n=2: 2** [n=1: 2]]]]
#
# def len_deep(spis):
#   # Брой на елементите в списък със под-списъци
#   if not spis: return 0
#   else:
#     for elem in spis:
#       if not isinstance(elem,list):
#         return len_deep(spis[1:]) + 1
#       else:
#         return len_deep(elem)+len_deep(spis[1:])
# print("Броят на елементите е: "+str(len_deep(([1, [2, [3, 4]]]))))
#
# def fibonacci(n):
#    if n==0: return 0
#    elif n==1: return 1
#    else:
#       return fibonacci(n-1) + fibonacci(n-2)
# k=6
# print("Числото на Фибоначи с позиция n="+str(k+1)+" e: "+str(fibonacci(k)))
#
# def isPalindrome(s):
#     def toChars(s):
#       s = s.lower()
#       ans = ''
#       for c	in s:
#         if c	in 'abcdefghijklmnopqrstuvwxyz':
#           ans = ans + c
#       # Трябва да върне изчистен стринг от други символи
#       return ans
#     def isPal(s):
#       if len(s) <= 1: return True
#       else:
#         return s[0] == s[-1] and isPal(s[1:-1])
#     return isPal(toChars(s))
# print("Палиндром ли е: "+str(isPalindrome("1234321")))

# По зададено n>0, намерете n-я елемент от редицата:
# (1) a(1) = 3, a(2) = 7, a(n+2) - 4*a(n+1) + 4*a(n) = 0
# (2) a(1) = 1, a(n+1) + a(n) = 2**n
# (3) a(1) = 1,  a(2) = 2, a(n+2) - 2*a(n+1) + a(n) = 0

def red_1(n,d):
    # a[n + 2] - 4 * a[n + 1] + 4 * a[n] = 0
    # a[n]=4*a[n-1]-4*a[n-2]
    if n in d:
        return d[n]
    else:
        ans = 4*(red_1(n - 1, d) - red_1(n - 2, d))
        d[n] = ans
    return ans
d = {1:3, 2:7}
print(red_1(5,d))
print(d)
# 3,7,16,36,80

def red_2(n,d):
    # a(n+1) + a(n) = 2**n
    # a[n-1]=2**(n-1) - a[n]
    # a[n]=2**(n-1)-a[n-1]
    if n in d:
        return d[n]
    else:
        ans = 2**(n-1) - red_2(n - 1, d)
        d[n] = ans
    return ans
d = {1:1}
print(red_2(5,d))
print(d)
# 1,1,3,5,11

def red_3(n,d):
    # a[n+2] - 2*a[n+1] + a[n] = 0
    # a[n]-2*a[n-1]+a[n-2]=0
    # a[n]=2*a[n-1]-a[n-2]
    if n in d:
        return d[n]
    else:
        ans = 2*red_3(n - 1, d) - red_3(n - 2, d)
        d[n] = ans
    return ans
d = {1:1,2:2}
print(red_3(5,d))
print(d)
# 1,2,3,4,5,6...

# Намерете стойността на g(N) за цяло число N, въведено от клавиатурата и N>10000, ако:
#
# За фиксирано реално число а>1 е зададена функцията f:
# 1. f(x, a) = 1 при x < a
# 2. f(x, a) = f(x-1, a) + f(x-a, a) при x >= a

def red_4(n,d):

