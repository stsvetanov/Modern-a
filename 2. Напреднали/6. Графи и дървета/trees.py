#l=[A[C,B[D,F,E[G[H,I]]]]]

# какво е I?
# ако I няма родител => e корен
# ако I няма наследници => e листо
# ако I има наследници => е родител

# да се намерят всички листа (и колко са)
# да се намерят всички родители (и колко са)
# да се намери корена на дървото (нулевата позиция)

A=[5,[1,2,[[3,4]]]]
# каква е височината на дървото или дълбочината на списъка
# (това е и броя на родителите)?
# броя на отварящите скоби (или затварящите) е дълбочината
# броят на запетаите + 1 (заради представянето на корена) е броя на листата
def treee_leafs(spis):
  # Брой на елементите в списък със под-списъци
  if not spis: return 0
  else:
    for elem in spis:
      if not isinstance(elem,list):
        return treee_leafs(spis[1:]) + 1
      else:
        return treee_leafs(elem)+treee_leafs(spis[1:])
# print("Броят на листата в дървото е: "+str(treee_leafs(A)))

def treee_parents(spis):
  # Брой на елементите в списък със под-списъци
  if not spis: return 1
  else:
    for elem in spis:
      if isinstance(elem,list):
          return treee_parents(spis[1:]) + 1
# print("Броят на родителите в дървото е: "+str(treee_parents(A)))
# print("Броят на всички възли в дървото е: "+str(treee_parents(A)+treee_leafs(A)+1))

# A=[B,C,D]
# B=[E,F,G]
# E=[J,K]
# D=[H,I]
# H=[L]
# A=[[[J,K],F,G],C,[[L],I]]

l_1="A[C,B[D,F,E[G[H,I]]]]"
l_2="A[B[E[J,K],F,G],C,D[H[L],I]]"
# да се намери височината на дървото
# колко е броя на родителите, а на листата ?
# s=l_2.split("[")
# print(s)
# print(len(s)-1) # брой родители, включително корена
# s=l_2.split(",")
# print(s)
# print(len(s)) # брой листа
# ако след буквата има отваряща скоба => буквата е родител
# ако след буквата има запетая или затваряща скоба =>листо
# дали индекса е нула
def whatitis(tree,s):
    position=tree.find(s)
    if position==-1: tex="Няма такъв елемент в дървото"
    elif position==0:tex=s+" е корен в дървото"
    elif tree[position+1]=="[": tex=s+" е родител (вътрешен възел) в дървото"
    elif tree[position+1]=="," or tree[position+1]=="]": tex=s+" е листо (външен възел) в дървото"
    return tex
# print(l_2)
#
# for s in l_2:
#     if s!="[" and s!="]" and s!=",":
#         print(whatitis(l_2,s))

# Вариант 2 – двоично дърво: данни, указател към наследници, указател към братя и сестри
# Node=(data,child,bro_sis)
# Node=(data,"","") - листо без братя и сестри от дясно
# Node=(data,"",bro_sis) - листо със братя и сестри от дясно
# Node=(data,child,"") - родител без братя и сестри от дясно
# Коренът не може да бъде открит в индексите 1 и 2 на върховете !
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
# Дървото в този случай е представено като списък от неподредени възли

# Да се намери корена на дървото
# Да се намери родителят на L
# Да се намери второто дете на B
# ne, eq, all, any

def rootis(mytree:list):
    # без обхождане !!!
    l1=[pos[1] for pos in mytree]
    l2=[pos[2] for pos in mytree]
    l0=[pos[0] for pos in mytree]
    root=set(l0)-set(l1+l2)
    root=list(root)
    return root[0]


def path_from_node_to_root(mytree:list,node):
    # Претърсването е в postorder
    root=rootis(mytree)
    path=-1
    parents=[]
    while node[0]!=root:
        for t in mytree:
            if node[0]==t[1] or node[0]==t[2]:
                parents.append(t[0])
                path+=1
                node = t
    return [path,parents]
# print(path_from_node_to_root(tree,H))

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
# print(secchield(tree,A))
# print(secchield(tree,I))

# Претърсване на дърво в дълбочина:
#   От горе надолу (Preorder)
#   От долу нагоре (Postorder)
#   Балансирано (Inorder)
# Претърсване в широчина

А=(3,"+",b)
B=(a,"-",1)
C=(2,"*",B)
D=(C,"+",A)
