from bs4 import BeautifulSoup
import requests
from students import students_html  # Стринг съдържащ HTML кода на таблицата от страницата

# response = requests.get("https://fpmi.bg/moodle/grade/report/grader/index.php?id=30")
# response_content = response.content
# print(response_content)

soup = BeautifulSoup(students_html, features="lxml")

fn_list = soup.find_all("td", class_="userfield userusername cell c2")

for fn in fn_list:
    parent_element = fn.parent
    fn = int(fn.text)

    name = parent_element.find("a", class_="username").text

    print(f'{name} {fn}')



