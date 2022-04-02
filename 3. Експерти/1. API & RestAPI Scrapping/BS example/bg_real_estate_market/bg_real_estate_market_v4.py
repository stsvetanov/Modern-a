from collections import defaultdict
import requests
import matplotlib.pylab as plt
from bs4 import BeautifulSoup

property_type_total_price = defaultdict(int)
propety_type_count = defaultdict(int)
property_type_max_price = defaultdict(int)

quarter_total_price = defaultdict(int)
quarter_count = defaultdict(int)

start_url = "https://www.imot.bg/pcgi/imot.cgi?act=3&slink=6ssrk7&f1=1"
# start_url = input("Enter url")

print(start_url)
response = requests.get(start_url)
response_content = response.content

#####  Намиране на броя страници с резултати отговарящи на търсенето
soup = BeautifulSoup(response_content, features="lxml")   #парсва текста , свързано със структутата на дървото
#тага span - взимаме странците от 1 до 25
pagesNumber = soup.find("span", class_="pageNumbersInfo")
pagesNumber = int(pagesNumber.text.split()[3])
#странците от 1 до 25  -> 25
print(pagesNumber)
#####

##### Генерираме списък с вскички страници
new_url = start_url[:-1]
print(new_url)
# списък с адреси
urls = [f'{new_url}{n}' for n in range(1, pagesNumber+1)]
print(urls)

for url in urls:
    response = requests.get(url)

    response_content = response.content   #целия текст на странцита
    soup = BeautifulSoup(response_content, features="lxml")
    prices_div = soup.find_all("div", class_="price")

    for price_div in prices_div:
        price_parent = price_div.parent
        try:
            price = int(''.join(price_div.text.split()[:2]))      #взимаме без еврото и го правим на стринг
        except:
            print("Price is not integer")     #когато е цена по договаряне

        property_type = price_parent.find("a", class_="lnk1")
        property_type = str(property_type.text).split()[1]     #3-стаен
        #print(f'Тип на имота: {property_type}')

        quarter = price_parent.find("a", class_="lnk2")
        quarter = str(quarter.text).split(",")[1]
        #print(f'Квартал: {quarter}')

        size = price_parent.findNext('tr').text.split(",")[0].split()[0]
        #print(f'Квадратура: {size}')

        property_type_total_price[property_type] += price
        propety_type_count[property_type] += 1

        if property_type_max_price[property_type] < price:
            property_type_max_price[property_type] = price

        quarter_total_price[quarter] += price
        quarter_count[quarter] += 1

property_avg_price = {}

for key, value in property_type_total_price.items():
    property_avg_price[key] = value/propety_type_count.get(key)

quarter_avg_price = {}
for key, value in quarter_total_price.items():
    quarter_avg_price[key] = value/quarter_count.get(key)

print(property_avg_price)
print(quarter_avg_price)
print(property_type_max_price)

#Средна цена за всеки тип имот
fig1 = plt.figure(figsize=(10,5)).suptitle('Средна цена за всеки тип имот',fontsize = 10)
plt.bar(*zip(*property_avg_price.items()))

#Средна цена за квартал
fig1 = plt.figure(figsize=(10,5)).suptitle('Средна цена за квартал',fontsize = 10)
plt.bar(*zip(*quarter_avg_price.items()))    #zip - прави ги наведнъж

#Max price
fig1 = plt.figure(figsize=(10,5)).suptitle('Максимална цена за тип имот',fontsize = 10)
plt.bar(*zip(*property_type_max_price.items()))    #zip - прави ги наведнъж
plt.show()