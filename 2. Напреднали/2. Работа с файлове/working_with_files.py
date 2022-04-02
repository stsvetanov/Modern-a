# 1) Четене на .json, красиво принтиране, запис като дейта фрейм, експорт (.csv,.xlsx)
# 2) Четене на .csv, запис като дейта фрейм, показване на брой записи и колони и имена на колоните, експорт (.json,.xlsx)
# 2) Четене на .xls, запис като дейта фрейм, показване на брой записи и колони и имена на колоните, експорт (.csv,.json)

# Task 1)
import json
import pandas as pd

jname="./exmple.2.json"
cname="./invoice_2019_5_exported_1_utf8.csv"
xname="./invoice_2019_5.xls"

# jopen=open(jname,'r') # Отваряне на .json файла за четене
# jdata= json.load(jopen) # Зареждане на .json данните
# print (json.dumps(jdata, sort_keys=True, indent=4)) # красиво отпечатване
#
# jdata=pd.read_json(jname) # Отваряне, прочитане и запис в дейта фрейм
# print(jdata.head()) # принтване на първите 5 записа
#
# with pd.ExcelWriter('exmple.2.xls') as writer:
#     jdata.to_excel('exmple.2.xls',sheet_name='sheet 1',index=False)
# jdata.to_csv('exmple.2.csv',index=False)

# # Task 2)
# cdata=pd.read_csv(cname,sep=';')
# print(cdata.head())
# print("Брой редове: %d, брой колони: %d\n" %(cdata.shape[0],cdata.shape[1]))
# print("Имена на колоните:\n")
# print(cdata.columns)
# cdata.to_excel('csv_xls.xlsx',index=False)
# cdata.to_json('csv_json.json',force_ascii=False)

# Task 3)
xdata=pd.read_excel(xname,sheet_name='details_1')
print(xdata.head())
print("Брой редове: %d, брой колони: %d\n" %(xdata.shape[0],xdata.shape[1]))
print("Имена на колоните:\n")
print(xdata.columns)
# Принцип на коректен запис на един .json файл от дейта фрейм структура:
# 1) всеки един запис от дейта фрейма трябва да бъде представен като елемент на списък
# 2) всеки елемент от списъка представлява речник с ключове-имената на колоните и стойности-съответните клетки
# 3) списъкът се явява стойност в нов речник с единствен ключ, който кръщаваме както решим
# 4) експортираме в .json като използваме json modula, а не pandas

cols=xdata.columns
L=[]
for r in range(xdata.shape[0]):
    X=dict()
    for c in range(xdata.shape[1]):
        X[cols[c]]=str(xdata.iloc[r,c])
        # превръщаме в стринг задължително, когато искаме да експортираме в .json формат
    L.append(X)
D={'data':L}
xdata.to_csv('xls_csv.csv',index=False)
# експорт посредством pandas
# xdata.to_json('xls_json.json',force_ascii=False)

json_object = json.dumps(D, indent=4,ensure_ascii=False)
# сериализация, т.е. превръщаме речника в поток от данни
# ensure_ascii=False осигурява правилен експорт на кирилица !!!
with open('xls_json_2.json', "w") as outfile: # създаване нов празен файл с опция за запис в него
        outfile.write(json_object) # записваме потока от данни в нов новия файл
# Задължително затваряме файловете след като сме приключили работа с тях
outfile.close()