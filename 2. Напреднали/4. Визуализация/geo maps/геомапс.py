import folium
import gpx_parser as parser

pth='/Users/valerina/PycharmProjects/test/Упражнения/graphics/'
fn='3301146.gpx'

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

with open(pth+fn, 'r') as gpx_file:
    gpx = parser.parse(gpx_file)
myMap=folium.Map(location=[43.2141, 27.9147],zoom_start=16)
folium.Marker([43.2141, 27.9147], popup="Varna").add_to(myMap)
# for track in gpx:
#     for segment in track:
#         for point in segment:
#             folium.Marker([point.latitude,point.longitude],popup="").add_to(myMap)

for point in L:
    folium.Marker([point.geo_coord.latitude, point.geo_coord.longitude], popup=point.town).add_to(myMap)
#myMap.save('VarnaCenter_on_folium_map.html')
myMap.save('BG_folium_map.html')