# Да се състави функция, която връща като резултат списък от символни низове.
# Всеки символен низ е с една и съща дължина, която се подава като входен
# параметър при обръщение към функцията. Всеки низ включва само символи,
# които се съдържат в символният низ, подаден като втори аргумент при обръщение към функцията.
# За всеки два елемента s1 , s2 от списъка, връщан като резултат, трябва
# да е изпълнено условието: s1 != s2
# Дължината на списъка, който се връща като резултат, трябва да бъде кратен
# (да се дели без остатък) на цяло число, което се подава като трети аргумент при обръщение към функцията.

def mystring(len_s,s:str,len_l:int):
    import random as rd
    L=[''.join([rd.choice(s) for i in range(len_s)])]
    while len(L)%len_l!=0:
        mys=''.join([rd.choice(s) for i in range(len_s)])
        if mys not in L: L.append(mys)
    return L
every_string=15
s='asdfg'
kratnost=15

res=mystring(every_string,s,kratnost)
print(res)

# Да се направи филтър, който извежда само тези стрингове, които съдържат 'aaa'
myl=lambda x: 'aaa' in x
# myl връща True или False

filtered_res=list(filter(myl,res))
print(filtered_res)

L=['toyota','audi','ford','mercedes','pegeot','nissan','bmw']
N=[20,7,5,30,12,5,4]

# да се изведат всички марки коли, от които в автопарка са налични бройки кратни на 5
car_lambda=lambda x: x%5==0
newN=list(map(car_lambda,N))
newL=[]
for i in range(len(L)):
    if newN[i]:newL.append(L[i])
print(newL)
#*****************************************
p=lambda x: x**2+4*x+4
q=lambda x: x+8
pq=lambda fx,fy: fx==fy
isTrue=lambda x: x==True
X=range(0,101)
# да се намерят всички стойности за x в интервала X, за които p=q

pl=list(map(p,X))
ql=list(map(q,X))
print(pl)
print(ql)
new=[]
res=list(map(pq,pl,ql))
print(res)
for i in range(len(res)):
    if res[i]==True: new.append(i)
print(new)

# Да се напише рекурсивна функция,
# която по зададен аргумент L - списък с брой елементи кратен на 6,
# връща нов двумерен списък M: M[I, J] = L[K], където I, J се
# пресмятат по следния начин: I = K // 6 ; J = K % 6
# t.e. I е броя на подсписъците
# Пример:
#
# [1,2,3,4,5,6,7,8,9,10,11,12] => [[1,2,3,4,5,6],[7,8,9,10,11,12]]

import random as rd
# n=6*rd.randint(0,100)
nl=lambda x: x%6==0
nlist=list(filter(nl,range(0,100)))
n=rd.choice(nlist)
L=list(range(n))
print(L)
sublists=n//6
# M=[]
# k=0
# for i in range(sublists):
#     element=L[k:k+6]
#     M.append(element)
#     k=k+6
# print(M)

P=[]
def myrec(L,n):
   global P
   if not L: return
   else:
       P.append(L[0:n])
       myrec(L[n:],n)

myrec(L,3)
print(P)

P=[[0,0,0,0,0,0] for i in range(sublists)]
# Необходимо условие, за да използваме достъп по индекси и запълване по индекси
# P=[]
def myrec2(L,n):
   global P
   if not L: return
   else:
       I=n % (len(L) // 6)
       J=n // (len(L) // 6)
       P[I][J]=L[n]
       myrec2(L,n-1)

myrec2(L,len(L))
print(P)