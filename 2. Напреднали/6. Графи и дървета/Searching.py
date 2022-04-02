def parent(mytree:list,node):
    # Претърсването е в postorder
    while True:
        for t in mytree:
            if node[0] == t[1]: return t[0]
            elif node[0]==t[2]: node=t
# print(parent(tree,K))

def secchield(mytree:list,parent):
    # Претърсването е в preorder
    for t in mytree:
        if parent[1]==t[0] and t[2]!="":
            return t[2]
        elif parent[1]==t[0] and t[2]=="":
            return "Няма второ дете"

R1=["A","B",True]
R2=["A","C",True]
R3=["A","D",True]
R4=["B","E",True]
R5=["B","F",True]
R6=["B","G",True]
R7=["E","J",True]
R8=["E","K",True]
R9=["D","H",True]
R10=["D","I",True]
R11=["H","L",True]
# V=("A","B","C","D","E","F","G","H","I","K","L","J")
# Алгоритъм за топологично търсене - намира всички родители
# Проверка за 0 входящи ребра в конкретен възел:

# graf=[R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11]
# graf_0=[]
# graf_1=[]
# path=[]
# V=set()
# for r in graf:
#     V.add(r[0])
#     V.add(r[1])
#     graf_0.append(r[0])
#     graf_1.append(r[1])
# print(V)
# V=list(V)
# for v in V:
#     if v not in graf_1:
#         path.append(v)
#         #graf_1.remove(v)
#         for g in graf:
#             if g[2]==True and g[0]==v:
#                 g[2]=False
#                 # graf_1.
#         graf_1=[]
#         for r in graf:
#             if r[2]==True: graf_1.append(r[1])
#     print(v)
#     print(graf)
#     print(graf_1)
# print(path)


# Топлогична подребра в свързан граф
J=("J","","K")
E=("E","J","F")
F=("F","","G")
G=("G","","")
B=("B","E","C")
C=("C","","D")
D=("D","H","")
H=("H","L","I")
L=("L","","")
A=("A","B","")
K=("K","","")
I=("I","","")
tree=[K,J,E,F,G,B,A,C,D,H,I,L]
# всяко листо на позиция 1 е ""
V=set()
for r in tree:
    if r[0]!="":V.add(r[0])
    if r[1]!="":V.add(r[1])
    if r[2]!="":V.add(r[2])

path=[]

# търсим ребра, в които възелът се намира на позиция 1: това родител-наследник
# търсим ребра, в които възелът се намира на позиция 2: това брат-сестра
n=len(tree)
while n>0:
    sink = [r[0] for r in tree if r[1] == ""]
    path.append(sink)
    tr=set([r for r in tree if r[0] in sink])
    tree = list(set(tree) - tr)
    for i in range(len(tree)):
        if tree[i][1] in sink:
            k=list(tree[i])
            k[1]=""
            tree[i]=tuple(k)
        if tree[i][2] in sink:
            k = list(tree[i])
            k[2] = ""
            r = tuple(k)
    # print(tree)
    n=len(tree)
    # print(n)
print(tree)
# path.append(tree[0][0])
path=path[::-1]
print(path)
# [J,K,L,I,F,G,C]
# [E,H]
# [B,D]
# [A]*