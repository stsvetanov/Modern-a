# collections
# namedtuple
from dataclasses import dataclass
from typing import NamedTuple

# @dataclass(order=True)
class Colour(NamedTuple):
    red: int
    green: int
    blue: int = 0 # стойност по подразбиране
red = Colour(255, 0)
orange = Colour(red=255, green=165)
print(red)
print(orange)
print(orange[0],orange[1],orange[2]) # разпечатвам стойностите на атрибутите чрез достъп до тях по индекс
print(orange.red,orange.green,orange.blue) # разпечатвам стойностите на атрибутите чрез достъп до тях по име

@dataclass(order=True)
class Colour2:
    red: int
    green: int
    blue: int
red = Colour2(255, 0,0)
orange = Colour2(red=255, green=165,blue=0)
print(list(sorted([orange, red])))

import dataclasses
print(dataclasses.astuple(red))
print(dataclasses.asdict(red))
print(dataclasses.replace(red, blue=12))

from datetime import datetime
# Примерен клас с име PyCon
@dataclass
class PyCon():
    location: str
    date: datetime
    year: int = 2018
p=PyCon("varna",datetime.now().day)
print(p)

# from dataclasses import dataclass
@dataclass
class car:
    brand:str
    model:str
    year:int=1967
new_car=car("Toyota","COrola",2018)
print(new_car)
# new_car=dataclasses.replace(new_car,model="Corola")
new_car.model="Corola"
nc=dataclasses.asdict(new_car)
print(nc)
nc['brand']="TOYOTA"
print(nc)

# # Metaklasowe
# class CarMeta(type):
#     def __new__(cls, name, bases, attrs):
#         return type.__new__(cls, name, bases, attrs)
#     @staticmethod
#     def createCarClass(carType, maxV):
#         return CarMeta('Car_' + carType, (Car,), {'_MAX_V':maxV})
# Car_Corolla = CarMeta.createCarClass('Corolla', 80.0)
# car = Car_Corolla(10.0)
# print(car)
# # print(car.velocity)
# # car.accelerate(100.0, 80.0)
# print(car.velocity)
from typing import ClassVar
@dataclass
class Colour3:
    MAX:ClassVar[int]=255
    red: int
    green: int
    blue: int = 0
red = Colour3(265, 0)
orange = Colour3(255, 165)
print(red,orange)