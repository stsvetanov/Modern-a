def simple_for(k):
    simples=[]
    for n in range(2,k):
        check = True  # когато числото е просто
        for x in range(2,n):
            if n%x==0:
                check=False
        if check:
            simples.append(n)
    return simples

deliteli=[2,3,5,7,11]
dkeys=simple_for(100)
borj_key=len(dkeys)
dvalues=[] #всеки един елемент е редица от резултатите при деление на делителите
for dk in dkeys:
    l=[]
    for dl in deliteli:
        l.append(dk%dl)
    dvalues.append(tuple(l))
mydic=dict(zip(dkeys,dvalues))
print(mydic)

# 2:[(2,0),(3,1),(5,1)...(97,1)]
# 3
# 5
# 7
# 11
 # fn 13873 +
def newd(k,d):
    # d=deliteli
    # k=dkeys
    newdict=dict()
    for dk in d:
        vals = []
        for keyor in k:
            vals.append((keyor,keyor%dk))
        newdict[dk]=vals
    return(newdict)

def newdd():
    global deliteli
    global mydic
    newdict=dict()
    for d in deliteli:
        newdict[d]=[]
        # 1. създаваме ключ d
        # 2. на ключ d присвояваме стойност, която е празен списък
        for key,val in mydic.items():
            newdict[d].append((key,val[deliteli.index(d)]))
            # key=2: val=(0,2,2,2,2), тогава:
            # при d=2, val[deliteli.index(d)]=val[0]
            # при d=3, val[deliteli.index(d)]=val[1]
            # {2: [(2, 0), (3, 1), (5, 1), (7, 1), (11, 1),
    return(newdict)
print(newdd())

