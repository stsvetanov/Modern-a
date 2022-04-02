import random as rd
from functools import reduce
L=[rd.randint(1,25) for i in range(10)]
print('L: ', L)

l1=lambda x: x**2+4*x+4
l2=lambda x: x**3+x**2-10*x-8
l3=lambda x: (x+5)**2-(x-5)**2
l4=lambda x: (x%3)**x
lhelp=lambda a,b: a+b

M1=list(map(l1,L))
M1f=list(filter(lambda x:x<100,M1))
D=dict(zip(L,M1))
M3=reduce(lhelp,M1)

D_2={}
D_2[True]=list(filter(lambda x:x<25,M1))
D_2[False]=list(filter(lambda x:x>=25,M1))

print('M1: ',M1)
print('M1f: ',M1f)
print('D: ',D)
print('M3: ',M3)
print('D_2',D_2)