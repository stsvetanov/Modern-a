# Sofia, 42.69917,23.32250
# lat  [-90,90]
# long [-180;180]
class geo_point:
    def __init__(self, lat=0,long=0):
        if lat>=-90 and lat<=90: self.latitude=lat
        else:
            self.latitude=0
        self.lat_sn='N'
        if long>=-180 and long<=180: self.longitude=long
        else:
            self.longitude = 0
        self.long_WE='E'

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
        s="--географска ширина: %10.5f %s\n" %(ss[0],ss[1])
        s = s + "--географска дължина: %9.5f %s\n" % (ss[2], ss[3])
        return s

class address(geo_point):
    def __init__(self,city,gp=geo_point()):
        self.town=city
        self.geo_coord=gp
    def __repr__(self):
        s = "Координатите на град %s са:\n" % (self.town)
        s=s+"%s" %(self.geo_coord)
        return s

def geo_distance(a,b):
    # Изчислява разстоянието между 2 географски точки
    # a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    # φ = lattitude
    # λ=longtitude
    # c = 2 ⋅ atan2( √a, √(1−a) )
    # d = R ⋅ c
    R= 6371 # земния радиус
    import math
    # Предполагаме, че а и b са обекти от клас address

    la_a=a.geo_coord.latitude
    la_b=b.geo_coord.latitude
    lat_diff=math.radians(la_a-la_b)
    lo_a = a.geo_coord.longitude
    lo_b = b.geo_coord.longitude
    long_diff = math.radians(lo_a - lo_b)
    la_a=math.radians(la_a)
    la_b=math.radians(la_b)
    aa=(math.sin(lat_diff/2))**2+math.cos(la_a)*math.cos(la_b)*(math.sin(long_diff/2))**2
    cc=2*math.atan2(aa**0.5,(1-aa)**0.5)
    distance=R*cc
    return distance

# Varna=address('Varna',geo_point(43.2141, 27.9147))
# Burgas=address('Burgas',geo_point(42.5048, 27.4626))
# print(Varna)
# print(Burgas)
# print("Разстоянието по права линия между %s и %s е %f" %(Varna.town, Burgas.town,geo_distance(Varna,Burgas)))

L=[address('Varna',	geo_point(43.2141, 27.9147)),
address('Avren',	geo_point(43.128476, 27.810187)),
address('Bliznaci',	geo_point(43.056764, 27.860897)),
address('Dolni Chiflik',	geo_point(42.963141, 27.769082)),
address('Bqla',	geo_point(42.918408, 27.784869)),
address('DCH',	geo_point(42.906091, 27.719976)),
address('Bq',	geo_point(42.866727, 27.733532)),
address('Pomorie',	geo_point(42.827967, 27.628470)),
address('Nesebar',	geo_point(42.724650, 27.626405)),
address('Burgas',	geo_point(42.5048, 27.4626))]

# dist=0
# for i in range(len(L)-1):
#     dist+=geo_distance(L[i],L[i+1])
# print(dist)
#
# # с функцията map
# dist_2=sum(list(map(geo_distance,L[:-1],L[1::])))
# print(dist_2)

# # Тестване на класа
# #geop=geo_point(42.69917,23.32250)
# #print(geop)
# geo_city=address('София')
# print(geo_city)
# geo_city.geo_coord.latitude=-42.69917
# geo_city.geo_coord.longitude=23.32250
# # geo_city.geo_coord e обект от клас geo_point()
# # и затова всички атрибути и методи за geo_point() стават приложими
# print("----------------------")
# print(geo_city.geo_coord)
# # geo_city.geo_coord.get_address()
# # print("----------------------")
# # print(geo_city)

pth='/Users/valerina/PycharmProjects/test/Класове/'
fn='3301146.gpx'
import gpx_parser as parser
with open(pth+fn, 'r') as gpx_file:
    gpx = parser.parse(gpx_file)
# gpx съдържа тракове за движението
# траковете са отделни маршрути, които нямат общо по между си
# сегментите са маршрути в рамките на един трак
# точките са конкретните гео точки към даден момент в даден сегмент
# ако дължината на gpx e 1 => има само един трак
# ако дължината на track e 1 => има само един сегмент

# Вариант 1: 1 трак, 1 сегмент:
if len(gpx)==1 and len(gpx.tracks)==1:
    print("Изминатото разстояние е %.4f м\n" % (gpx.tracks[0].length_2d()))
# Вариант 2: няколко трака, няколко сегмента:
else:
    for track in gpx:
        for segment in track:
            print("Изминатото разстояние за сегмент %s е %.4f м\n" %(segment,segment.length_2d()))
# Вариант 3: извличане на точките и пресмятане на разстоянията с функцията geo_distance(a,b):

dist_by_tracks=[]
dist_by_segments = []
point_distances=[]
for track in gpx:
    for segment in track:
        for point in segment:
            point_distances.append(address('',geo_point(point.latitude,point.longitude)))
        s=sum(list(map(geo_distance,point_distances[:-1],point_distances[1::])))
        dist_by_segments.append(s)
        print("Изминатото разстояние за сегмента е %.4f км\n" %(s))
    s=sum(dist_by_segments)
    dist_by_tracks.append(s)
    print("Изминатото разстояние за трака е %.4f км\n" % (s))
s=sum(dist_by_tracks)
print("Общото изминато разстояние е %.4f км\n" % (s))