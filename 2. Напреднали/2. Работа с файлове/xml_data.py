# <?xml version="1.0" encoding="windows-1251" standalone="yes"?>
# ред 1 показва по какъв начин са кодирани символите във файла и версията на xml-a
# <ROWDATA xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
# ред 3 се явява корен на дървото в xml файла, като е указан стандарта за схема на xml файла
# Стандартът за схема се използа за валидирането на файла при неговото съставяне
# Атрибутът винаги стои след името на отварящия таг, но в самия отварящ таг
# Пример за атрибут: <movie favorite="True">
# Тук атрибут ще наричаме favorite и той има стойност "True"
# Таг наричаме всичко, което се намира между знаците < и >
# Пример за таг: <ROW>
# Затварящ таг винги има име на някой отварящ таг, като започва с: </
# Стойността между един отварящ и един затварящ таг с едно и също име се извлича с .text
# Горното е валидно при условие, че не следва някаква структура от тагове !!!
#         <ROW>
# "ROW" представлява таг за ред от фактурата и има допълнителна структура от тагове
# За всеки "ROW" структурата от тагове е една и съща !!!
#             <MSISDN>359896824044</MSISDN>
#             <CALL_DATE>2019-03-31</CALL_DATE>
#             <CALL_START_TIME>22:22:02</CALL_START_TIME>
#             <B_NUMBER>telenorbg</B_NUMBER>
#             <CALL_NAME>Моб. интернет</CALL_NAME>
#             <PRODUCT_TYPE> </PRODUCT_TYPE>
#             <CALL_DURATION>00:00:00</CALL_DURATION>
#             <GPRS_USED_KB>2923.00</GPRS_USED_KB>
#             <CALL_CHARGE>0.00</CALL_CHARGE>
#             <BM_INDICATOR>*</BM_INDICATOR>
#         </ROW>


pth="/Users/valerina/PycharmProjects/1386/Работа с JSON-20210517/"
fn="details1_2019_5.xml"

import xml.etree.ElementTree as ET
tree = ET.parse(pth+fn)
root = tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
print(root.text)

# Показва всички тагове в дървото
all_elements_in_tree=set([elem.tag for elem in root.iter()])
print(all_elements_in_tree)

# Извличане на първите 5 записа:
First_5=[]
for child in root:
    # child е ROW, нямаме атрибути, но имаме под тагаове
    l = []
    for subch in child:
        # subch mоже да бъде: MSISDN, CALL_DATE, CALL_START_TIME,B_NUMBER,CALL_CHARGE...
        l.append(subch.text)
    First_5.append(l)
    if len(First_5) == 5: break

for f5 in First_5:
    print(f5)

# Красиво извеждане на XML файл:
# print(ET.tostring(root, encoding='utf8').decode('utf8'))
print(ET.tostring(child, encoding='utf8').decode('utf8'))
ET.
