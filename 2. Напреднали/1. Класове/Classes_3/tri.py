class Point:
    def __init__(self):
        from random import randint
        lower_bound=0
        upper_bound=10
        self.x=randint(lower_bound,upper_bound)
        self.y=randint(lower_bound,upper_bound)
        self.z=0
    def get_point(self):
        return [self.x,self.y,self.z]
    def __repr__(self):
        s="Координата по X: %10.2f\n" %(self.x)
        s=s+"Координата по Y: %10.2f\n" %(self.y)
        s = s + "Координата по Z: %10.2f\n" % (self.z)
        return s
class Tri:
    def __init__(self):
        self.A=Point()
        self.B=Point()
        self.C=Point()
    def get_tri(self):
        # Извлича трите точки A, B, C
        l=[self.A.get_point(),self.B.get_point(),self.C.get_point()]
        return l
    def distance(self,p1,p2):
        # Връща разстоянието между две точки
        d=round(((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5,2)
        return d
    def is_tri(self):
        # Проверява дали точките могат да образуват триъгълник
        a=self.distance(self.A,self.B)
        b=self.distance(self.A,self.C)
        c=self.distance(self.C,self.B)
        if a<b+c and b<a+c and c<a+b: return [True,[a,b,c]]
        else: return [False,[a,b,c]]
    def peri(self):
        # Изчислява полу-периметъра на триъгълника (сбора от разстоянията между точките, разделен на две)
        abc = self.is_tri()
        if abc[0] == True:
            abc = abc[1]
            P=abc[0]+abc[1]+abc[2]
            p=round(P/2,2)
            return [p,round(p-abc[0],2),round(p-abc[1],2),round(p-abc[2],2)]
        else:
            return "Не може да се изчисли периметър, т.к. точките не образуват триъгълник"
    def surface(self):
        # Изчислява лицето на тригълника
        abc = self.is_tri()
        if abc[0] == True:
            pp=self.peri()
            s=round((pp[0]*pp[1]*pp[2]*pp[3])**0.5,2)
        else:
            s="Не може да се изчисли лице, т.к. точките не образуват триъгълник"
        return s
    def h(self):
        # Намира трите височини в триъгълника
        abc=self.is_tri()
        if abc[0]==True:
            abc=abc[1] # връща списък с дължините на страните на триъгълника
            s=self.surface()
            h=[]
            for i in range(3):
                h.append(round(2*s/abc[i],2))
                # формула за височината: 2*s/abc[i], abc[i] е поредната страна в триъгълника
        else:
            h="Не може да се изчислят височините, т.к. точките не се образува триъгълник"
        return h

    def __repr__(self):
        s="Генрираните точки са с координати:\n"
        s=s+"т.А:\n"
        s=s+self.A.__repr__()

        s = s + "т.B:\n"
        s = s + self.B.__repr__()

        s = s + "т.C:\n"
        s = s + self.C.__repr__()

        abc=self.is_tri()
        if abc[0]==True: tes=" "
        else: tes=" не "
        s=s+"\nГенерираните точки"+tes+"образуват триъгълник\n"
        if abc[0] == True:
            s=s+"Дължините на триъгълника са:\n"
            s=s+"a=%10.2f, b=%10.2f, c=%10.2f\n" %(abc[1][0],abc[1][1],abc[1][2])
            s = s + "Височините на триъгълника са:\n"
            hs=self.h()
            s = s + "Ha=%9.2f, Hb=%9.2f, Hc=%9.2f\n" % (hs[0], hs[1], hs[2])
            p=self.peri()
            s=s+"Периметърът на триъгълника е: %10.2f\n" %(round(p[0]*2,2))
            s = s + "Лицето на триъгълника е: %15.2f\n" %(self.surface())
            return s

# t=Tri()
# print(t.get_tri())
# print(t.distance(t.A,t.B))
# print(t.is_tri())
# print(t.peri())
# print(t.surface())
# print(t.h())

# Ако имате допълнително условие, да се създадат 5 триъгълника и да се изведе информацията за тях

L=[Tri() for i in range(5)] # ще генерира 5 различни тройки от точки

# L=[]
# l=0
# while l<5:
#     k=Tri()
#     if k.get_tri()[0]==True:
#         L.append(k)
#         print(k)
#         l+=1
print(L)
print(len(L))




#print(t)
