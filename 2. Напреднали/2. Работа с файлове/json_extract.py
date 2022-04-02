import json
with open('exmple.2.json') as f:
  json_data = f.read()
f.closed
python_obj = json.loads(json_data)
keylist = list(python_obj.keys())
print(list(keylist))
for x in python_obj[keylist[0]]:
        print (x["room-number"])
