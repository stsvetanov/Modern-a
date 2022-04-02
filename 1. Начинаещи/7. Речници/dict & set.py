# dict & set

# 3 множества от по 10 случайни числа, в интервала [1;20]
# списък от речници, всеки речник със следния формат:
# a,b,c,isTri,is3,is2,is90,P,S

import random as rd

n=10
min=1
max=20
def make_random_set(n,min,max):
    my_set=set()
    i=0
    while (i<n):
        l=len(my_set)
        my_set.add(rd.randint(min,max))
        if l<len(my_set): i+=1
    return my_set

a=list(make_random_set(n,min,max))
b=list(make_random_set(n,min,max))
c=list(make_random_set(n,min,max))

def isTri(a1,a2,a3):
    b=False
    cond_1 = a1 + a2 > a3
    cond_2 = a1 + a3 > a2
    cond_3 = a3 + a2 > a1
    if cond_1&cond_2&cond_3: b=True
    return b

def is3(a1, a2, a3):
    b = False
    cond=a1 == a2==a3
    if cond: b=True
    return b

def is2(a1, a2, a3):
    b = False
    cond_1 = a1 == a3
    cond_2 = a1 == a2
    cond_3 = a3 == a2
    if cond_1 | cond_2 | cond_3: b = True
    return b

def is90(a1, a2, a3):
    b = False
    cond_1 = a1 ** 2 + a2 ** 2 == a3 ** 2
    cond_2 = a1 ** 2 == a2 ** 2 + a3 ** 2
    cond_3 = a1 ** 2 + a3 ** 2==a2 ** 2
    if cond_1|cond_2|cond_3: b=True
    return b

def P(a1, a2, a3):
    p=a1+a2+a3
    return p

def S(a1, a2, a3):
    p=P(a1,a2,a3)/2
    s=p*(p-a1)*(p-a2)*(p-a3)
    s=round(s**(1/2),2)
    return s


def is3_2(a1, a2, a3):
    b = None
    if isTri(a1,a2,a3):
        cond=a1 == a2==a3
        if cond: b=True
        else: b=False
    return b

def is2_2(a1, a2, a3):
    b = None
    if isTri(a1,a2,a3):
        cond_1 = a1 == a3
        cond_2 = a1 == a2
        cond_3 = a3 == a2
        if cond_1 | cond_2 | cond_3: b = True
        else:
            b = False
    return b

def is90_2(a1, a2, a3):
    b = None
    if isTri(a1,a2,a3):
        cond_1 = a1 ** 2 + a2 ** 2 == a3 ** 2
        cond_2 = a1 ** 2 == a2 ** 2 + a3 ** 2
        cond_3 = a1 ** 2 + a3 ** 2==a2 ** 2
        if cond_1|cond_2|cond_3: b=True
        else:
            b = False
    return b

def P_2(a1, a2, a3):
    p=None
    if isTri(a1,a2,a3): p=a1+a2+a3
    return p

def S_2(a1, a2, a3):
    s=None
    if isTri(a1,a2,a3):
        p=P(a1,a2,a3)/2
        s=p*(p-a1)*(p-a2)*(p-a3)
        s=round(s**(1/2),2)
    return s

# ldict=[]
# for i in range(n):
#     dkeys = ["a", "b", "c", "isTri", "is3", "is2", "is90", "P", "S"]
#     d = dict.fromkeys(dkeys)
#     d['a']=a[i]
#     d['b']=b[i]
#     d['c']=c[i]
#     d['isTri']=isTri(a[i],b[i],c[i])
#     if d['isTri']:
#         d['is3']=is3(a[i],b[i],c[i])
#         d['is2']=is2(a[i],b[i],c[i])
#         d['is90']=is90(a[i],b[i],c[i])
#         d['P']=P(a[i],b[i],c[i])
#         d['S']=S(a[i],b[i],c[i])
#     ldict.append(d)

ldict2=[]
for i in range(n):
    dkeys = ["a", "b", "c", "isTri", "is3", "is2", "is90", "P", "S"]
    dvalues=[a[i],b[i],c[i],isTri(a[i],b[i],c[i]),is3_2(a[i],b[i],c[i]),is2_2(a[i],b[i],c[i]),is90_2(a[i],b[i],c[i]),P_2(a[i],b[i],c[i]),S_2(a[i],b[i],c[i])]
    d=dict(zip(dkeys,dvalues))
    ldict2.append(d)
# print('Вариант 1:')
# for k in ldict:
#     print(k)

print('Вариант 2:')
for k in ldict2:
    print(k)

# import pandas as pd
# import xlwt
# df=pd.DataFrame(ldict)
# df.to_excel('my_data.xls')

# task_1: Да се изчистят всички речници от списъка, за които isTrue=False
# task_2: Да се изведат всички равностранни триъгълници от списъка
# task_3: Да се изведат всички тръгълници с лице по-голямо от 45

# task_1
l=len(ldict2)
for i in ldict2:
    if i['isTri']==False:
        ldict2.remove(i)
print('Премахнати са %d реда от списъка, които не образуват триъгълници' %(l-len(ldict2)))
print(len(ldict2))

# task_2
te="Равностранните триъгълници са:"
tri3=[]
for i in ldict2:
    if i['is3']:tri3.append(i)
if len(tri3)==0:
    print(te+' 0')
else:
    print(te + str(len(tri3)))
    for i in tri3:
        print(i)

# task_3
te="Равностранните триъгълници са:"
tri45=[]
for i in ldict2:
    if i['S']>45:tri45.append(i)
if len(tri45)==0:
    print(te+' 0')
else:
    print(te + str(len(tri45)))
    for i in tri45:
        print(i)