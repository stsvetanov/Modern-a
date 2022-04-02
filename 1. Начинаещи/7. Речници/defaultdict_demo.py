from collections import defaultdict

# somedict = {}
# print(somedict[3]) # KeyError

somedict = defaultdict(int)
print(somedict[3]) # print int(), thus 0

somedict1 = defaultdict(set)
print(somedict1[3]) # print int(), thus 0

somedict2 = defaultdict(list)
print(somedict2[3]) # print int(), thus 0