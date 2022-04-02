# зоологическа градина
# различен тип клетки: малки животни, клетки за големи животни, клетки за птици, и клетки за водоплаващи
# всяко животно: старо, възрастно, младо; пол: мъжко, женско; име на български и на латински; режим на хранене
# режим на хранене: с какво се храни, схема на дневните дажби (сутрин:x kg; обед: y kg; вечер: z kg)

# 1. Да се изведе пълната информация за конкретно животно по неговото име (__repr__)
# 2. Да се намери общия брой на животните, обитаващи клетки за големи животни:
#     - да се напише метод, който връща стойност True ако животното, обитава клетка за големи животни
class zoo_name():
    def __init__(self,name_bg='',name_lat=''):
        self.name_bg = name_bg
        self.name_lat = name_lat
    def __repr__(self):
        s = self.name_bg + '\n'
        s += self.name_lat + '\n'
        return s
class Zoo(zoo_name):

    def __init__(self, name=zoo_name(),sex='',age='',cage='',diet=''):
        self.name=zoo_name()
        if sex in {"мъжко животно", "женско животно"}:
            self.sex=sex
        else:
            self.sex="error"

        if age in {"старо животно", "възрастно животно", "младо животно"}:
            self.age=age
        else:
            self.age="error"

        if cage in {"клетка за малки животни", "клетка за големи животни", "клетка за птици", "клетка за водоплаващи"}:
            self.cage=cage
        else:
            self.cage="error"
        diet_cond_1=isinstance(diet,dict)
        if diet_cond_1:
            diet_cond_2=list(diet.keys)==['сутрин','обед','вечер']
            if diet_cond_2:
                self.diet=diet
            else: self.diet="error"
        else: self.diet="error"
    def big_cage(self):
        if self.cage=="клетка за големи животни":
            return True
        else:
            return False
    def dieta_str(self):
        if isinstance(self.diet,str):
            s= self.diet
        else:
            s="сутрин: " + str(self.diet['сутрин'])
            s+=" обед: "+ str(self.diet['обед'])
            s += " вечер: " + str(self.diet['вечер'])
        return s
    def zoo_errors(self):
        Errors_in_ZooPark = set()
        cond_1 = self.sex == "error"
        cond_2 = self.age == "error"
        cond_3 = self.cage == "error"
        cond_4 = self.diet == "error"

        if cond_1:
            Errors_in_ZooPark.add('sex')
        if cond_2:
            Errors_in_ZooPark.add('age')
        if cond_3:
            Errors_in_ZooPark.add('cage')
        if cond_4:
            Errors_in_ZooPark.add('diet')
        return Errors_in_ZooPark
    def __repr__(self):
        s=self.name.__repr__() +'\n'
        s+=self.sex+'\n'
        s+=self.age+'\n'
        s+=self.cage+'\n'
        s+=self.dieta_str()
        return s

# диета={'сутрин':5, 'обед': 15, 'вечер': 8}
# звяр=Zoo("Тигър","Tiger","мъжко животно","възрастно животно","обитава клетка за големи животни",диета)
# zwqr=Zoo()

# въвеждане на 10 животни в зоологическата градина
ZooPark=[]
for i in range(10):
    if i%3==0:
        звяр = Zoo(name=zoo_name(name_bg=str(i)), cage='клетка за големи животни')
    else:
        звяр=Zoo(name=zoo_name(name_bg=str(i)),cage='клетка за малки животни')
    ZooPark.append(звяр)

print(ZooPark)
# зад.1: Кои животни обитават големи клетки?
# зад.2: Колко са животните, които обитават големи клетки?
# зад.3: В кои атрибути на класа за въведените животни в зоопарка има грешни данни?
br=0
Error_in_ZooPark=set()
for zp in ZooPark:
    # решението на зад.1 и 2:
    if zp.big_cage()==True:
        br+=1
        print(zp.name.name_bg)
    ## Стандартно решение на зад.3:
    # cond_1= zp.sex=="error"
    # cond_2= zp.age=="error"
    # cond_3= zp.cage=="error"
    # cond_4= zp.diet=="error"
    # if cond_1 :
    #     Errors_in_ZooPark.add('sex')
    # if cond_2 :
    #     Errors_in_ZooPark.add('age')
    # if cond_3 :
    #     Errors_in_ZooPark.add('cage')
    # if cond_4 :
    #     Errors_in_ZooPark.add('diet')

    # Решение чрез метода за откриване на грешки в данните
    Error_in_ZooPark.update(zp.zoo_errors())
print(br)
print(Error_in_ZooPark)
