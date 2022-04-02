# Елена си празнува рождения ден в бар,
# дава на бармана списък с имена на гостите и годините им.
# Хората от този списък не е нужно да плащат.

# Помогнете на бармана да състави програма,
# 1) която му помага да разбере дали човек дошъл на бара фигурира
# в този списък съответно дали трябва да си плати или не,
# 2) дали е над 18г., за да знае дали може да му продаде алкохол или не,
# 3) и която записва до имената им - поръчката и цената,
# 4) за да може Елена да плати накрая.


import random as rd

# --------------DATA----------------
NameList=['Анжела','Гергана','Йоана','Кристиян','Марио','Рая','Сузана','Виктория','Огнян','Калоян','Тодор','Николай','Ивета','Николета','Ивона','Фелиция'] #Съдържа имената на студентите като стрингове
age_lower_limit=15
age_upper_limit=68
AgeList=[rd.randint(age_lower_limit,age_upper_limit) for item in NameList]
NameAgeList=list(zip(NameList,AgeList))
AlkoholList=['водка','ракия','коняк','уиски','вино','ликьор','алкохолен коктейл']
AlkoholPrice=[5,7,7,15,8,10,25]
NotAlkoholList=['кола','пепси','енергийна напитка','сок','вода','газирана напитка','безалкохолен коктейл']
NotAlkoholPrice=[3,3,7,8,4,3,12]
DrinkList=AlkoholList+NotAlkoholList
DrinkPrice=AlkoholPrice+NotAlkoholPrice
Drinks=dict(zip(DrinkList,DrinkPrice))
D_bar=dict()

#----------DEFINITIONS--------------
def check_conditions_to_make_order(person,drink):
    check_name = person in NameList
    check_orders = person not in D_bar
    check_drink = drink in AlkoholList
    for v in NameAgeList:
        if v[0]==person:
            check_age=v[1]>=18
            break
    if all([check_name,check_orders,check_age,check_drink]): status=1 # създаваме нов ключ, може да пие алкохол
    elif all ([check_name,check_orders,not check_age,not check_drink]): status=2 # създаваме нов ключ, не може да пие алкохол
    elif all ([check_name,check_orders,not check_age,check_drink]): status=3 ## създаваме нов ключ, с рандъм безалкохолно
    elif all([check_name, check_orders, check_age, not check_drink]):status = 4 # създаваме нов ключ, поръчал беалкохолно
    elif all([check_name, not check_orders, check_age, check_drink]):status = 10  # добавяме, може да пие алкохол
    elif all([check_name, not check_orders, not check_age, not check_drink]):status = 20  # добавяме, не може да пие алкохол
    elif all([check_name, not check_orders, not check_age, check_drink]):status = 30  ## добавяме, с рандъм безалкохолно
    elif all([check_name, not check_orders, check_age, not check_drink]):status = 40  # добавяме, поръчал беалкохолно
    elif not check_name: status=0 # не влиза в базата
    return status
def make_order(person,drink,price):
    # person се подава само като име
    global D_bar
    global NameList
    global NameAgeList
    global AlkoholList

    nadrinks=list(zip(NotAlkoholList,NotAlkoholPrice))
    status=check_conditions_to_make_order(person,drink)
    if status == 1:
        # създаваме нов ключ, може да пие алкохол
        D_bar[person] = [(drink, price)]
    elif status == 2:
        # създаваме нов ключ, за лице под 18, което е поръчало безалкохолно
        D_bar[person] = [(drink, price)]
    elif status == 3:
        ## създаваме нов ключ, с рандъм безалкохолно за лице под 18
        # print("На лица под 18 години не сервираме алкохол.")
        random_na_drink = rd.choice(nadrinks)
        D_bar[person] = [(random_na_drink[0], random_na_drink[1])]
    elif status == 4:
        # създаваме нов ключ, поръчал беалкохолно
        D_bar[person] = [(drink, price)]
    elif status == 10:
        # добавяме, може да пие алкохол
        D_bar[person].append((drink, price))
    elif status == 20:
        # добавяме, за лице под 18, което е поръчало безалкохолно
        D_bar[person].append((drink, price))
    elif status == 30:
        ## добавяме, с рандъм безалкохолно
        # print("На лица под 18 години не сервираме алкохол.")
        random_na_drink = rd.choice(nadrinks)
        D_bar[person].append((random_na_drink[0], random_na_drink[1]))
    elif status == 40:
        # добавяме, поръчал беалкохолно
        D_bar[person].append((drink, price))
    elif status == 0:
        # не влиза в базата
        print("Клиентът не е от списъка на Елена.")
        pass
    else: print("Unknowkn Error...")
def consumation_by_name():
    global D_bar
    global NameAgeList
    NoConsumation=[] # Кой не е поръчвал нищо
    Consumation=dict()# За каква сума всеки е поръчал
    for n in NameAgeList:
        if n[0] not in D_bar:
            NoConsumation.append(n[0])
    for k,v in D_bar.items():
        Consumation[k]=0
        prices=[]
        for vv in v:
            prices.append(vv[1])
        L=sum(prices)
        if L>0: Consumation[k]=L
    return (NoConsumation,Consumation)
def auto_orders(number_of_orders):
    global NameList,NameAgeList,AlkoholList, D_bar,Drinks
    drinksAsList=list(Drinks.items())
    for i in range(number_of_orders):
        chosen_person=rd.choice(NameList)
        random_drink_item=rd.choice(drinksAsList)
        chosen_drink=random_drink_item[0]
        chosen_price=random_drink_item[1]
        make_order(chosen_person,chosen_drink,chosen_price)

# ----------MAIN----------------
auto_orders(5)
make_order('Фелиция','вино',7)
make_order('Фелиция','вино',17)
for k,v in D_bar.items():
    print(k,v)
total=consumation_by_name()
s='Гости на партито, които не са консумирали нищо: '
try:
    s+=','.join(total[0])
except:
    s+='няма такива :)'
print(s)

total_cost=0
for k,v in total[1].items():
    total_cost+=v
    print("%s е консумирал(а) общо на стойност: %d лева" %(k,v))
print("Елена трябва да плати на бармана за партито общо %d лева" %(total_cost))



