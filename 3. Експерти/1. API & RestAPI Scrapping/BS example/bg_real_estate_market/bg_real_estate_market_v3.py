import grequests
import requests
import matplotlib.pylab as plt
from bs4 import BeautifulSoup

response = requests.get("https://www.imot.bg/pcgi/imot.cgi?act=3&slink=6agod1&f1=1")
response_content = response.content

#####  Намиране на броя страници с резултати отговарящи на търсенето
soup = BeautifulSoup(response_content, features="lxml")
pagesNumber = soup.find("span", class_="pageNumbersInfo")
pagesNumber = int(pagesNumber.text.split()[3])
print(pagesNumber)
#####

##### Генерираме списък с вскички страници
urls = [('https://www.imot.bg/pcgi/imot.cgi?act=3&slink=6agod1&f1={}'.format(n)) for n in range(1,pagesNumber+1)]
print(urls)
#####

##### Изтегляне на данните от страниците чрез генератор и библиотека grequests вместо requests
unsent_request = (grequests.get(url) for url in urls)
responseList = grequests.map(unsent_request)
#####

diction = {}
for response in responseList:

    response_content = response.content
    soup = BeautifulSoup(response_content, features="lxml")
    prices = soup.find_all("div", class_="price")

    for price in prices:
        price_parent = price.parent
        price = int(''.join(price.text.split()[:2]))
        #print(f'Цена: {price}')

        property_type = price_parent.find("a", class_="lnk1")
        property_type = str(property_type.text).split()[1]
        #print(f'Тип на имота: {property_type}')

        quarter = price_parent.find("a", class_="lnk2")
        quarter = str(quarter.text).split(",")[1]
        #print(f'Квартал: {quarter}')

        size = price_parent.findNext('tr').text.split(",")[0].split()[0]
        #print(f'Квадратура: {size}')

        if property_type in diction:
            diction[property_type][0] += price
            diction[property_type][1] += int(size)
            diction[property_type][2] += 1
        else:
            diction[property_type] = [0, 0, 0]
            diction[property_type][0] += price
            diction[property_type][1] += int(size)
            diction[property_type][2] += 1



        #print("*********************")
print(diction)
avgprice = {}

##### Средна цена имот
for prop_type in diction:
    avgprice[prop_type] = round(diction[prop_type][0] / diction[prop_type][2], 2)
print(avgprice)

##### Средна цена на квадрат за тип имот
avgpriceQuarter = {}
for prop_type in diction:
    avgpriceQuarter[prop_type] = round(diction[prop_type][0] / diction[prop_type][1], 2)
print(avgpriceQuarter)

fig1 = plt.figure(figsize=(20, 5)).suptitle('Средна цена имот', fontsize=14)
plt.bar(*zip(*avgprice.items()))
fig2 = plt.figure(figsize=(20, 5)).suptitle('Средна цена на квадрат за тип имот', fontsize=14)
plt.bar(*zip(*avgpriceQuarter.items()))
plt.show()
