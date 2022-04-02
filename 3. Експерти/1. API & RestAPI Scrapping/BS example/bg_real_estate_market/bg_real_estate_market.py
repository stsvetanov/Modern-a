from bs4 import BeautifulSoup
import requests

# response = requests.get("https://www.imot.bg/pcgi/imot.cgi?act=3&slink=50xu0m&f1=1")
response = requests.get("https://www.imot.bg/pcgi/imot.cgi?act=3&slink=57suqn&f1=1")
response_content = response.content

soup = BeautifulSoup(response_content, features="lxml")

prices = soup.find_all("div", class_="price")

for price in prices:
    price_parent = price.parent
    price = int(''.join(price.text.split()[:2]))
    print(f'Цена: {price}')

    property_type = price_parent.find("a", class_="lnk1")
    property_type = str(property_type.text).split()[1]
    print(f'Тип на имота: {property_type}')

    quarter = price_parent.find("a", class_="lnk2")
    quarter = str(quarter.text).split(",")[1]
    print(f'Квартал: {quarter}')

    size = price_parent.findNext('tr').text.split(",")[0].split()[0]
    print(f'Квадратура: {size}')

    print("*********************")



