# Boolean operators
# default values

# Примери за Falsy стойности в зависимост от типа:
# int - 0
# float: 0.0 (но трябва да се внимава с това, заради грешки в точността на представяне на float числата, особено ако float стойността е резултат от изчисления)
# str - "" (празен стринг)
# bytes - b"" (празен bytes обект)
# list, tuple, dict, set - празни
# None
# False

# Всички останали стойности за съотвения тип се третират като Truthy, например:
# int - 1, -1, -5237922296986728930672677403958
# float: 0.000000000001, 320573.3245
# str - " " (стринг, съдържащ интервал), "any other string value"
# bytes - b" " (bytes, съдържащ интервал),b"\x32bytes\x62"
# непразни list, tuple, dict, set - [" "], [0], [1,2,3,4, "a"], {"key": "value"}, {2, 4, 6, 8}, ("", "")
# True
# Обект

# value = value or DEFAULT_VALUE

# minimal/short-circuit evaluation
# "default" стойност на променлива, ако тя към момента е празна


def display_list(l: list = None):
    # this.options = options || {}
    # if l is not None:
    for element in l or []:
        print(element)


display_list([1, 2, 3, 4])
display_list()
