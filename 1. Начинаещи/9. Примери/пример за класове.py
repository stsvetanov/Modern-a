# Задача 1:
#
# Да се опише клас за координата от географска точка, такъв че:
#
# позволява въвеждането на координатата както като реално число градуси, така и като комбинация от цели числа за градуси и минути
# координатата има атрибут за ширина/дължина, съответно северна/ южна и източна/западна
# по подразбиране се задава северна ширина с източна дължина
# да се напишат методи за: инициализация и красиво представяне
# да се напишат методи, които:
# проверяват въведените стойностости и в зависимост от това:
# пресмятат другия формат на представяне на координатата и го записват в съответния атрибут
# При така формулираната задача, колко атрибута трябва да съдържа класа?
#
# Тествайте класа и методите му.

class GP():
    # long_lat=0 : северна ширина, N
    # long_lat=1 : южна ширина, S
    # long_lat=2 : източна дължина, E
    # long_lat=3 : западна дължина, W

    def __init__(self,deg=0,min=0,long_lat=0):
        self.degrees,self.minutes,self.long_latitude=self.check(deg,min,long_lat)
    def check(self,deg,min,long_lat):
        ch_1=not (isinstance(deg,int) or isinstance(deg,float))
        ch_2=not isinstance(min,int)
        ch_3=not isinstance(long_lat,int)
        ch_4=isinstance(deg,float)
        check_1=any([ch_1,ch_2,ch_3])

        # Ако и check_1 е True, тогава ще приложим стойности по подразбиране
        if check_1:
            return (0,0,0)
            # return (degrees,minutes,long_lat)
        elif ch_4:
            if long_lat>=0 and long_lat<=3:
                return(int(deg),60*(deg-int(deg)),long_lat)
            else:return(int(deg),60*(deg-int(deg)),0)
        else:
            if long_lat >= 0 and long_lat <= 3:
                return (deg, min, long_lat)
            else:
                return (deg, min, 0)
    def __repr__(self):
        # 23,75;0 => 23º45'N
        if self.long_latitude==0 : s='N'
        elif self.long_latitude==1 : s='S'
        elif self.long_latitude==2 : s='E'
        elif self.long_latitude==3 : s='W'
        else: s='N'

        result="%dº%d'%s" %(self.degrees,self.minutes,s)
        return result

mypoint=GP(23.75)
print(mypoint)
mypoint=GP(23,23.75)
print(mypoint)
mypoint=GP(23,1,23)
print(mypoint)