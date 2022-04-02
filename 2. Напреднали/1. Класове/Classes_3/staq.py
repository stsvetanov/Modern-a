
class furniture:
    def __init__(self,name="",w=0,h=0,d=0):
        self.typefur=name
        self.width=w
        self.height=h
        self.lengthd=d
    def __repr__(self):
        s=self.typefur + " с размери: %10.2f,%10.2f,%10.2f\n" %(self.width,self.height,self.lengthd)
        return s
class tech:
    def __init__(self,type="",trademark="",model="",year=2020):
        self.type_tech=type
        self.trade_mark = trademark
        self.model = model
        self.year = year
    def __repr__(self):
        s = self.type_tech + ":\nмарка: %s\nмодел: %s\nгодина: %d\n" % (self.trade_mark, self.model, self.year)
        return s

class room(furniture,tech):
    def __init__(self,name=""):
        self.name=name
        self.furnitures=[]
        self.appl=[]
    def __repr__(self):
        s="В стаята %s има:\n" %(self.name)
        for i in self.furnitures:
            s+=i.__repr__()
        for i in self.appl:
            s+=i.__repr__()
        return s
t=room("Хол")
t.furnitures.append(furniture("маса",30,75,40))
#t.furnitures.append(furniture("маса2",60,75,40))
t.appl.append(tech("Телевизор","Philips","S90",2019))
t.appl.append(tech("PC","Lenovo","S90",2015))
t.appl.append(tech("таблет","Lenovo","S90",2017))

# Намиране и разпечатване на най-старата техника
a=t.appl
print(a)
l=[]
for i in a:
    l.append(i.year)
minyear=min(l)
for i in range (len(a)):
    if a[i].year==minyear: print(a[i])


#print(t.appl)