# Класове
# Дефинирайте структура, която описва дадена географска точка:
# държава - string
# град - string
# ширина - {'degrees':[0;90],'minutes':[0;60],'seconds':[0:60],pole:{'S','N'}
# дължина - {'degrees':[0;90],'minutes':[0;60],'seconds':[0:60],pole:{'E','W'}
# метод, който превръща ширината/дължината в реални числа
# метод, който да показва красиво всеки един обект на класа
class GeoPoint():
    def __init__(self,degrees:int(),minutes:int(),seconds:int(),pole,lat_long=True):
        # lat_long=True => lat
        # lat_long=False => long
        self.lat_long=lat_long
        self.coordinates={'degrees':degrees,'minutes':minutes,'seconds':seconds}
        if lat_long==True:
            if pole not in {'N', 'S'}:
                self.pole = 'N'
            else:
                self.pole = pole
        else:
            if pole not in {'E', 'W'}:
                self.pole = 'E'
            else:
                self.pole = pole
    def convert_degrees_into_real(self,deg,min,sec):
        s=sec/60
        m=min/60
        d=round(deg+m+s,2)
        return d
    def __repr__(self):
        if self.lat_long: s='Географска ширина: %f, %s'
        else: s='Географска дължина: %f, %s'
        deg_real=self.convert_degrees_into_real(self.coordinates['degrees'], self.coordinates['minutes'],
                                       self.coordinates['seconds'])
        return s %(deg_real,self.pole)

class City(GeoPoint):

    def __init__(self,country='България',town='', lat=GeoPoint(0,0,0,"N"),long=GeoPoint(0,0,0,'E',False)):
        self.country=country
        self.city=town
        self.lattitude=lat
        self.longtitude=long
    def __repr__(self):
        s='Държава: %s\nГрад: %s\n%s\n%s\n'
        return s %(self.country,self.city,self.lattitude,self.longtitude)


Varna=[(43,13,0),(27,55,0)]
Sofia=[(42,42,0),(23,19,48)]


#
a=City()
a.city='Sofia'
a.lattitude=GeoPoint(43,13,0,'N')
a.longtitude=GeoPoint(27,55,0,'E',False)
print(a)

# Извличане на имената на атрибутите за обекта "a" от клас "City(), които сме създали"
attrs_1 = [obj for obj in dir(a) if not callable(getattr(a, obj)) and obj[:2]!='__']
# dir(a) извлича под формата на списък всички атрибути и методи за класа от който е "a"
# "not callable" означава да не е функция
# getattr(a, obj) извлича поредния елемент-атрибут от "а"
# obj[:2]!='__' проверява името на атрибута да не съдържа двойна подчертавка
attrs_2 = [obj for obj in dir(a) if not callable(obj) and obj[:2]!='__']
# ще извлече само атрибутите и специфичния метод (без онези, които са с подчертавка),
# които сме създали за класа и всички наследени специфични методи
funcs_1=[obj for obj in dir(a) if callable(getattr(a, obj)) and obj[:2]!='__']
# ще извлече само специфичния метод (без онези, които са с подчертавка),
# които сме създали за класа и всички наследени специфични методи
funcs_2=[obj for obj in dir(a) if callable(getattr(a, obj)) and obj[:2]=='__']
# ще извлече само специалните методи (вградени), които започват с двойна подчертавка
print(attrs_1)
print(attrs_2)
print(funcs_1)
print(funcs_2)






