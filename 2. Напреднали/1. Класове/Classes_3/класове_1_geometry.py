# Класове и наследяване

# Пример: Геометрия
# Точка (в равнина) има координати x и y
# Окръжност се представя като точка (център) и радиус => наследява "Точка"
# Цилиндър се представя с окръжност и височина => наследява "Окръжност"

from dataclasses import dataclass

# @dataclass()
class Point():
    def __init__(self,x: float=0,y: float=0,name: str='O'):

        if not isinstance(x, float):
            try: self.x=float(x)
            except: self.x = 0
        else: self.x=x

        if not isinstance(y, float):
            try:self.y = float(y)
            except:self.y = 0
        else: self.y=y

        if not isinstance(name, str):self.name = str(name)
        else:  self.name=name

        self.d=round(((1-self.x)**2+(1-self.y)**2)**(1/2),2)
    def topont11(self):
        return  round(((1-self.x)**2+(1-self.y)**2)**(1/2),2)
    def __repr__(self):
        s="т.%s (%.2f;%.2f)"%(self.name,self.x,self.y)
        # %.2f форматира с реалното число с максимум два знака след десетичната запетая
        return s
@dataclass()
class Circle():
    center: Point=Point()
    radius: float=1


    def diameter(self):
        return 2*self.radius
    def perimeter(self):
        return 3.14*self.diameter()
    def square(self):
        return 3.14*self.radius**2

    def __repr__(self):
        s="oръжност с: център %s, радиус %.2f, диаметър %.2f, обиколка %.2f, лице %.2f" %(self.center.__repr__(),self.radius,self.diameter(),self.perimeter(),self.square())
        return s


@dataclass()
class Cylinder():
    base: Circle=Circle()
    h: float=1
    def __repr__(self):
        s="Цилиндър с \nOснова %s\nВисочина: %.2f\n" %(self.base.__repr__(),self.h)
        return s

# # използване на класовете с данните по подразбиране
# p=Point()
# c=Circle()
# cyl=Cylinder()
# print(p)
# print(c)
# print(cyl)

# # използване на класовете с наши данните
# p=Point(5,7,'A')
# c=Circle(center=p,radius=3)
# cyl=Cylinder(c,10)
# print(p)
# print(c)
# print(cyl)


# Ако L е списък от данни, където са посочени в следния ред: [x,y,name,radius,h],
# то да се обходи списъка и всеки подсписък да бъде преформатиран като обект от клас цилиндър
L=[[3,4,'A',5,4],[1,4,'B',15,4],[3,2,'C',5,18],[5,2,'D',3,4],[8,9,'E',7,10],[0,0,'F',10,7]]

for i in range(len(L)):
    p = Point(x=L[i][0],y=L[i][1],name=L[i][2])
    c = Circle(center=p, radius=L[i][3])
    cyl = Cylinder(c, L[i][4])
    L[i]=cyl
    print(L[i])

# print(L)

print(p.d)
print(p.topont11())
