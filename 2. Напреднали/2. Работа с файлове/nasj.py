file_name="/Users/valerina/PycharmProjects/1386/Работа с JSON-20210517/not_a_simple_json.json"

import json

example2=open(file_name,'r') # Отваряне на .json файла за четене
jdata= json.load(example2)
print(jdata.keys())
D=dict()
for i in jdata.keys():
    D[i]=type(jdata[i])
for k,v in D.items():
    print('%s:%s' %(k,v))


