# зад.3: МАРАТОН
# За целите на обработката на резултатите от Софийски маратон трябва да се опишат следните класове:
# Клас Time, представящ време чрез часове, минути и секунди – цели числа. Класът трябва да разполага с:
# конструктори, методи за достъп, метод __repr__()
# Метод Time_diff , намиращ разликата между текущото време и времето t, предадено чрез аргумента
# Клас Competitor, представящ следните данни за състезател: регистрационен номер, име, фамилия,
# стартово време (на маратон състезателите не винаги стартират заедно), време на достигане на финала.
# Класът трябва да разполага с:
# *** конструктори, методи за достъп, метод __repr__()
# *** Метод __repr__() трябва да извежда информация за състезателното време на участника
# Тестов клас, демонстриращ поведението на класовете и взаимоотношението между тях
#import datetime
class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.start_hh=hh
        self.start_mm=mm
        self.start_ss=ss

    def __repr__(self):
        s=str(self.start_hh)+":"+str(self.start_mm)+":"+str(self.start_ss)
        return s
    def Time_diff(self,ehh=0,emm=0,ess=0):
        delta_hh=ehh-self.start_hh
        delta_mm=emm-self.start_mm
        delta_ss=ess-self.start_ss
        delta=Time(delta_hh,delta_mm,delta_ss)
        return(delta.__repr__())

class Competitor(Time):

    def __init__(self,id,name,fname, start_hh,start_mm,start_ss,end_hh,end_mm,end_ss):
        self.id=id
        self.name=name
        self.fname=fname
        self.start_time=Time(start_hh,start_mm,start_ss)
        self.endhh=end_hh
        self.endmm=end_mm
        self.endss=end_ss
        #self.end_time=Time(end_hh,end_mm,end_ss)
    def __repr__(self):
        s="състезателен номер: "+str(self.id)+"\n"
        s+=self.name +" "+self.fname+"\n"
        s+="Състезателно време: "+self.start_time.Time_diff(self.endhh,self.endmm,self.endss).__repr__()
        return s


# Testing
id=12
n='Ivan'
fn='Ivanov'
st=Time(13,00,00)
print(st)
et=Time(13,45,15)
print(st.Time_diff(13,12,12))
compet=Competitor(id,n,fn,13,0,0,13,45,12)

print(compet)