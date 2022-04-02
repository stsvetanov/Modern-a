# Имаме магазин дрехи с определени наличности. Да се направят подходящи класове и методи,
# такива че да може да се решат следните задачи:
# 1. Да се провери дали дадена заявка може да бъде изпълнена
# (т.е. разполагаме ли със съответните дрехи и количества)
# 2. Ако дадена заявка може да бъде изпълнена да се изпълни и да се определи общата печалба от заявката
# 3. Какви количества са останали след заявката

# ______ОПисание на класовете__________
class Dreha():
    # Описва конкретна дреха, като ако не бъдат подадени стойности
    # при създаването на нов обект от този клас, то ще се вземат всички първи стойности от
    # речника за ограниченията.
    ограничения={
    "размери":["XSS","XS","S","M","L","XL","XXL","XXXL",'не е посочено'],
    "принт":["на точки", "на райета","каре","цветя","фигури","без шарки","не е посочено"],
    "цвят":["бяло","жълто", "оранжево","розово","червено","синьо","зелено","кафяво","черно","сребристо","златисто","многоцветно","не е посочено"],
    "тип":["рокля","панталон", "пола","блуза","палто","яке","елек","не е посочено"],
    "мода":["дамска колекция", "мъжка колекция", "детска колекция","не е посочено"]
    }
    def __init__(self,
                 fmc=ограничения["мода"][0],
                 tip=ограничения["тип"][0],
                 marka="неизвестна",
                 color=ограничения["цвят"][0],
                 sharka=ограничения["принт"][0],
                 razmer=ограничения["размери"][0]
                 ):
        # Проверява дали подадените стойности са валидни и ако не са:
        # взима последната стойност за конкретния ключ от речника с ограниченията

        if fmc in self.ограничения["мода"]:self.moda=fmc
        else:self.moda=self.ограничения["мода"][-1]

        if tip in self.ограничения["тип"]:self.type=tip
        else:self.type = self.ограничения["тип"][-1]

        if color in self.ограничения["цвят"]:self.color=color
        else:self.color = self.ограничения["цвят"][-1]

        if sharka in self.ограничения["принт"]:self.pattern=sharka
        else:self.pattern = self.ограничения["принт"][-1]

        if razmer in self.ограничения["размери"]:self.size=razmer
        else:self.size = self.ограничения["размери"][-1]

        self.mark = marka
    def __repr__(self):
        s="%s %s %s %s %s %s" %(self.moda,self.mark,self.size, self.type, self.color,self.pattern)
        return s

class Magazin(Dreha):
    def __init__(self,Dreha,kolichestwo,pro_cena,pechalba,prodavbi):
        self.dreha=Dreha
        self.q=kolichestwo
        self.price=pro_cena
        self.profit=pechalba
        self.sold=prodavbi
    def check(self,Dreha,qual):
        ch_1=self.dreha==Dreha
        ch_2=self.q>=qual
        if ch_1 and ch_2: return True
        else: return False
    def porychka(self,q):
        self.q=self.q-q
        self.sold=self.sold+q
        return q*self.profit
    def __repr__(self):
        s="%s %d %.2f %.2f" %(self.dreha,self.q,self.price,self.profit)
        return s
    def get_q(self):
        s = "От артикул '%s' разполагаме с %d бройки с единична продажна цена %.2f." % (self.dreha, self.q,self.price)
        return s
    def get_profit(self):
        s = "От артикул '%s' са продадени общо %d броя с обща печалба в размер на %.2f лева." % (self.dreha, self.sold, self.sold*self.profit)
        return s

# __________MAIN CoDE______________
d1=Dreha("дамска колекция","панталон","Kelvin Klein","многоцветен","каре","S")
d2=Dreha("дамска колекция","рокля","Kelvin Klein","червено","на точки","S")
d3=Dreha("дамска колекция","рокля","Dorothy Perkins","червено","на райе","S")

MDrehi=[Magazin(d1,5,75,15,12),Magazin(d2,1,135,45,8),Magazin(d3,0,185,65,5)]
print("\nНаличности в магазина:")
for md in MDrehi:
    print(md.get_q())

LDrehi_porychka=[(d1,1),(d3,2)]
print("\nВие поръчахте:")
for ld in LDrehi_porychka:
    print("От артикул %s са поръчани %d бройки"%(ld[0],ld[1]))
print('\nОбработка на поръчката:')
Suma_porychka=0
Pechalba_ot_porychkata=0
for ld in LDrehi_porychka:
    br = 0
    for md in MDrehi:
        if md.check(ld[0],ld[1]):
            br+=1
            Suma_porychka+=ld[1]*md.price
            Pechalba_ot_porychkata+=ld[1]*md.profit
            break
    if br>0:
        print("Артикулът '%s' може да бъде поръчан." % (ld[0]))
        print("...поръчване и обновяване на информацията...")
        md.porychka(ld[1])
        print("Поръчката е направена. Магазинът разполага със:")
        print(md.get_q())
    else:
        print("Артикулът '%s' не може да бъде поръчан." % (ld[0]))
print("\nОбщата сума на поръчката е за %.2f лева."%(Suma_porychka))
print("\nОбщата печалба от поръчката е за %.2f лева."%(Pechalba_ot_porychkata))
print("\nПродажби и печалби:")
for md in MDrehi:
    print(md.get_profit())
