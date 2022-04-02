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

# specify the url
urlpage = 'https://www.technomarket.bg/produkti/televizori-nad-50/'
print(urlpage)
# Този път е специфичен, и зависи от настройките, които сте направили за драйвера
path='/Users/valerina/Downloads/geckodriver'
driver = webdriver.Firefox(executable_path = path)
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# Определяне на броя на артикулите, броя на страниците за обхождане и броя на артикулите на последна страница
# total_items




# Извличане на първата страница с резултати:
results=driver.find_elements_by_tag_name('tm-product-view') # 34 резултата=24+10
results=results[:24] # защото на страницата се визуализират по 24 резултата, останалите 10 са други
tex='Number of results'
print(tex, len(results))
# create empty array to store data
data = []
# loop over results
for result in results:
    tex=result.text.split("\n")
    if len(tex)<5:
        tex.insert(0,0)
        tex.append(tex[3])
    tex.pop(2)

    rl = result.find_elements_by_tag_name('a')[0]
    link = rl.get_attribute("href")
    # append dict to array
    data.append({"TV" :tex[1],"Стара цена":tex[2],"Нова цена":tex[3],"Отстъпка":tex[0],"Линк" : link})

# # # close driver
driver.quit() # Затваря прозореца на Firefox

# # save to pandas dataframe
df = pd.DataFrame(data)
print(df)
# #
# # # # write to csv
df.to_csv('Promo_TechnoMarket.csv')


#test
# from selenium.webdriver.common.keys import Keys
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# element = driver.find_element_by_xpath("//select[@name='Salutation']")
# all_options = element.find_elements_by_tag_name("option")
# for option in all_options:
#     if option.get_attribute("value") == "Ms":
#         option.click()
# driver.find_element_by_name("_ngcontent-serverapp-c281").text.click()
#
# someElement = driver.find_element_by_name("searchbox")
# someElement.submit()

# driver.find_elements_by_name("_ngcontent-serverapp-c281").click()
# <span class="mat-option-text">120 продукта </span> да се наклика от падащото меню
# <li _ngcontent-serverapp-c281="" class="pagination-next">
# <a _ngcontent-serverapp-c281="" tabindex="0" aria-label="Следваща страница" class="ng-star-inserted"> Следваща страница </a><!----><!----></li>
# <li _ngcontent-serverapp-c281="" class="pagination-next disabled">
# <!----><span _ngcontent-serverapp-c281="" class="ng-star-inserted"> Следваща страница </span><!----></li>
