import requests
from selenium import webdriver
import time
#
# # main_url='http://www.regalia6.com/books/eU4ebnik-matematika-12klas_PP_Veroyatnosti_21/files/mobile/'
# # main_url='http://www.regalia6.com/books/eU4ebnik-matematika-12klas_PP_Prakt-mat_21/files/mobile/'
# # main_url='http://sales.anubis-bulvest.com/epub/12_klas/b12MatPP3Mod/'
# #main_url='https://bg.e-prosveta.bg/fulldemo/CsnDEtgjdY-943/900'
# #https://static.e-prosveta.bg/900/3/bg/bg3.jpg
# main_url='https://static.e-prosveta.bg/900/3/bg/bg'


fnames=[str(i)+'.jpg' for i  in range(38,219)]
main_url='https://bg.e-prosveta.bg/fulldemo/CsnDEtgjdY-943/900?page='
urls=[main_url+str(i) for i  in range(38,219)]
# els = []
for i in range(218):
    r = requests.get(urls[i]).url
    driver = webdriver.Firefox(executable_path='/Users/valerina/Downloads/geckodriver')
    driver.get(r)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(10)

    el = driver.find_element_by_tag_name('app-ebook-page')
    el = el.find_element_by_tag_name('img')

    url=el.get_attribute('src')

    r = requests.get(url, allow_redirects=True)
    open(fnames[i], 'wb').write(r.content)

    driver.close()







