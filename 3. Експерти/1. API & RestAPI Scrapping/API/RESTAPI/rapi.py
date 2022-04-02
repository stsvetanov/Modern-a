# Работа с REST & API чрез модула requests
import requests as r
url='https://translate.yandex.net/api/v1.5/tr.json/translate'
API_key='trnsl.1.1.20200518T082618Z.9e1f20f62f387c4c.60427769efe6430b0a7b46ee569187bfab048d08'
# s = r.get(url)
# headers = {'Content-Type': 'application/json', 'User-Agent': 'Python Teacher', 'Accept': 'application/vnd.github.v3+json'}
# # headers е речник с параметрите на заявката
# s.status_code # връща статуса на заявката, т.е. дали генерира грешка и ако да-каква. При код 200 => всичко е ОК
# s.headers['content-type'] # връща типа на съдържанието на страницата
# s.text # връща текста
# s.json # връща текста, форматиран като .json, а .json има формата на речник !!!
# Формат на резултата с s.json() към API-то на Yandex за превод:
# {"code":200,"lang":"bg-en","text":["Where the dog"]}
# -----------------------------------------------------
# Задача: Да се достъпи API Yandex Translation и като се използват произволно избрани езици (от тези, които се поддържат)
# да се преведе един същи текст. Информацията да се форматира по една от следните две схеми:
# 1) Структура на събраните данни:
#   схемата за превод: bg-en
#   оригиналната фраза за превод
#   превода
# 2) Структура на събраните данни:
#   схемата за превод: Език, на който се превежда
#   оригиналната фраза за превод
#   превода
# Варианти за обработка:
# 1) Вложен списък, и запис като текстов файл .csv
# 2) Речници като елементи на списък и запис като .json файл
# 3) Класове и запис като текстов файл .csv или .xls
# 4) Таблични данни в Pandas и запис като .xls, .csv или .json

# ОБЩА ЧАСТ на кода
import pandas as pd
import random as rd
import json

# Прочитане на файла с поддържаните езици за превод от Yandex
# Информацията е извлечена от:
# https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages
f="/Users/valerina/PycharmProjects/test/RESTAPI/languadges.csv"
lang=pd.read_csv(f,sep=";")
lang=lang.iloc[:,0:2] # Първата колона е кода, а втората името на езика
#print(lang)
# Създаваме списък от 10 случайни превода от български на друг език и ги записваме спрямо изискването на API услугата,
# да бъдат представени във формата: '<lang_from>-<lang_to>'
langs=["bg-"+rd.choice(lang.iloc[:,0]) for i in range(10)]
#print(langs)
text_to_be_translated="Първият буден сутринта беше петела"

# От тук нататък всеки вариант за обработка ще бъде представен с отделна функция
def read_url(languadges,url=url,API_key=API_key,text2translate=text_to_be_translated):
    params = dict(key=API_key, text=text2translate, lang=languadges)
    # params са паметри, с които си служи самото API, т.е. това са критериите на заявката към API-то
    res = r.get(url, params=params)
    res = dict(res.json())['text'][0]
    # res връща конкрентия превод
    return res
def with_class_structure():
# Създаваме клас със структура, каквато е описана
    class Превод():
        def __init__(self,text,lang,translation):
        self.phrase=text
        self.lang_code=lang
        self.translated=translation
        def __repr__(self):
            s="Фраза: %s\nЕзици: %s\nПревод: %s\n" %(self.phrase,self.lang_code,self.translated)
            return s
    L=[] # празен списък с обекти от тип Превод()
    for i in range(10):
        res=read_url(langs[i])
        # запълване на L:
        li=Превод(text_to_be_translated,langs[i],res)
        L.append(li)
    return L
def with_list_of_dictionaries():
# списък от речници => .json, позволява импорт/експорт и обработка
# [{1:'Ivan',2:'Petrov',3:25},{1:'Maria',2:'Petrova',3:23},{1:'Ivan',2:'Angelov',3:25}]
    L=[]
    for i in range(10):
        res = read_url(langs[i])
        # запълване на L:
        di={'Phrase':text_to_be_translated, 'Languadges':langs[i],'Translation':res}
        L.append(di)
    return L
def with_Pandas_dataframes(type_of_choise=0,col_names=column_names_1):
# да използваме dataframe от Pandas за да съхраняваме и обработваме данни
# крайният резултат може да бъде записан като .csv

# При type_of_choise=0 се използва column_names_1, т.е. I-ви вариант на структурата за резултата
# При type_of_choise=1 се използва column_names_2, т.е. II-ри вариант на структурата за резултата

    results = pd.DataFrame(columns = col_names)
    # извеждане на езиковата схема
    for i in range(10):
        res=read_url(langs[i])
        if type_of_choise==0:
            results.loc[i,column_names_1[0]]=langs[i]
            results.loc[i,column_names_1[1]]=res
        elif type_of_choise==1:
            ll=lang.iloc[:,0]==langs[i][-2:]
            lre=lang[ll]
            lre=lre.values[0][1] # със .values превръщаме в numpy array,
            # като [0] връща индекса и стойността под формата array, т.е
            # има 2 елемента, и тогава с [1] вземаме 2-я, защото това е Езикът !!!
            results.loc[i,column_names_2[0]]=lre
            results.loc[i,column_names_2[1]]=res
    return results
def with_Lists():
    L = []  # празен списък с обекти от тип Превод()
    for i in range(10):
        res = read_url(langs[i])
        # запълване на L:
        li = [langs[i], text_to_be_translated, res]
        L.append(li)
    return L


# Основна програма с използване на дефинираните функции:
# ----------------------------------------------------------
# Използване на речници и запазване в .json формат:
D=with_list_of_dictionaries()
with open('translated.json', 'w') as json_file:
    json.dump(D, json_file)

# Прочитане на запазения .json файл като списък от речници
# with open('translated.json', 'r') as json_file:
#     d=json.load(json_file)
#     print(type(d))
#     print(d)
# ----------------------------------------------------------
# Използване на класове:
L=with_class_structure
print(L)
output_file = open("class_objects_out.txt", "w")
for i in L:
    output_file.write(i)
output_file.close()
# ----------------------------------------------------------
# Използване на Pandas и запис като .xls
column_names_1 = ["Езикова схема", "Превод"]
column_names_2 = ["Език", "Превод"]
#pth="/Users/valerina/PycharmProjects/test/RESTAPI/"
fo_1="results_1.xls"
fo_2="results_2.xls"
results=with_Pandas_dataframes()
#print(results)
results.to_excel(fo_1,sheet_name="Sheet_1",index=False)

results=with_Pandas_dataframes(1,column_names_2)
#print(results)
results.to_excel(fo_2,sheet_name="Sheet_1",index=False)

# ----------------------------------------------------------
# Използване на вложена структура от списъци и запис като .csv
output_file = open("lists_out.csv", "w")
header="Езици;Текст;Превод"
output_file.write(header)
L=with_Lists()
for i in L:
    s=';'.join(i)
    output_file.write(s)
output_file.close()






