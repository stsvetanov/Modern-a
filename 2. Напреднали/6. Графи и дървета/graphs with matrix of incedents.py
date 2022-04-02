# Насочен граф, да се намерят върхове от тип "source" и "sink"
# Работим, като използваме матрица на инцидентност (numpy matrix)
# по редове: върховете - len(vertexes)
# по колони: ребра - len(G)
# 0 ако k-ия възел не участва в l-то ребро
# 1 ако k-я възел е начало на l-то ребро
# -1 ако k-я възел е край на l-то ребро
# сумата по колони винаги е НУЛА
# ако всички елементи от ред са <=0 , то върхът е sink
# ако всички елементи от ред са >=0 , то върхът е source
G=[("A","B"),("A","C"),("B","D"),("C","D"),("B","E"),("F","E")]
# Preprocessing - предварителна обработка (кодиране)
vertexes=set()
for i in G:
    vertexes.add(i[0])
    vertexes.add(i[1])
vertexes=list(vertexes)
nrows=len(vertexes)
ncols=len(G)
dimm=(nrows,ncols)
ribs=list(range(ncols)) # ребра
d=dict()
e=dict()
for i in range(nrows):
    d[vertexes[i]]=i # {"A":0,,,,}
    e[i]=vertexes[i] # {0:"A",,,,}

GG=[]
for i in G:
    GG.append((d[i[0]],d[i[1]]))
# GG=[(2, 0), (2, 1), (0, 3), (1, 3)]
# GG=[(от връх, към връх),,,,]
print(GG)


import numpy as np
matrix=np.zeros(dimm, dtype=int)
# редовете са "връховете"
# колоните са "ребрата", т.е. това са броя на елементите в G и GG

for r in ribs:
    matrix[GG[r][0]][r]=1
    matrix[GG[r][1]][r]=-1

m_sink=matrix<=0
# Проверка за "листа" (sink)
# Проверява всеки един елемент от matrix дали изпълнява условието и
# връща матрица True и False с размера на matrix
m_sink=list(m_sink.all(1))
# ndarray.all(axis): ако axis=1, то проверява по редове дали всички стойности са True,
# ако всички стойности за един ред са True, тогава резултатът за реда е True
m_source=matrix>=0
# Проверка за sources
m_source=list(m_source.all(1))

# От тук надолу няма промяна в скрипта в сравнение с този за матрицата за съседство
sinks,sources=[],[]
for i in range(nrows):
    if m_sink[i]: sinks.append(i)
    if m_source[i]: sources.append(i)
sinks=[e[sink] for sink in sinks]
sources=[e[source] for source in sources]
print("The Sources are: "+str(sources))
print("The Sinks are: "+str(sinks))

# Намерете пътя от А до Е
l=[]
def path(start_node,end_node):
    global l,d,e
    k=-1
    if start_node==end_node:
        l.append(end_node)
        return
    else:
        AB=d[start_node]
        l.append([])
        k=k+1
        rebra=list(matrix[AB]==1)
        rebra=[i for i in range(len(rebra)) if rebra[i]==True]
        # списък с колоните, от които може да се тръгне
        for r in rebra:
            l[k].append(start_node)
            next_node_row_index=list(matrix[:,r]).index(-1)
            next_node=e[next_node_row_index]

            return path(next_node,end_node)
path("A","E")
print(l)
#[[A,B,E],[A,B,D],[A,C,D]]



