def rows(text):
    """Определя броя на редовете, които могат да бъдат отпечатани
    Sum съдържа броя на елементите с натрупване"""
    n = len(text)
    a = 1
    d = 2
    sum = 0
    i = 0
    while sum < n:
        i = i + 1
        sum = sum + a
        a = a + d
    
    # Sum отразява броя на елементите в равнобедрен триъгълник. Ако броят на елементите в sum е колкото на общия брой, то тогава текстът може да се отпечата под формата на равнобедрен тиръгълник.
    if sum == n:
        rows = i
    else:
        rows = 0
    
    return rows

def slice(s, var_from, elements):
    # Функцията връща отрязък от стринг по зададени стринг, начална позиция и брой елементи, които да се върнат започвайки от началната позиция.
    sliced = ""
    for i in range(0, elements - 1 + 1, 1):
        sliced = sliced + s[i + var_from]
    
    return sliced

def space(tex, row):
    spaces = ""
    nr = rows(tex)
    
    # k е отместването от началото на реда, за красивото отпечатване
    k = nr - row
    for i in range(0, k - 2 + 1, 1):
        spaces = spaces + "*"
    
    return spaces

# Main
text = input()
var_from = 0
nr = rows(text)
if nr != 0:
    for i in range(0, nr - 1 + 1, 1):
        elements = i * 2 + 1
        sl = space(text, i) + slice(text, var_from, elements) + space(text, i)
        print(sl)
        var_from = var_from + elements
else:
    print("Не е възможно текстът да бъде отпечатан като:\tравнобедрен триъгълник")
#     "C:\\User\\Downloads\\my.py" , специално при Windows
#   "3-ти март мина, не видях зарята ':('"
#   "3-ти март мина, не видях зарята \":(\""
