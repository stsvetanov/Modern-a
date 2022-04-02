# Да се дефинира клас GeoLocation, такъв че:
# променлива за класа: Gradove=['Бургас','Варна','Силистра','Търговище','Ловеч','Кърджали','Пловдив','Добрич','София','Благоевград','Пазарджик','Перник','Плевен','Видин','Монтана','Кюстендил','Ямбол','Русе','Враца','Велико Търново','Шумен','Габрово','Стара Загора','Смолян','Хасково','Разград','Сливен']
# има атрибути:
# **град А: стринг, може да бъде измежду елементите на списъка Gradove
# **град Б: стринг, може да бъде измежду елементите на списъка Gradove
# **маршрут: стринг (свободен текст)
# **разстояние между А и Б в км: положително реално число
# има методи за:
# **инициализация: използвайте try/except за тестване на входните данни, и изберете някакви константи за атрибутите, в случаите, когато или не са подаден входни данни, или входните данни не отговарят на критериите. Ако са подадени град А и град Б да бъдат еднакви, то независимо от обявено разстоние, то трябва да се смени с нула.
# **красиво представяне: “Разстоянието от град А до град Б по маршрут X е ###.## км.”
# функция за сортиране на елементите по азбучен ред по град А за списък от обекти от клас GeoLocation
# Демонстрирайте класа

class GeoLocation():
    Gradove = ['Бургас', 'Варна', 'Силистра', 'Търговище', 'Ловеч', 'Кърджали', 'Пловдив', 'Добрич', 'София',
               'Благоевград', 'Пазарджик', 'Перник', 'Плевен', 'Видин', 'Монтана', 'Кюстендил', 'Ямбол', 'Русе',
               'Враца', 'Велико Търново', 'Шумен', 'Габрово', 'Стара Загора', 'Смолян', 'Хасково', 'Разград', 'Сливен']
    def __init__(self,cityA=Gradove[0],cityB=Gradove[1],route="пътуване с кола",AB=115):
        import random as rd
        check_1=cityA in self.Gradove
        check_2=cityB in self.Gradove
        check_4=isinstance(route,str)

        try:
            check_5=(isinstance(AB,float) or isinstance(AB,int)) and AB>=0
        except:
            check_5=False

        if check_1: self.A=cityA
        else: self.A=self.Gradove[rd.randint(0,len(self.Gradove))]

        if check_2: self.B=cityB
        else: self.B = self.Gradove[rd.randint(0, len(self.Gradove))]

        if check_4: self.R=route
        else: self.R="незвестен маршрут"

        check_3=self.A!=self.B

        if check_5:
            if check_3:
                self.AB=AB
            else:
                self.AB=0
        else:
            if not check_3: self.AB=0
            else:
                try:
                    self.AB=float(AB)
                except:
                    self.AB=100
        self.sort_cities()
    def sort_cities(self):
        # градовете в обекта, като първият винаги е по-малък по абучен ред от втория град
        if self.A>self.B:
            self.A,self.B=self.B,self.A
    def __repr__(self):
        s="Разстоянието от град %s до град %s по маршрут %s е %d км." %(self.A,self.B,self.R,self.AB)
        return s

## Демо на класа:
# grad=GeoLocation()
# print(grad)
# grad=GeoLocation("Бургас","София","пътуване с рейс","350")
# print(grad)

def Init_GeoLocations_list():
    # Инициализация на списък с обекти от тип GeoLocations
    import random as rd
    routes=["пътуване с кола", "пътуване с влак", "пътуване с рейс"]
    Gradovete = ['Бургас', 'Варна', 'Силистра', 'Търговище', 'Ловеч', 'Кърджали', 'Пловдив', 'Добрич', 'София',
                   'Благоевград', 'Пазарджик', 'Перник', 'Плевен', 'Видин', 'Монтана', 'Кюстендил', 'Ямбол', 'Русе',
                   'Враца', 'Велико Търново', 'Шумен', 'Габрово', 'Стара Загора', 'Смолян', 'Хасково', 'Разград', 'Сливен']
    L=[]
    for i in range(10):
        cityA=Gradovete[rd.randint(0,len(Gradovete)-1)]
        cityB=Gradovete[rd.randint(0,len(Gradovete)-1)]
        rout=routes[rd.randint(0,len(routes)-1)]
        AB=rd.randint(75,450)
        L.append(GeoLocation(cityA,cityB,rout,AB))
    return L

def Geo_sorting(GS_list):
    G=[]
    print("Първоначална подребда:")
    for l in GS_list:
        G.append(l.A)
        print(l)
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i]<G[j]:
                # GS_list[i].A<GS_list[j].A
                pass
            else:
                G[i],G[j]=G[j],G[i]
                GS_list[i],GS_list[j]=GS_list[j],GS_list[i]

L=Init_GeoLocations_list()
Geo_sorting(L)

print("\nСортирана подребда:")
for l in L:
    print(l)

def Min_Max_route_in_GS_list(GS_list,MM="min"):
    # Тази функция приема входен параметър MM, който по подразбиране е min,
    # но ако има друга стойност, се намира максимума
    km = [l.AB for l in GS_list]
    if MM=="min":
        path=min(km)
        ind=km.index(path)
        s="\nНай-късото разстояние между градовете %s и %s е %d км по маршрут %s." %(GS_list[ind].A,GS_list[ind].B,GS_list[ind].AB,GS_list[ind].R)
    else:
        path=max(km)
        ind=km.index(path)
        s="\nНай-дългото разстояние между градовете %s и %s е %d км по маршрут %s." %(GS_list[ind].A,GS_list[ind].B,GS_list[ind].AB,GS_list[ind].R)
    return s
print(Min_Max_route_in_GS_list(L))


L=[]
L.append(GeoLocation("Варна","София","пътуване с влак",490))
L.append(GeoLocation("Варна","София","пътуване със самолет",300))
L.append(GeoLocation("София","Варна","пътуване с кола",450))
print(Min_Max_route_in_GS_list(L))

def Min_Max_route_in_GS_list_2(GS_list,градА,градБ,MM="min"):
    # Тази функция приема входен параметър MM, който по подразбиране е min,
    # но ако има друга стойност, се намира максимума

    km = [l.AB for l in GS_list if (l.A==градА and l.B==градБ) or (l.A==градБ and l.B==градА) ]
    # (l.A==градА and l.B==градБ) or (l.A==градБ and l.B==градА) осигурява независимо от подредбата на градовете
    # да бъде намерена такава двойка драдове, т.к. когато подаваме данните на функцията може да ги подадем неподредени
    filtered_locs=[l for l in GS_list if (l.A == градА and l.B == градБ) or (l.A == градБ and l.B == градА)]
    # филтрираме по еднакъв начин данните в km и filtered_locs,
    # като по този начин ще има съответствие в индексите, когато търсим min или max
    if km:
        if MM=="min":
            path=min(km)
            ind=km.index(path)
            s="\nНай-късото разстояние между градовете %s и %s е %d км по маршрут %s." %(градА,градБ,filtered_locs[ind].AB,filtered_locs[ind].R)
        else:
            path=max(km)
            ind=km.index(path)
            s="\nНай-дългото разстояние между градовете %s и %s е %d км по маршрут %s." %(градА,градБ,filtered_locs[ind].AB,filtered_locs[ind].R)
    else:
        s="Няма описано разстояние за градовете %s и %s" %(градА,градБ)
    return s
print(Min_Max_route_in_GS_list_2(L,"София","Варна"))