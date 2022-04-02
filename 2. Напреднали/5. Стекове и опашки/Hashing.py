def hashCode(s):
    hash=5381
    for i in s:
        hash=31*hash+ord(i)
    return hash

# print(hashCode("ord123"))
# print(hashCode("o1r2d3"))
# print(hashCode("ord321"))
hash=dict()
size=1000
def getHash(elindex):
    return elindex*179424691%size
def add(elindex):
    hash[getHash(elindex)]=True
def remove(elindex):
    hash[getHash(elindex)] = False
def contains(elindex):
    h=getHash(elindex)
    if h in hash.keys(): return hash[h]
    else: return "Doesn't exist such element in hash"

add(1)
remove(0)
remove(3)
print(hash)
print(contains(1))
print(contains(3))
print(contains(4))


