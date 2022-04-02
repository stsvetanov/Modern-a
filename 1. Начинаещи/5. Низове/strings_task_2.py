import random as rd
k=rd.randint(1,35)
print("Броят на елементите на списъка е: "+str(k))
l=[]
for i in range(k):
    l.append(rd.randint(1,20))
print(l)
##for i in range(1,21):
##    txt="%s: %d" %(i,l.count(i))
##    if l.count(i)>0:
##        print(txt)
##    if l.count(i)>1: p=i #След края на цикъла p ще бъде последният повтарящ се повече от веднъж елемент
##    
###Ако едно число се среща повече от веднъж в списъка, то всички срещания в списъка да бъдат изтрити
##number=rd.randint(0,len(l))
##n=l[number]
##print(n)
##nc=l.count(n)
##while l.count(n)>1:
##    l.remove(n)
##if nc!=l.count(n): l.remove(n)
##print(l)
###Ако едно число се среща повече от веднъж в списъка, то оставете само последното му срещане в списъка
##number=rd.randint(0,len(l))
##n=l[number]
##print(n)
##while l.count(n)>1:
##    l.remove(n)
##print(l)
###Ако едно число се среща повече от веднъж в списъка, то оставете само първото му срещане в списъка
##l.reverse()
##number=rd.randint(0,len(l))
##n=l[number]
##print(n)
##while l.count(n)>1:
##    l.remove(n)
##l.reverse()
##print(l)
        
#Да се намерят индексите на последния повтарящ се елемент
##for i in range(0,len(l)):  
##    if l[i]==p: print(i)
a=list(range(1,21))
b=[]
for i in range(1,21):
    b.append(l.count(i))
for i in range(20,0,-1):
    if b[i]<=1:
        a.pop(i)
        b.pop(i)
freq=zip(a,b)
for i in freq: print(i)
