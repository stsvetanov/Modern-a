# Насочен граф, да се намерят върхове от тип "source" и "sink"
# Работим, като използваме матрица на съседство (numpy matrix)
G=[("A","B"),("A","C"),("B","D"),("C","D"),("B","E"),("F","E")]
# Preprocessing - предварителна обработка (кодиране)
vertexes=set()
for i in G:
    vertexes.add(i[0])
    vertexes.add(i[1])
vertexes=list(vertexes)
n=len(vertexes)
d=dict()
e=dict()
for i in range(n):
    d[vertexes[i]]=i # {"A":0,,,,}
    e[i]=vertexes[i] # {0:"A",,,,}

GG=[]
for i in G:
    GG.append((d[i[0]],d[i[1]]))
# GG=[(2, 0), (2, 1), (0, 3), (1, 3)]
# GG=[(от връх, към връх),,,,]
# print(GG)

# решение чрез използване на матрица
# условие за source: сума по колони=0
# условие за sink: сума по редове=0

import numpy as np
matrix=np.zeros((n,n), dtype=int)
# редовете са "ОТ връх"
# колоните са "КЪМ връх"
for i in GG:
    matrix[i[0]][i[1]]=1
sums_by_rows=matrix.sum(1)
sums_by_cols=matrix.sum(0)
# print(matrix)
# print(sums_by_rows) #[1,0,2,1]
# print(sums_by_cols) #[1,2,0,1]
# sums_by_rows=list(sums_by_rows)
# sink=sums_by_rows.index(0)
# sums_by_cols=list(sums_by_cols)
# source=sums_by_cols.index(0)
# sink=e[sink]
# source=e[source]
# print("The Source is: "+source)
# print("The Sink is: "+sink)

# Това беше вариант на задачата при условие, че разполагаме само с един source и един sink
sums_by_rows=list(sums_by_rows)
sums_by_cols=list(sums_by_cols)
n=len(sums_by_cols)
sinks,sources=[],[]
for i in range(n):
    if sums_by_rows[i]==0: sinks.append(i)
    if sums_by_cols[i]==0: sources.append(i)
sinks=[e[sink] for sink in sinks]
sources=[e[source] for source in sources]
print("The Sources are: "+str(sources))
print("The Sinks are: "+str(sinks))


