import requests

# Пример 1:
# s = requests.get("http://httpbin.org/get") # зареждане на адреса
# print("Получаване на статуса на заявката:")
# print(s.status_code) #Получаване на статуса на заявката
# print("Получаване на (елемент от заглавната част (headers):")
# print(s.headers['content-type']) #Получаване на (елемент от) заглавната част (headers):
# print("Получаване на съдържанието като текст:")
# print(s.text)
# print("Получаване на съдържанието като json:")
# print(s.json()) # позволява да бъде обработено (парснато), т.е. можем да извлечем конкретна информация
# print("Получаване на content:")
# print(s.content)
# print("Проверка за redirect:")
# print(s.is_redirect)

# Пример 2:
# Пример за извличане на съдържанието на конкретна страница на Техномаркет
# т.к. страницата е динамична (генерира се от скрипт, в зависимост от нашия избор и филтри, които сме чекнали
# резултатът реално връща самия скрипт, а не това, което ни вълнува
# urlpage = 'https://www.technomarket.bg/produkti/televizori-nad-50/'
# s = requests.get(urlpage)
# print(s.status_code,s.is_redirect)
# # в заисимост от това, дали 'content-type' e text или json, ще използваме различно извличане
# if s.headers['content-type']=="text/html":
#     print(s.text)
# else:
#     print(s.json())


# # Пример 3: за метод get – API за github
# # параметри на заявката
# headers = {'Content-Type': 'application/json','User-Agent': 'Python Teacher','Accept': 'application/vnd.github.v3+json'}
# api_url = 'https://api.github.com/users/krassens/repos'
# resp = requests.get(api_url, headers=headers)
# ans = resp.json() # отговор
# print(len(ans))
# d = ans[0]
# # името на хранилището
# print(d['name'])

# Пример 4: Remix
api_url = 'https://remixshop.com/bg/womens-clothes/dresses'
# filter={'size':'S','page':4}
filter={'size':'S','last':1}
# last=1 означава "добавени днес"
# last=2 означава "добавени последните 3 дни"
respons = requests.get(api_url, params=filter)
urlpage=respons.url
print(urlpage)

# if respons.headers['content-type'][:9]=="text/html":
#     print(respons.text)
# else:
#     print(respons.json())
# <a>, href, alt, src

from selenium import webdriver
import time
import pandas as pd
#
driver = webdriver.Firefox(executable_path = '/Users/valerina/Downloads/geckodriver')
# # # get web page
driver.get(urlpage)
# # # execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# # # sleep for 30s
time.sleep(30)

# <span class="shownText"></span> 1 - 30 от 6 157 резултата


string_results_as_list=driver.find_elements_by_class_name("text")[1].text.split(" ")
if len(string_results_as_list)<=6:
    # <span class="shownText"></span> 1 - 30 от 157 резултата
    number_of_results=int(string_results_as_list[4])
else:
    # <span class="shownText"></span> 1 - 30 от 6 157 резултата, т.е. при повече от 999 резултата:
    # при използване на split(" ") числото 6157, ще бъде разделено на два стринга: "6" и "157"
    # затова ги залепяме и резултата обръщаме в integer
    number_of_results=int(string_results_as_list[4]+string_results_as_list[5])
items_per_page=int(string_results_as_list[2])
number_of_pages=number_of_results//items_per_page+1
print("Общо артикули: %d" %number_of_results)
print("Брой страници: %d" %number_of_pages)
print("Артикули на страница: %d" %items_per_page)
data = []
# # loop over results per page
def scrap_by_page(page_number):
    global data
    global api_url
    filter={'size':'S','last':1,'page':page_number}
    # last=1 означава "добавени днес"
    # last=2 означава "добавени последните 3 дни"
    respons = requests.get(api_url, params=filter)
    urlpage=respons.url
    driver = webdriver.Firefox(executable_path = '/Users/valerina/Downloads/geckodriver')
# # # get web page
    driver.get(urlpage)
# # # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# # # sleep for 30s
    time.sleep(30)

    results=driver.find_elements_by_class_name('product-box-content')
    for result in results:
        rl = result.find_elements_by_tag_name('a')[0]
        link = rl.get_attribute("href")
        info=result.text.split("\n")
        info2=rl.find_element_by_tag_name("img")
    # print("Отпечатване на ALT като атрибут:")
        alt=info2.get_attribute("alt").split(",") # alt става списъсък
    # alt[0] е марката - имаме я таг a => пропуснем
    # alt[1] е Размера - имаме от таг a => пропуснем
    # alt[2] е цвета
    # всичко, което е между alt[2] и alt[-1] е типа на материята
    # alt[-1] е цената - имаме от таг a => пропуснем
        if len(alt)>4:
            textile=','.join(alt[3:-2])
    # Алтернатива
    # print("Отпечатване на ALT като свойство:")
    # print(color.get_property("alt"))
        if len(info)<8:
            info.insert(0, 0)
            info.insert(5,'0%')
            info.insert(6,info[4])
    # print(info)
    # append dict to array
        data.append({"Марка":info[1],"Размер":info[2],"Цвят":alt[2][5:],"Материя":textile,"Цена":info[6],"link":link})
# close driver
    driver.quit()

for i in range(number_of_pages):
    scrap_by_page(i)
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('Remix.csv')


