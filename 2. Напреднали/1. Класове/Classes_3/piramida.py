class Point:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    def getp(self):
        # връща координатите на дадена точка
        p = [self.x, self.y, self.z]
        return p
    def __repr__(self):
        s="Координата по X: %10.2f\n" %(self.x)
        s=s+"Координата по Y: %10.2f\n" %(self.y)
        s = s + "Координата по Z: %10.2f\n" % (self.z)
        return s
class BasePyr:
    # Пирамида ABCD, основа: ABC и връх D
    def __init__(self):
        lb = 0
        ub = 10

        from random import randint
        l=[]
        for i in range(4):
            x = randint(lb, ub)
            y = randint(lb, ub)
            if i<3:
                l.append(Point(x,y))
            else: # Случаят за т.D
                z=randint(lb+1, ub)
                l.append(Point(x,y,z))
        self.A = l[0]
        self.B = l[1]
        self.C = l[2]
        self.D = l[3]
    def distances(self):
        AB = ((self.A.x - self.B.x) ** 2 + (self.A.y - self.B.y) ** 2 + (self.A.z - self.B.z) ** 2) ** 0.5
        BC = ((self.C.x - self.B.x) ** 2 + (self.C.y - self.B.y) ** 2 + (self.C.z - self.B.z) ** 2) ** 0.5
        AC = ((self.A.x - self.C.x) ** 2 + (self.A.y - self.C.y) ** 2 + (self.A.z - self.C.z) ** 2) ** 0.5
        AD = ((self.A.x - self.D.x) ** 2 + (self.A.y - self.D.y) ** 2 + (self.A.z - self.D.z) ** 2) ** 0.5
        BD = ((self.D.x - self.B.x) ** 2 + (self.D.y - self.B.y) ** 2 + (self.D.z - self.B.z) ** 2) ** 0.5
        CD = ((self.C.x - self.D.x) ** 2 + (self.C.y - self.D.y) ** 2 + (self.C.z - self.D.z) ** 2) ** 0.5
        AB = round(AB, 2)
        BC = round(BC, 2)
        AC = round(AC, 2)
        AD = round(AD, 2)
        BD = round(BD, 2)
        CD = round(CD, 2)
        return [AB,BC,AC,AD,BD,CD]
    def peri(self):
        s = self.distances()
        pB=round((s[0]+s[1]+s[2])/2,2) # полу-периметър на основата ABC
        pAB = round((s[0] + s[3] + s[4]) / 2, 2) # полу-периметър на основата ABD
        pBC = round((s[1] + s[5] + s[4]) / 2, 2) # полу-периметър на основата BCD
        pAC = round((s[2] + s[3] + s[5]) / 2, 2) # полу-периметър на основата ACD
        return [pB,pAB,pBC,pAC]
    def SQS(self):
        s=self.distances()
        p=self.peri()
        sqs=[]
        sqs.append(round((p[0] * (p[0] - s[0]) * (p[0] - s[1]) * (p[0] - s[2])) ** 0.5,2))  ## Base Square
        sqs.append(round((p[1] * (p[1] - s[0]) * (p[1] - s[3]) * (p[1] - s[4])) ** 0.5,2))  ## ABD Square
        sqs.append(round((p[2] * (p[2] - s[1]) * (p[2] - s[4]) * (p[2] - s[5])) ** 0.5,2))  ## BCD Square
        sqs.append(round((p[3] * (p[3] - s[2]) * (p[3] - s[3]) * (p[3] - s[5])) ** 0.5,2))  ## ACD Square
        return sqs
    def apotemas(self):
        sqs=self.SQS()
        s = self.distances()
        ap=[]
        ap.append(round(2 * sqs[1] / s[0],2)) #ABD
        ap.append(round(2 * sqs[2] / s[1],2)) #BCD
        ap.append(round(2 * sqs[3] / s[2],2)) #ACD
        return ap
    def isOinci(self):
        # дали петата на височината на пирамидата съвпада с центъра на вписаната окръжност в основата
        ap=self.apotemas()
        if ap[0]==ap[1]==ap[2]:
            s = "Петата на височината съвпада с центъра на вписаната окръжност"
        else:
            s = "Петата на височината НЕ съвпада с центъра на вписаната окръжност"
        return s
    def isOoutci(self):
        #дали петата на височината на пирамидата съвпада с центъра на описаната окръжност в основата
        r = self.distances()
        if r[3]==r[4]==r[5]:
            s = "Петата на височината съвпада с центъра на oписаната окръжност"
        else:
            s = "Петата на височината НЕ съвпада с центъра на oписаната окръжност"
        return s
    def peta(self):
        # Връща координатите на петата на височината на пирамидата
        # Петата има координати x и y същите като т.D, и z=0
        xO=self.D.x
        yO=self.D.y
        zO=0
        pe=Point(xO,yO,zO)
        return pe.getp()
    def getP(self):
        # Връща списък от координатите на 4-те точки на пирамидата
        pA = self.A.getp()
        pB = self.B.getp()
        pC = self.C.getp()
        pD = self.D.getp()
        p = [pA, pB, pC, pD]
        return p
    def hi(self):
        # Връща височината на пирамидата :)
        # Защото основата сме я генерирали с точки, за които z=0
        return self.D.z
    def is_tri(self):
        # Проверява дали точките могат да образуват триъгълник
        d=self.distances()
        if d[0]<d[1]+d[2] and d[1]<d[0]+d[2] and d[2]<d[0]+d[1]: return True
        else: return False
    def __repr__(self):
        s="Генрираните точки са с координати:\n"
        s=s+"т.А:\n"
        s=s+self.A.__repr__()
        s = s + "т.B:\n"
        s = s + self.B.__repr__()
        s = s + "т.C:\n"
        s = s + self.C.__repr__()
        s = s + "т.D:\n"
        s = s + self.D.__repr__()

        abc=self.is_tri()
        if abc==True: tes=" "
        else: tes=" не "
        s=s+"\nГенерираните точки"+tes+"образуват пирамида\n"
        if abc == True:
            s=s+"Дължините на основните ръбове са:\n"
            dist = self.distances()
            s=s+"AB=%10.2f\nAC=%10.2f\nBC=%10.2f\n" %(dist[0], dist[1], dist[2])
            s = s + "Дължините на околните ръбове са:\n"
            s = s + "AD=%10.2f\nBD=%10.2f\nCD=%10.2f\n" % (dist[3], dist[4], dist[5])
            s = s + "Апотемите на пирамидата са:\n"
            hs=self.apotemas()
            s = s + "на ABD=%9.2f, на BCD=%9.2f, на ACD=%9.2f\n" % (hs[0], hs[1], hs[2])
            p=self.peri()
            s=s+"Периметрите на триъгълниците са: \n"
            s=s+"...на основата ABC: %10.2f\n"%(round(p[0]*2,2))
            s = s + "...на ABD: %10.2f\n" % (round(p[1] * 2, 2))
            s = s + "...на BCD: %10.2f\n" % (round(p[2] * 2, 2))
            s = s + "...на ACD: %10.2f\n" % (round(p[3] * 2, 2))
            s = s + "\nЛицата на триъгълниците са: \n"
            sq=self.SQS()
            s = s + "...на ABC: %10.2f\n" % (round(sq[0] * 2, 2))
            s = s + "...на ABD: %10.2f\n" % (round(sq[1] * 2, 2))
            s = s + "...на BCD: %10.2f\n" % (round(sq[2] * 2, 2))
            s = s + "...на ACD: %10.2f\n" % (round(sq[3] * 2, 2))
            s=s+"Петата на пирамидата е с координати:\n"
            s=s+(Point(self.D.x,self.D.y).__repr__())
            s=s+"Височината на пирамидата е: %10.2f\n" %(self.hi())
            s=s+self.isOinci()+"\n"
            s = s + self.isOoutci() + "\n"
        else: s=s+"Няма пирамида - няма изчисления\n"
        return s


pyramide=BasePyr()
print(pyramide)
# print(pyramide.getP())
# print(pyramide.distances())
# print(pyramide.peri())
# print(pyramide.SQS())
# print(pyramide.apotemas())
# print(pyramide.isOinci())
# print(pyramide.isOoutci())
# print(pyramide.peta())
# print(pyramide.hi())