# data = (100, 200)
# print(type(data))
# x, y = data
# print(x)
# print(y)



data = (100, 200, 23, 234, 435)
# for index, el in enumerate(data):
#     print(index)
#     print(el)

# x, y, *rest = data
x, y, *_ = data
print(x)
print(y)
print(*_)

