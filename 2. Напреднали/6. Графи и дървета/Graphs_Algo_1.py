# rebro=(възел А, възел Б, стойност)
r1=(1,5,80)
r2=(1,6,54)
r3=(1,3,47)
r4=(3,5,23) #*
r5=(3,6,75)
r6=(3,2,55) #*
r7=(3,4,88)
r8=(3,7,66)
r9=(5,7,93)
r10=(6,4,74)
r11=(2,4,31)
r12=(2,8,79)
r13=(2,7,74)
r14=(4,8,29)
r15=(7,8,68)
r16=(5,2,32) #*
n=8 #брой възли в графа

# проверка за цикъл: дали съществуват в пътя двата възела от реброто
G=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]


def KRUSKA(G):
    #minimum path KRUSKA
    g0 = set([g[0] for g in G])  # v (от)
    g1 = set([g[1] for g in G])  # w (към)
    v=g0.union(g1) #всички върхове
    n=len(v)
    g2 = [g[2] for g in G]  # това са теглата на пътя
    path=[]
    t=[] # списък с тегловите коефициенти за сумиране
    ver=[]
    while len(path)<n-1:
        minimum=min(g2)
        index=g2.index(minimum)
        rebro=G[index]
        cond_1 = ver.count(rebro[0])>=2
        cond_2 = ver.count(rebro[1])>=2
        cirle=cond_1 and cond_2
        if cirle==True:
            G.pop(index)
        else:
            path.append(G.pop(index))
            g2.pop(index)
            t.append(rebro[2])
            ver.append(rebro[0])
            ver.append(rebro[1])
    return [path,sum(t)]

# kruska=KRUSKA(G)
# print(kruska[0])
# print(kruska[1])

def PRIM(G):
    # minimum path PRIM
    g0 = set([g[0] for g in G])  # v (от)
    g1 = set([g[1] for g in G])  # w (към)
    v = list(g0.union(g1))  # всички върхове
    n = len(v) # брой на върховете
    path = [] # нареден списък с ребрата
    t = []  # списък с тегловите коефициенти за сумиране
    T=[v[0]] # Т го инициализираме с който и да е от върховете (може и на случаен принцип)
    E=[r for r in G if (v[0] == r[0]) or (v[0] == r[1])]
    # Във Е натрупваме всички ребра, в които участва изследвания връх
    while len(path) < n:
        g2 = [e[2] for e in E]  # това са теглата на пътя за ребрата в E
        minimum = min(g2) # намираме минималното тегло
        index = g2.index(minimum) # извличаме индекса на минималното тегло
        rebro = E[index] # по индекса намираме съответното ребро в E
        GE = list(set(G) - set(E)) # на всяка стъпка премахваме от G онези ребра, които са влезли в E
        path.append(E.pop(index)) # едва тогава махаме реброто с минимална оценка и го слагаме в path
        if rebro[1] in T: # изследваме втория възел от всяко ребро дали е в Т или не:
            pass
        else:
            T.append(rebro[1])
            e_ext=[] # празен помощен списък от ребра
            for r in GE: # за всяко ребро r в GE проверяваме дали съдържа възелът, който изследваме (rebro[1])
                condition=(rebro[1] == r[0]) or (rebro[1] == r[1])
                if condition: e_ext.append(r) # ако е така, то тези ребра ги натрупваме в помощния списък

            E.extend(e_ext) # увеличаваме списъка с ребрата с този от помощния списък
            E=list(set(E)) # за да се избегне дублиране правим конвертиране към множество, и след това обратно в списък
            t.append(minimum) # към списъка с теглата добавяме намерения минимум
    return([T,path,sum(t)])
# print(PRIM(G))



# насочен претеглен граф: (v1,v2,cost)
# v1 е възел който сочи към възел v2, със стойност cost
# True когато възел 1 не е посетен
r1=("A","B",2)
r2=("A","D",1)
r3=("B","D",3)
r4=("B","E",10)
r5=("D","E",2)
r6=("E","G",6)
r7=("D","G",4)
r8=("G","F",1)
r9=("D","F",8)
r10=("C","F",5)
r11=("D","C",2)
r12=("C","A",4)
R=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]

def Dijkstra(v1,v2,G):
    vertex = list(set([r[0] for r in G]).union(set([r[1] for r in G])))
    vertex={v:True for v in vertex} # ако възелът не е посетен е True
    if v1 in vertex and v2 in vertex:
        cost=0
        pqueue={v1:cost}
        r2list=[r[1] for r in G if r[0]==v1]
        while v2!=r2:
            for r2 in r2list:
                


    print(vertex)
    return