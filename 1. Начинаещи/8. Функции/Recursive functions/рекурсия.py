# def arithm_pro_n(a,d,n):
# # n-член от аритметична прогресия
#     if n==1: return a
#     else:
#         return d+arithm_pro_n(a,d,n-1)
#         # return arithm_pro_n(a+d,d,n-1)
# print("n-ти член на аритметична прогресия: " +str(arithm_pro_n(1,3,6)))
#
# def arithm_pro_sum(a,d,n):
# # сума на числата от аритметична прогресия
#     if n==0: return 0 # return 0, защото имаме сумиране, и първия елемент при сумиране с натрупване е винаги 0
#     else:
#         return a+arithm_pro_sum(a+d,d,n-1)
# print("Сума член на аритметична прогресия: " +str(arithm_pro_sum(1,3,6)))
#
# def arithm_pro_multiply(a,d,n):
# # произведение на числата от аритметична прогресия
# #     if n==1: return a
#     if n==0: return 1 # return 1, защото имаме умножение, и първия елемент при умножение с натрупване е винаги 1-ца
#     else:
#         return a*arithm_pro_multiply(a+d,d,n-1)
# print("Произведение на аритметична прогресия: " +str(arithm_pro_multiply(1,3,6)))
#
# def geo_pro_n(a,q,n):
# # n-член от геометрична прогресия
#     if n==1: return a
#     else:
#         # return geo_pro_n(a*q,q,n-1)
#         return q*geo_pro_n(a,q,n-1)
# print("n-ти член на геометрична прогресия: " +str(geo_pro_n(1,3,6)))
#
# def geo_pro_sum(a,q,n):
# # сума на числата от геометрична прогресия
#     if n==1: return a
#     else:
#         # return a*q**(n-1)+geo_pro_sum(a,q,n-1)
#         return a + geo_pro_sum(a*q, q, n - 1)
#
# print("Сума на геометрична прогресия: " +str(geo_pro_sum(2,3,6)))
#
# def geo_pro_multiply(a,q,n):
# # произведение на числата от геометрична прогресия
#     if n==1: return a
#     else:
#         # return a*q**(n-1)*geo_pro_multiply(a,q,n-1)
#         return a*geo_pro_multiply(a*q,q,n-1)
#
# print("произведение на геометрична прогресия: " +str(geo_pro_multiply(2,3,3)))

# def rec_list_sum(L):
#     if not L: # L се скъсява на всяко ниво на рекурсия
#         return 0
#     else:
#         return L[0] + rec_list_sum(L[1:])
# print("Сума на числа от списък: "+str(rec_list_sum([1,4,7,10,13,16])))
#
# def power(k,n):
# # Лекция 10, слайд 28
#   if n==1:
#     return k
#   else:
#     return k * power(k,n-1)
# k=4
# n=3
# print(str(k)+" на "+str(3)+"-та степен: "+str(power(k,n)))
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
# print("Броят на елементите е: "+str(len_deep(([1, 5, [2, [3, 4]]]))))
#
# def fibonacci(n):
#    if n==1: return 0
#    elif n==2: return 1
#    else:
#       return fibonacci(n-1) + fibonacci(n-2)
# print("Числото на Фибоначи с позиция n="+str(8)+" e: "+str(fibonacci(8)))
#
#
# def fib_2(n):
#     # добавя 10 числа на Фибоначи към споисъка L
#     global L
#     if n<=0:
#         return L
#     else:
#         L.append(sum(L[-2:]))
#         return fib_2(n-1)
# L = [0, 1]
# F=fib_2(10)
# print("Числата на Фибоначи са: ", F)

#
# def isPalindrome(s):
#     def toChars(s):
#       s = s.lower()
#       ans = ''
#       for c	in s:
#         if c in 'abcdefghijklmnopqrstuvwxyz':
#           ans = ans + c
#       return ans
#     # s='Acds1dca'
#     # toChars(s):
#     # - s='acds1dca'
#     # - s='acdsdca'
#     def isPal(s):
#         global br
#         if len(s) <= 1: return True
#         else:
#             condition=s[0] == s[-1] and isPal(s[1:-1])
#             if condition:
#                 br+=1
#                 return condition
#             else:
#                 br+=1
#                 print(br-1)
#                 return False
#         # return s[0] == s[-1] and isPal(s[1:-1])
#     return isPal(toChars(s))
# br=0 #служи за отпечатване на позицията, в която текстът престава да бъде палиндром
# print("Палиндром ли е: "+str(isPalindrome('Aces1dca')))


# Да се намери чрез рекурсия k! и да се намери сумата от всички числа k! , за които k=[1;n]
def fact(k):
    if k==1: return 1
    else:
        return k*fact(k-1)
print(fact(4))

def fact_sum(k):
    s=0
    L=list(range(1,k+1))
    for l in L:
        s+=fact(l)
    return s
print(fact_sum(4))


k=4
L=list(range(1,k+1))
def fact_sum_2(L):
    if not L: return 0
    else:
        return fact(L[0])+fact_sum_2(L[1:])
print(fact_sum_2(L))

def fact_sum_3(L):
    def fact(k):
        if k == 1:
            return 1
        else:
            return k * fact(k - 1)

    if not L: return 0
    else:
        return fact(L[0])+fact_sum_3(L[1:])
print(fact_sum_3(L))