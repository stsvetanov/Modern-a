# Диляна Хаджиматева
# докт. към КИТ, ФМИ, СУ "Св.Климент Охридски"
# н.р-л: доц. Валерия Симеонова
# дисц. Извличане на информация, проф. Иван Койчев
# 2021

# Описание на проекта:
# част 1: Извличане на информация: Търсене и сваляне на книги от сайта Library of Genesis с адрес:
# http://libgen.rs
# За да работи коректно е необходимо да се инсталира geckodriver за Mozila Firefox или аналог за Google Chrome
# и да се укаже пътя до драйвера

# Необходими модули
import requests
from selenium import webdriver
import time
import wget

# ЧАСТ 1:
# Формат на пълната заявка:
# api_url='http://libgen.rs'
# http://libgen.rs/search.php?req=cluster&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def&sort=year&sortmode=DESC&page=2
# описание на параметрите за филтриране на заявката (filter_params):
# req=cluster :търсене по ключова дума
# req=cluster* + python :търсене по две и повече ключови думи
# lg_topic=libgen :не се променя
# open=0 :не се променя
# view=simple :simple използва опростен изглед на резултата, detailed използва разширен формат на представяне,
#              ще използваме simple
# res=25 : може да приема стойности {25,50,100}
# phrase=1 :1 е без маска за думите, по които търсим, а 0 е със
# column=def :def търси всички колони
# sort=year :сортиране по година
# sortmode=DESC : сортиране в намаляващ ред

# Формат на резултата:

# attribute: color="grey" първата дума от текста е броя на резултатите, т.е. до първия интервал !!!
# Това е единствения сив текст в страницата !!!
# експат: /html/body/table[2]/tbody/tr/td[1]/font

# експат за типа на файловете: /html/body/table[3]/tbody/tr[2]/td[9]
# tr[i], i е в интервала [2;101], търсим само "pdf"

# т.к. има някакво ограничение и сървърът понякога връща грешка 50? ще се използват два линка за сваляне
# експат 1 за достъп до линка за сваляне на файла: /html/body/table[3]/tbody/tr[2]/td[10]/a
# експат на линка за сваляне след зареждане на горния линк: //*[@id="download"]/h2/a

# експат 2 за достъп до линка за сваляне на файла: /html/body/table[3]/tbody/tr[2]/td[11]/a
# експат на линка за сваляне след зареждане на горния линк: //*[@id="main"]/tbody/tr[1]/td[2]/a

# експат id: id е уникалният номер на файла в базата на ЛибГен. Той присъства както в първата колона,
#            така и като id за някои от таговете. Ще го използваме, за да извличаме името и ISBN-а на
#            поредната книга: /html/body/table[3]/tbody/tr[2]/td[1]

# Дефиниране на параметрите на заявката:
AU='http://libgen.rs'
DP='/Users/Didi/Downloads/geckodriver'
Pages=1
search_text="cluster*"
FPs={"req":search_text,"view":"simple","res":100,"phrase":0, "column":"def", "sort":"year","sortmode":"DESC","page":1}

def pdf_download(DR,i):
    # Функцията сваля конкретния .pdf file
    global DP
    expath_1='/html/body/table[3]/tbody/tr[%d]/td[10]/a' %(i)
    expath_2 = '/html/body/table[3]/tbody/tr[%d]/td[11]/a' % (i)

    try:
        dwurl=DR.find_element_by_xpath(expath_1).get_attribute('href')
        resp = requests.get(dwurl).url
        driver = webdriver.Firefox(executable_path=DP)
        driver.get(resp)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # Забавяне с 30 секунди, за да може да се свали цялата информация за страницата
        time.sleep(30)
        download_pdf_url = driver.find_element_by_xpath('//*[@id="download"]/h2/a').get_attribute('href')
    except:
        dwurl = DR.find_element_by_xpath(expath_2).get_attribute('href')
        resp=requests.get(dwurl).url
        driver = webdriver.Firefox(executable_path=DP)
        driver.get(resp)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # Забавяне с 30 секунди, за да може да се свали цялата информация за страницата
        time.sleep(30)
        download_pdf_url=driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[1]/td[2]/a').get_attribute('href')


    to_practice=['python','using%20r','application', 'sklearn','pytorch','scikit']
    expat_id = '/html/body/table[3]/tbody/tr[%d]/td[1]' % (i)
    id = int(DR.find_element_by_xpath(expat_id).text)
    fname=DR.find_element_by_id(id).text
    name_ISBN='ISBN'+fname.split(',')[-1]+'.pdf'
    number_to_pr=0
    for p in to_practice:
        if fname.lower().find(p)!=-1:
            number_to_pr+=1
    if number_to_pr==0:
        folder_path = './MyBooks/Theory/'
    else:
        folder_path = './MyBooks/Practice/'

    if len(name_ISBN)>8:
        folder_path+=name_ISBN
    else:
        folder_path+=str(id)+'.pdf'
    wget.download(download_pdf_url, out=folder_path)
    print("Downloaded file: %s" %(fname))
    driver.close()

def loading_url(api_url, driver_path,filter_params=dict()):
    # Тази функция извлича съдържанието на една страница
    # След първото използване ще извлечем общия брой на резултатите и броя на страниците,
    # които трябва да се обходят
    global Pages
    if len(filter_params)==0:
        respons = requests.get(api_url)
    else:
        respons = requests.get(api_url, params=filter_params)
    urlpage = respons.url
    print(urlpage)
    driver = webdriver.Firefox(executable_path=driver_path)
    # Извличане на страницата
    driver.get(urlpage)
    # Обхождане на страницата от горе до долу
    # Този ред не се променя и е постоянен
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # Забавяне с 30 секунди, за да може да се свали цялата информация за страницата
    time.sleep(30)
    if Pages==1:
        Pages=driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/font').text
        Pages=int(Pages.split(" ")[0])//100+1
    else: pass
    for i in range(2,101):
        # Сваля само .pdf файлове на английски език за последните 5 години
        exp_pdf='/html/body/table[3]/tbody/tr[%d]/td[9]' %(i)
        exp_lang='/html/body/table[3]/tbody/tr[%d]/td[7]' %(i)
        exp_year='/html/body/table[3]/tbody/tr[%d]/td[5]' %(i)
        condition_pdf=driver.find_element_by_xpath(exp_pdf).text=="pdf"
        condition_lang=driver.find_element_by_xpath(exp_lang).text=="English"
        condition_year=True
        try:
            int(driver.find_element_by_xpath(exp_year).text)
        except:
            condition_year="just skip it"
        finally:
            if condition_year!="just skip it":
                condition_year=int(driver.find_element_by_xpath(exp_year).text)>=2016
        # "just skip it" е за записи, вкоито има изброени повече от една година
        # condition_year == False е случая когато годината е по-ранна от 2016,
        # и няма смисъл да се обхождат по-нататък страниците, затова имаме break
        # Реално сваляме само файловете, които са pdf-и на английски в периода [2016;...)
        if condition_year=="just skip it":
            pass
        elif condition_year==False:
            break
        elif condition_year and condition_pdf and condition_lang:
            pdf_download(driver, i)
        else: pass

    driver.close()

for j in range(1,Pages+1):
    loading_url(AU, DP, FPs)
    if j == 1:
        print(Pages)