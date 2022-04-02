import json
# json_data = '{"data":[{"name": "Brian", "city": "Seattle"},{"name": "Arny", "city": "Washington"}]}'
# # Всеки запис от JSON се задава в {}, като се използва структурата на данните
# # Еквивалентът на JSON записите се представя посредством структура от тип речник
# # Задължителен елемент от записа е включването на главния ключ от структурата, в този случай "data":
# # Записите се изброяват заключени в една двойка квадратни скоби, а всеки запис с двойка {}
# # за разделител между записите се използва запетая
# python_obj = json.loads(json_data) # python_obj е речник, който създаваме от .json стринг
# print(python_obj.keys())
# for x in python_obj["data"]:
#         print (x["name"])
# # Pretty printing JSON data
# print (json.dumps(python_obj, sort_keys=True, indent=2))

file_name="/Users/valerina/PycharmProjects/1386/Работа с JSON-20210517/exmple.2.json"
example2=open(file_name,'r') # Отваряне на .json файла за четене
jdata= json.load(example2) # Прочитане на файла и конвертиране в структурата речник
# print (json.dumps(jdata, sort_keys=True, indent=2))
#
# L=[]
# # Задача: да се изведе списък с номерата на всички стаи, които са с квадратура >60
# for x in jdata["medical"]: #jdata["medical"] е списък от еднотипни речници, т.е. х е речник
#         if x["sq-ft"]>60: L.append(x["room-number"])
# print(L)
#
# L=[]
# # Задача: да се запише нов .json файл, който съдържа пълната информация за стаите, които са с квадратура >60
# for x in jdata["medical"]: #jdata["medical"] е списък от еднотипни речници, т.е. х е речник
#         if x["sq-ft"]>60: L.append(x)
# jdata["medical"]=L
#
# # Задача: да се изведат номерата на стаите, които не са за преглед на пациенти "examination"
# L=[]
# for x in jdata["medical"]: #jdata["medical"] е списък от еднотипни речници, т.е. х е речник
#         if x["use"]!="examination": L.append(x["room-number"])
# print(L)

# Задача: Да се запише нов .json файл, който съдържа пълната информация за стаите, като:
#         преименувате на български ключовете и стойностите
Dkeys={"medical":"Информация",'room-number':"Номер на стая", 'use':"Предназначение", 'sq-ft':"Площ", 'price':"Цена на ден за престой"}
Duse={'waiting':"Чакалня", 'office':"Кабинет", 'reception':"Рецепция", 'examination':"Приемна"}
# # Вариант 1
# L=[]
# for x in jdata["medical"]:
#         D=dict()
#         D["Номер на стая"]=x['room-number']
#         D["Предназначение"] = Duse[x['use']]
#         D["Площ"] = x['sq-ft']
#         D["Цена на ден за престой"] = x['price']
#         L.append(D)
# jdata=dict()
# jdata["Информация"]=L

# Вариант 2
L=[]
for x in jdata["medical"]:
        D = dict()
        for k,v in x.items():
                if k!="use":D[Dkeys[k]]=v
                else:D[Dkeys[k]]=Duse[v]
        L.append(D)
jdata=dict()
jdata["Информация"]=L




# Запис на .json file
new_json_fn="/Users/valerina/PycharmProjects/1386/Работа с JSON-20210517/exmple.2_new.json"
json_object = json.dumps(jdata, indent=4,ensure_ascii=False) # сериализация, т.е. превръщаме речника в поток от данни
# ensure_ascii=False осигурява правилен експорт на кирилица !!!
# Writing to sample.json
with open(new_json_fn, "w") as outfile: # създаване нов празен файл с опция за запис в него
        outfile.write(json_object) # записваме потока от данни в нов новия файл

# Задължително затваряме файловете след като сме приключили работа с тях
example2.close()
outfile.close()