# Географска точка: клас за описание на географска точка GeoPoint
# ширина, дължина, име, тип: град/село/връх/езеро/река

# градуси, Е/W, S/N => клас за географски координати GeoCoord


class GeoCoord():
    def __init__(self, degrees:float,long_lat=True, direction="E"):
        # long_lat=True, означава, че ще създаваме координати за дължина
        # long_lat=False, означава, че ще създаваме координати за ширина
        if degrees >=0 and degrees <=90: self.deg=degrees
        else: self.deg=23

        if long_lat and isinstance(long_lat,bool): self.longlat=long_lat
        # проверката isinstance(long_lat,bool) я правим защото всяко число различно от 0 ще върне True
        # което означава, че ще може да се въвеждат невалидни данни, ако проверката липсва.
        else: self.longlat=False
        if not isinstance(direction,str): direction=str(direction)
        if self.longlat==False and (direction not in "SN"): self.dir="S"
        if self.longlat == False and (direction in "SN"): self.dir = direction
        if self.longlat  and (direction not in "EW"): self.dir = "E"
        if self.longlat  and (direction in "EW"): self.dir = direction
    def deg_min_sec(self):
        d=int(self.deg)
        res=(self.deg-d)*60
        m=int((self.deg-d)*60)
        s=int((res-m)*60)
        dms="%dº %d' %d\" " %(d,m,s)
        return dms
    def __repr__(self):
        # s="%f %s" %(self.deg,self.dir)
        # s=str(self.deg)+" "+self.dir
        s=self.deg_min_sec() + self.dir
        return s

t1=GeoCoord(23.54,False,1)
# print(t1)


from dataclasses import dataclass

@dataclass()
class GC():
    deg: int
    longlat: bool
    dir: str
    def deg_min_sec(self):
        d=int(self.deg)
        res=(self.deg-d)*60
        m=int((self.deg-d)*60)
        s=int((res-m)*60)
        dms="%dº %d' %d\" " %(d,m,s)
        return dms
    def __repr__(self):
        s=self.deg_min_sec() + self.dir
        return s

t2=GC(0,0,0)
t2.dir="N"
t2.longlat=False
t2.deg=43.23

# print(t2)

t3=GeoCoord(43.54,False,"N")
# print(t3)


class GeoPoint(GeoCoord):
    def __init__(self,lat=GeoCoord(0),long=GeoCoord(0,False,'N'), name='',type=''):
        self.name=name
        if type in {'град','село','връх','езеро','река'}: self.type=type
        else:
            self.type='град'
            self.name ='София'
        if isinstance(lat,GeoCoord): self.lat=lat
        else: self.lat=GeoCoord(0)
        if isinstance(long,GeoCoord): self.long=long
        else: self.long=GeoCoord(0)

    def __repr__(self):
        s="%s: %s\nг.дължина: %s\nг.ширина:  %s" %(self.type, self.name, self.lat, self.long)
        return s

@dataclass()
class GP():
    lat:  GC=GC(23,True,"E")
    long: GC=GC(43,False,"N")
    name: str = 'Sofia'
    type: str = 'city'

k=GeoPoint(t1,t3)

print(k)
k2=GP()
print(k2)
