def decor(uni):
    def wrapper(*args):
        print(" Начало на декорацията: ")
        print("дисциплина: " + uni[0] + "\n")
        print("семестър: " + str(uni[1]) + "\n")
        print("факултетен номер: " + str(uni[2]) + "\n")
        print("дата: " + str(uni[3]) + "\n")
        print("оценка: " + uni[4] + "\n")
        print(" Край на декорацията... ")
    return wrapper

from typing import NamedTuple
from datetime import datetime
@decor
class uni(NamedTuple):
    discipline:str
    semester:int
    fn:int
    date: datetime
    grade: str

u=uni("IST",2,12000,datetime.today().date(),"Отличен")


# Да се дефинира клас описващ изпит, като има:
# име на дисциплината (str), семестър (int), фн(int), дата(datetime), оценка (int от 2 до 6)
# да се декорира отпечатването на обект от класа като се използва функция декоратор
# същият резултат да се постигне чрез стандартните методи за работа с класове



