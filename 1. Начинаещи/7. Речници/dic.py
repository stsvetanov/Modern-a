# Упражнение от 18.03.2020 върху речници

# s_1=input('Списък 1 (разделител ,): ')
# s_2=input('Списък 1 (разделител ,): ')
# s_1=s_1.split(',') # резултатът от сплитването винаги е списък
# s_2=s_2.split(',')

# Създаване на речници, въз основата на два списъка
def dict_zip(s_1,s_2):

    d_1=dict(zip(s_1,s_2))
    print('Речник със zip: ',d_1)
    return d_1
def dict_update(s_1,s_2):
    d_2={}
    for i in range(len(s_1)):
        d_2.update({s_1[i]:s_2[i]})
    #   d.update({key:val})
    print('Речник със update: ',d_2)
    return d_2
def dict_brakets(s_1,s_2):
    d_3 = {}
    for i in range(len(s_1)):
        d_3[s_1[i]]= s_2[i]
    print('Речник със скоби и достъп до ключа: ', d_3)
    return d_3
def dict_for(s_1,s_2):
    d_4={int(s_1[i]):int(s_2[i]) for i in range(len(s_1))}
    return d_4

# d1=dict_zip(s_1,s_2)
# d2=dict_update(s_1,s_2)
# d3=dict_brakets(s_1,s_2)
# d4=dict_for(s_1,s_2)

def zad_1(dic):
# зад 1: Ако стойността за определен ключ е X (сами избирате),
# то тя да бъде променена на Y

    s=input('Въведи ключ за проверка: ')
    if s in dic: # проверява дали в речник има ключ, който да се казва като стойността на s
        dic[s]='Changed'
    print(dic)
    return dic

def zad_2_v1(dic):
# зад 2: Ако съществува ключ X, то той да бъде преименуван на Y, но да се запази стойността му
    s1=input('Въведи ключ за проверка: ')
    s2=input('Въведи нов ключ: ')
    if s1 in dic:
        dic[s2]=dic.pop(s1)
        # 1. създаваме ключ s2
        # 2. присвояваме стойност за s2, равна на стойността за s1
        # 3. изтриваме двойката ключ=s1 и стойност за s1
        # .pop(key)
    print(dic)
    return dic

def zad_2_v2(dic):
# зад 2: Ако съществува ключ X, то той да бъде преименуван на Y, но да се запази стойността му
    s1 = input('Въведи ключ за проверка: ')
    s2 = input('Въведи нов ключ: ')
    if s1 in dic:
        dic[s2] = dic[s1]
        dic.pop(s1)
    print(dic)
    return dic

def zad_3_v1(dic):
# zad.3 Сортирайте речника спрямо имената на ключовете
#     d1_sbk={}
    k=list(dic.keys())
    k.sort()
    # for i in k:
    #     d1_sbk.update({i:dic[i]})
    # Alternativno:
    d1_sbk={i:dic[i] for i in k}
    print(d1_sbk)
    return d1_sbk

def zad_3_v1(dic):
# алтернативен вариант:

    d=dict(sorted(dic.items()))
    # dic.items() връща двойките ключ-стойност
    # sortted() ги подрежда по ключа
    # dict() превръща списъка от наредени двойки ключ-стойност отново в речник
    print('Първоначален вариант на речника: ',dic)
    print('Сортиран вариант на речника: ', d)
    return d

def zad_4_v1(l):
# Задача 4: Разполагате с един списък с повтарящи се елементи.
# Да се напише програма, която преброява колко пъти се
# среща всеки елемент в списъка, а резултатът да се оформи като речник.

    s=input('Списък от думи (разделител ,): ')
    L=s.split(',')
    # пример: L=['ime', 'ime', 'name', 'imeto', 'name']
    D=dict() # Създаден празен речник
    for i in L:
        if(i in D):
            D[i]+=1
        else:
            D[i]=1
    # В този цикъл i е поредният елемент от L
    # D е празен речник, не съдържа нито ключове, нито стойности за тях.
    # Ако i го няма като ключ в D, то той се създава и приема стойност 1 (това е else клаузата)
    # Ако i е намерено като ключ в D, то се добавя към стойността за него 1-ца
    print(D)
    return D

def zad_4_v2(l):
# Друг вариант
    s=input('Списък от думи (разделител ,): ')
    L=s.split(',')
    # пример: L=['ime', 'ime', 'name', 'imeto', 'name']

    L_as_set=set(L) # превръща списъка в множество, т.е. маха дублиранията
    L_as_list=list(L_as_set) # превръща множеството отново в списък,
                             # защото елементите на множествата не могат
                             # да бъдат достъпвани чрез индекс
    D={} # Създаден празен речник
    for i in L_as_list:
        # i приема стойности измежду неповтарящите се елементи на списъка
        co=L.count(i) # преброява срещанията на i във L
        D.update({i:co}) # добавя нова двойка ключ-стойност към речника D
    print(D)
    return D
def zad_5_swap(dic):
    # обръща ключовете като стойности и стойностите като ключове
    keys=dic.keys()
    vals=dic.values()
    newdic=dict(zip(vals,keys))
    return newdic

def zad_6_matrix():
    from random import randint
    n=randint(5,10)
    matrix=[]
    for r in range(n):
        matrix.append([])
        for c in range(n):
            matrix[r].append(randint(0,100))

        # print(matrix[r][c])


# стартирането на функциите се осъществява като изпишем името
# на функцията и подадем аргументите (ако има такива) в кръгли скоби:
# zad_6_matrix()
# d1=dict_zip(s_1,s_2)

# пример със def zad_5_swap(dic):
d={2:'a',3:'b',5:'c',7:'d',11:'e'}
print(zad_5_swap(d))