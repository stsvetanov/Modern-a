# Даден е един .csv файл.
# 1.Да се прочете и запази като дейта фрейм в променливата original_copy.
# 2.Да се направи копие на дейта фрейма в променливата new_copy.
# 3.Да се напише скрипт, който отразява структурата на original_copy в клас, описващ един ред от дейта фрейма.
# 4.Да се напише функция, която преобразува данните от дейта фрейма в списък от обекти от класа
# ** Вариант 1: една функция за всички данни наведнъж
# ** Вариант 2: една функция за конвертиране на един ред към един обект и използване с apply/map
# 5.Да се напише метод за класа, който проверява дали "извикания номер" отговаря на шаблона да започва с "359"
# и преформатира номера при нужда:
# * има номера, които започват с 00359=> става 359
# * има номера, които започват с 02   => става 3592
# * има номера, които започват с 052  => става 35952
# * има номера, които започват с 0700 => тези не ги променяме
# * има номера, които започват с 08 => става 3598
# 6.Да се напише функция, която релизира филтриране на списъка с обекти по зададени номера на колоните от дейта фрейма и условия за тях.
# 7.Реализирайте 5. и 6. чрез Pandas като използвате new_copy
# 8.Експортирайте списъка с обекти като .json файл.
#       ** Това означава, че всеки един обект трябва да го преобразуваме в структура от тип речник
#       *** Може да се използваме функция за преобразуването на един обект и да я използваме с map()

fname='./invoice_2019_5_exported_1_utf8.csv'
import pandas as pd
original_copy=pd.read_csv(fname,encoding="utf8",sep=';')
# original_copy=pd.read_csv(fname)
# encoding="cp1251" oсигурява прочитането на кирилица, кодирана с Windows 1251
# encoding="ascii"
# encoding="utf8"
print(original_copy.head())
print(original_copy.columns)
# В структурата на класа няма да включим колони:
# 'Вид продукт' (5), 'GPRS(KB)' (7), '*' (9), 'Unnamed: 10'(10)
# В скобите е номера на колоната в дейта фрейма

new_copy=original_copy.reindex
class Calling():
    def __init__(self, c0="",c1="",c2="",c3="",c4="",c6="",c8=""):
        self.caller_id=str(c0)
        self.date = str(c1)
        self.time=str(c2)
        self.calling_id=self.calling_id_check(c3)
        self.service=str(c4)
        self.duration=str(c6)
        if c8=='' or c8==' ' :c8=0
        self.price=round(float(c8),2)
    def to_json_str(self):
        # Представяне на един обект от класа под формата на речник
        j={'caller_id':self.caller_id,'date':self.date,'time':self.time,'calling_id':self.calling_id,'service':self.service,'duration':self.duration,'price':self.price}
        return j
    def calling_id_check(self,tel_number):
        s=str(tel_number)[::-1]
        if s.endswith("95300"): s=str(tel_number)[2:]
        elif s.endswith("20") or s.endswith("250") or s.endswith("80"):s="359"+str(tel_number)[1:]
        else: s=str(tel_number)
        return s
    def __repr__(self):
        return self.to_json_str().__str__()
L=[] # Празен списък за попълване с обекти от класа
D=[]
for row in range(original_copy.shape[0]):
    k=original_copy
    L.append(Calling(k.iloc[row,0],k.iloc[row,1],k.iloc[row,2],k.iloc[row,3],k.iloc[row,4],k.iloc[row,6],k.iloc[row,8]))
    D.append(L[-1].to_json_str())
print(L[:5])
# 6.Да се напише функция, която релизира филтриране на списъка с обекти по зададени номера на колоните от дейта фрейма и условия за тях.
# Може да се представи чрез речник от вида:
# 0-'Избиращ номер',
# 1-'Дата',
# 2-'Начален час',
# 3-'Избран номер',
# 4-'Вид услуга',
# 6-'Продължителност',
# 8-'Стойност',

