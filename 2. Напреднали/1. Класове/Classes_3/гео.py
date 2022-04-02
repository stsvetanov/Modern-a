# Sofia, 42.69917,23.32250
# lat  [-90,90]
# long [-180;180]
class address:
    def __init__(self,city, lat=0,long=0):
        if lat>=-90 and lat<=90: self.latitude=lat
        else:
            self.latitude=0
        self.lat_sn='N'
        if long>=-180 and long<=180: self.longitude=long
        else:
            self.longitude = 0
        self.long_WE='E'
        self.town=city

    def lat_conv(self):
        if self.latitude<0:
            self.latitude=abs(self.latitude)
            self.lat_sn='S'
    def long_conv(self):
        if self.longitude<0:
            self.longitude=abs(self.longitude)
            self.long_WE='W'
    def get_address(self):
        self.lat_conv()
        self.long_conv()
        return [self.latitude,self.lat_sn,self.longitude,self.long_WE]

    def __repr__(self):
        ss=self.get_address()
        s="Координатите на град %s са:\n" %(self.town)
        s=s+"--географска ширина: %10.5f %s\n" %(ss[0],ss[1])
        s = s + "--географска дължина: %9.5f %s\n" % (ss[2], ss[3])
        return s

# Тестване на класа
# ci=['Sofia', 42.69917,23.32250]
# geo_address=address(ci[0],ci[1],ci[2])
# print(geo_address)
#
# ci_2=['Йоханесбург',-26.195246, 28.034088]
# geo_address=address(ci_2[0],ci_2[1],ci_2[2])
# print(geo_address)

ci_2=['Asunsion, Paraguay',-25.295284,-57.632939]
geo_address=address(ci_2[0],ci_2[1],ci_2[2])
#print(geo_address)
print(geo_address.town)
print(geo_address.latitude) # -25...
print(geo_address.lat_sn) # N
print(geo_address.longitude) # -57...
print(geo_address.long_WE) # E
print("----------------------")
geo_address.lat_conv()
print(geo_address.latitude) # -25...
print(geo_address.lat_sn) # N
print("----------------------")
geo_address.get_address()
print(geo_address.latitude) # -25...
print(geo_address.lat_sn) # N
print(geo_address.longitude) # -57...
print(geo_address.long_WE) # E