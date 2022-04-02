l1=[12,13,14,15,19]
l2=['Ани','Ива', 'Мима', 'Ники','Кирил']
l3=['ГГФ','ФМИ', 'ГГФ','ФЗФ','ГГФ']
l4=[] # помощен списък
for i in l3:
    if i=='ГГФ':l4.append(True)
    else: l4.append(False)

# модифициране на място:
for i in range(len(l4)):
    if not l4[i]: # ако поредният елемент не е True, тогава:
        l1.pop(i)
        l2.pop(i)
        l3.pop(i)
print(l1)
print(l2)
print(l3)
l=[]
for i in range(len(l1)):
    t=(l1[i],l2[i],l3[i])
    l.append(t)
print(l)

# без модифициране:
l1=[12,13,14,15,19]
l2=['Ани','Ива', 'Мима', 'Ники','Кирил']
l3=['ГГФ','ФМИ', 'ГГФ','ФЗФ','ГГФ']

l=[]
for i in range(len(l1)):
    if l3[i]=='ГГФ':
        t=(l1[i],l2[i],l3[i])
        l.append(t)
print(l)

l = [1, 3, 4, 6, 2, 9]
# l2=[]
# for i in l:
#     l2.append(i**2+i+5)
# print(l2)

# for i in range(len(l)):
#     l2.append(l[i] ** 2 + l[i] + 5)
# print(l2)

# l2=[i**2+i+5 for i in l]
# print(l2)

# i,n=0,len(l)
# l2=[]
# while i<n:
#     l2.append(l[i] ** 2 + l[i] + 5)
#     i+=1
# print(l2)