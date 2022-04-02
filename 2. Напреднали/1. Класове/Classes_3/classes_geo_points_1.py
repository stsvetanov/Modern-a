# Класове
# Дефинирайте структура, която описва дадена географска точка:
# държава - string
# град - string
# ширина - {'degrees':[0;90],'minutes':[0;60],'seconds':[0:60],pole:{'S','N'}
# дължина - {'degrees':[0;90],'minutes':[0;60],'seconds':[0:60],pole:{'E','W'}
# метод, който превръща ширината/дължината в реални числа
# метод, който да показва красиво всеки един обект на класа

class City():
#     тук може да има някакви променливи от тип константа или брояч
#     които да се използват от всички методи в класа
#     def __init__(self,lat,long,country='България',town=''): # конструктор
    def __init__(self,country='България',town='', lat={'degrees':0,'minutes':0,'seconds':0,'pole':''},long={'degrees':0,'minutes':0,'seconds':0,'pole':''}):
        self.country=country
        self.city=town
        self.lattitude=lat
        self.longtitude=long
    def convert_degrees_into_real(self,deg,min,sec):
        s=sec/60
        m=min/60
        d=round(deg+m+s,2)
        return d
    def __repr__(self):
        la=self.convert_degrees_into_real(self.lattitude['degrees'],self.lattitude['minutes'],self.lattitude['seconds'])
        lo = self.convert_degrees_into_real(self.longtitude['degrees'], self.longtitude['minutes'],
                                            self.longtitude['seconds'])
        s='Държава: %s\nГрад: %s\nГеографска ширина: %f\nГеографска дължина: %f'
        return s %(self.country,self.city,la,lo)

Varna=[(43,13,0),(27,55,0)]
Sofia=[(42,42,0),(23,19,48)]


a=City()
a.city='Sofia'
a.lattitude={'degrees':43,'minutes':13,'seconds':0,'pole':'N'}
a.longtitude={'degrees':27,'minutes':55,'seconds':0,'pole':'E'}


print(a)
print(a.city)
print(a.lattitude['pole'])






