import pandas as pd

# променливата pth съдържа пълния път до файла и следва да се модифицира
# pth='/Users/valerina/PycharmProjects/1386/C464597S2-Работа в час-200266/13877-Александра Миронова_1479446_assignsubmission_file_/ExelTable.xlsx'
pth='./ExelTable.xlsx'
#exel to csv
read_file = pd.read_excel (pth)
read_file.to_csv ('YPex.csv', index = None, header=True)

#exel to json
excel_data_fragment = pd.read_excel(pth, sheet_name='Sheet1')
json_str = excel_data_fragment.to_json()
with open('YPex.json', "w") as outfile:
    outfile.write(json_str)
    outfile.close()
print('Excel Sheet to JSON:\n', json_str)

# Обработка на .xlsx файла:
# 1) Въпрос от тип филтриране: кои са роклите, от които имаме по 3 бройки?
# 2) Въпрос от тип  обобщение: по колко бройки имаме ако групираме по стил и размер?
# 3) Ако са продадени по две зелени рокли от всеки вид (1 запис е един вид) и са ни върнали по една оранжева, покажете новите количества за всеки тип рокля.

# Решения:
# 1)
df=read_file
cond=df.iloc[:,2]==3
filtered_data=df[cond]
print(filtered_data)
# 2)
# вариант 1:
k=df.groupby(['style','size']).sum()
print(k)
# вариант 2:
pivot=pd.pivot_table(df, values='amount',index=['size','style'])
print(pivot)
# 3)
cond=df.iloc[:,1]=='green'
filtered_data=df[cond].copy()
filtered_data.iloc[:,2]-=2
df[cond]=filtered_data

cond=df.iloc[:,1]=='orange'
filtered_data=df[cond].copy()
filtered_data.iloc[:,2]+=1
df[cond]=filtered_data

print(df)

# excel to xml
# 1) Първо трябва да решим каква схема ще използваме за XML-a
# <dress>
#     <item>
#         <dress>'fairy'</dress>
#         <color>'blue'</color>
#         <amount>3</amount>
#         <style>'costume'</style>
#         <size>'s'</style>
#     </item>
#     <item>...</item>
# 2) Трябва да намерим начин, да прочетем всеки един ред от дейата фрейма,и даизвлечем стойностите
# като един ред е един <item>, всяка колона е таг в <item>
# 3) Прочетеното записваме като текст
# 4) ТЕкстът записваме във файл чрез стандартния интерфейс на Python

def row_to_tag (row):
    # Излвича данните за един ред от дейтафрейма и го превръща
    # в списък от стрингове, които включват и имената на таговете
    # Функцията връща стринга за един ред от данните
    xml = ['<item>']
    for field in row.index:
        xml.append('  <{0}>"{1}"</{0}>'.format(field, row[field]))
    xml.append('</item>')
    xml_str='\n'.join(xml)
    return xml_str

xml_text="<dresses>\n"+'\n'.join(df.apply(row_to_tag, axis=1))+"\n</dresses>"
# df.apply(row_to_tag, axis=1) - със метода apply прилагаме функцията row_to_tag за всеки ред (axis=1)

print(xml_text)
xml_file="Excel_to_XML.xml"
with open(xml_file, "w") as outfile:  # създаване нов празен файл с опция за запис в него
    outfile.write(xml_text)
outfile.close()