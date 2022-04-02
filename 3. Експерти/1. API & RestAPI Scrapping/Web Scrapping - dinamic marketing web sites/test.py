# Скрапване на динамични сайтове
# Източник: https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f
# Трябва да се инсталира драйвера geckodriver за Mozilla Firefox и да се добави в пътя:
# https://github.com/mozilla/geckodriver/releases

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
import bs4 as bs

# Зареждане на първоначалната страница
urlpage = 'https://www.technomarket.bg/produkti/televizori-nad-50/'
print(urlpage)
path='/Users/valerina/Downloads/geckodriver'
driver = webdriver.Firefox(executable_path = path)
driver.get(urlpage)
driver.find_element_by_id("mat-dialog-0").find_element_by_tag_name("button").click()
ff=driver.page_source
bs.BeautifulSoup(ff).

# driver.find_element_by_id("eimodal").find_element_by_id("cp_popup_content").find_element_by_id("cp_oui_footer").find_element_by_tag_name("p").click()

# driver.set_window_size(0,0)
# driver.set_window_position(0,0)
# driver.switch_to.default_content()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
time.sleep(30)
# driver.switch_to.default_content()

Execute=True
while Execute:
    # Извличане на текущата страница с резултати:
    results = driver.find_elements_by_tag_name('tm-product-view')  # 34 резултата=24+10
    results = results[:24]  # защото на страницата се визуализират по 24 резултата, останалите 10 са други
    tex = 'Number of results'
    print(tex, len(results))
    # create empty array to store data
    data = []
    # loop over results from current page
    for result in results:
        tex = result.text.split("\n")
        if len(tex) < 5:
            tex.insert(0, 0)
            tex.append(tex[3])
        tex.pop(2)

        rl = result.find_elements_by_tag_name('a')[0]
        link = rl.get_attribute("href")
        # append dict to array
        data.append({"TV": tex[1], "Стара цена": tex[2], "Нова цена": tex[3], "Отстъпка": tex[0], "Линк": link})
    # Проверка дали текущата страница е последната:
    soup=driver.page_source
    soup=bs.BeautifulSoup(soup,"lxml")
    test=soup.find("li",{'class':"small-screen"})
    test=test.text.replace(" ", "").split("/")
    if test[0]==test[1]:
        Execute=False
    else: #process next page
        liall=driver.find_elements_by_tag_name("li")
        li=[l.text for l in liall]
        lindex=li.index("Следваща страница")+1
        lindex=lindex+li[lindex:].index("Следваща страница")
        liall[lindex].click()

# close driver
driver.quit() # Затваря прозореца на Firefox

# Export Data
df = pd.DataFrame(data)
print(df)
df.to_csv('Promo_TechnoMarket.csv')

print("*********END*********")