class Tri():
    def __init__(self):
        import random as rd
        self.A = rd.randint(1, 35)
        self.B = rd.randint(1, 35)
        self.C = rd.randint(1, 35)
    def  isTri(self):
        a,b,c=self.A,self.B,self.C
        cond = (a <= b + c) & (b <= a + c) & (c <= a + b)  # или True или False
        return cond

    def isPrav(self):
        cond=False
        if self.isTri():
            a, b, c = self.A, self.B, self.C
            cond_3_2_1 = a ** 2 + b ** 2 == c ** 2
            cond_3_2_2 = a ** 2 + c ** 2 == b ** 2
            cond_3_2_3 = b ** 2 + c ** 2 == a ** 2
            cond = cond_3_2_1 | cond_3_2_2 | cond_3_2_3
        return cond
    def isRavb(self):
        cond=False
        if self.isTri():
            a, b, c = self.A, self.B, self.C
            cond = a==b | b==c | a==c
        return cond
    def isRavStr(self):
        cond=False
        if self.isTri():
            a, b, c = self.A, self.B, self.C
            cond = a==b & a==c
        return cond
    def isS(self):
        cond=False
        if self.isTri():
            a, b, c = self.A, self.B, self.C
            p = round((a + b + c) / 2, 2)
            cond = (p * (p - a) * (p - b) * (p - c)) ** (round(1 / 2, 2)) > 75
        return cond
    def __repr__(self):
        d=[[self.A,self.B,self.C],[self.isTri(),self.isPrav(),self.isRavb(),self.isRavStr(),self.isS()]]
        return d

import random as rd
n=rd.randint(5,15) # всички произволни обекти от клас Tri()
L_True=[] #тези, които образуват триъгълник
L_False=[] #тези, които не образуват триъгълник
D={}
d={}
for i in range(n):
    tri=Tri()
    check=tri.isTri()
    if check:
        L_True.append([tri.A,tri.B,tri.C])
        tri_repr=tri.__repr__()
        d[str(tri_repr[0])] = tri_repr[1]
    else:
        L_False.append([tri.A,tri.B,tri.C])

D['tringle True']=L_True
D['tringle False']=L_False
print(D)
D['tringle True']=d
for k in D['tringle True'].items():
    # т.к. сме преформатирали стойността на D['tringle True'] да бъде речник със структура #{l[i]:[T/F,T/F,T/F,T/F],...}
    # затова, за даможем да извлечем и ключа и стойността използваме метода .items()
    print(k)