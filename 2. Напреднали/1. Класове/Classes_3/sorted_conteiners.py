from typing import *


class MyClass:
    c: float
    def __init__(self):
        self.c=33.17
        self.d:str="I'm a string"
    def __repr__(self):
        s='mc.c=%f' %(self.c)
        s+='\nmc.d=%s' %(self.d)
        return s
mc=MyClass()
# print(mc)

# tlist: List[Union[int,int]]=[15,20]
# tlist: List[Union[int,int]]=[]
# tlist.append(int(input('първи ел.: ')))
# tlist.append(int(input('втори ел.: ')))
# print(tlist)

# school_coords: Dict[str,Tuple[int,int]]
# school_coords={'test':(1,'2')}
# print(school_coords)
# # Защо не връща грешка ?!

# vat_rate: int=20
# reduced_vat=True
# if reduced_vat:
#     vat_rate=5.5
#     # # Защо не връща грешка ?!
# print(vat_rate)

# Vector = List[int]
#
# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]
#
# # typechecks; a list of floats qualifies as a Vector.
#
# new_vector = scale(2.0, [1, -4, 5.4])
# print(new_vector)

import sortedcontainers as sc
# sd=sc.SortedDict()
# sd['e'] = 2
# sd['b'] = 5
# print(sd)

# # За даден стандартен речник, да се изведе най-големия ключ
# d={1:'a',5:'b',3:'c'}
# sd=sc.SortedDict()
# sd.update(d)
# print(sd.popitem(-1)[0])
#
# # Проверка за наличие на ключ в сортиран речник:
# print('c' in sd)
# # резултатът е False когато липсва такъв ключ
# print(sd.get('z') is None)
# # резултатът е True когато липсва такъв ключ
#
# set_orig={1,3,5,2}
# # Защо връща сортирано множество ?!
#
# # Сортиране:
# # първо да намеря най-малкия елемент
# el=min(set_orig)
# set_orig.remove(el)
# set_orig.add(el)

Date = NamedTuple('Date', ('year', 'month', 'day')) #ValueError: too many values to unpack (expected 2)
sputnik_1 = Date(year=1957, month=10, day=4)
year, month, day = sputnik_1
print(year)