# FILTER={0:["сравнение","някаква стойност"],
#  1:["сравнение–1","стойност-1","сравнение-2",'стойност-2'],date/time
#  2:["сравнение–1","стойност-1","сравнение-2",'стойност-2'],date/time
#  3:["сравнение","някаква стойност"],
#  4:["сравнение","някаква стойност"],
#  6:["сравнение-3","някаква стойност","сравнение-4","някаква стойност"],date/time
#  8:["сравнение-5","някаква стойност","сравнение-4","някаква стойност"]}

# сравнение: може да бъде == или != "започва със", "завършва на", "съдържа"
# сравнение–1: може да бъде: == (за конкретна дата)
#                            >=
#                            >
#                            "" от най-малката дата
# сравнение–2: може да бъде:
#                            <=
#                            <
#                            "" от най-голямата дата
# "сравнение-3/4" може да бъде: ==,>,<,>=,<=
# "сравнение–5": може да бъде:==,>,<,>=,<=, ot-do

def check_to_str(a,condition_string,b):
    # a е проверявания елемент
    # b е стойността с която сравняваме а

    if condition_string =="започва със":return a.find(b)==0 # връща True ако е истина
    elif condition_string =="завършва на":return a.endswith(b) # връща True ако е истина
    elif condition_string =="съдържа":return a.find(b)!=-1 # връща True ако е истина
    elif condition_string =='==':return a==b
    elif condition_string =='!=':return a!=b
    elif condition_string =='>':return a>b
    elif condition_string =='<':return a<b
    elif condition_string =='>=':return a>=b
    elif condition_string =='<=':return a<=b

FILTER={0:["==","359896824044"]}
def filter_objects(filters=dict()):
    global L # списъка с обектите
    G=set() # ще събирам всички обекти, които отговарят на поставените условия
    if filters!=dict(): # Ако филтърът не е празен:
        # Съответства на опцията ANY (OR), т.е. което и да е условие
        for l in L:
            if 0 in filters.keys():
                f=check_to_str(l.caller_id,filters[0][0],filters[0][1])
                if f:G.add(l)
            if 3 in filters.keys():
                f=check_to_str(l.calling_id,filters[0][0],filters[0][1])
                if f:G.add(l)
            if 4 in filters.keys():
                f=check_to_str(l.service,filters[0][0],filters[0][1])
                if f:G.add(l)
            if 1 in filters.keys():pass
            if 2 in filters.keys():pass
            if 6 in filters.keys(): pass
            if 8 in filters.keys():
                cond_4 = 8 in filters.keys()
                cond_5 = len(filters[8]) == 2
                if cond_4 and cond_5:
                    f = check_to_str(l.price, filters[0][0], filters[0][1])
                    if f: G.add(l)
                elif cond_4 and not cond_5:
                    f_1 = check_to_str(l.price, filters[0][0], filters[0][1])
                    f_2 = check_to_str(l.price, filters[0][2], filters[0][3])
                    if f_1 and f_2: G.add(l)

        # Функцията продължава с if проверка за наличието на всеки един възможен ключ
        # Всяка следваща обработка трябва да продължи да работи с G а не със L, това може
        # да реализира чрез допълнителна проверка дали G е празно или не, ако не е празно филтрирането е върху G
        # ! Филтрите в този вид на кода не се прилагат в реда, в който са подадени в речника
    return list(G)

testing=filter_objects(FILTER)
print(len(testing))
print(testing[:5])
# Запис на .json file
import json
jdata={'invoice':D}
new_json_fn="./exam_export.json"
json_object = json.dumps(jdata, indent=4,ensure_ascii=False)
# сериализация, т.е. превръщаме речника в поток от данни
# ensure_ascii=False осигурява правилен експорт на кирилица !!!
# Writing to sample.json
with open(new_json_fn, "w") as outfile: # създаване нов празен файл с опция за запис в него
        outfile.write(json_object) # записваме потока от данни в нов новия файл

# Задължително затваряме файловете след като сме приключили работа с тях
outfile.close()