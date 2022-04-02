import random

def slice(s, var_from, to):
    # Функцията връща отрязък от стринг по зададени стринг,
    # началона и крайна позиция. Реално връща tex[from,to-1]
    n = len(s)
    sliced = ""
    for i in range(var_from, to):
        sliced = sliced + s[i]
    return sliced

# Main
# random.seed()   #Prepare random number generator

# s = input()
s='Баба Марта ми донесе много мартенички'
newS = ""

# n- дължината на стринга, i- итератор в цикъла
# n = len(s)
# while len(newS) < len(s):
#     rnd = random.randint(0,len(s)-1)
#     print(rnd)
#     symbol = s[rnd]
#     newS = newS + symbol
#     s = slice(s, 0, rnd) + slice(s, rnd + 1, len(s))
# print(newS)

# алтернативен (стандартен) запис в Python:

# while len(newS) < len(s):
#     rnd = random.randint(0,len(s)-1)
#     symbol = s[rnd]
#     newS = newS + symbol
#     s=s[:rnd]+s[rnd+1:]
# print(newS)
newS=[]
sl=list(s)  # превръща стринг във списък
print(s)
n=len(s)
while len(newS) < n:
    rnd = random.randint(0,len(sl)-1)
    newS.append(sl.pop(rnd))
newS=''.join(newS) # превръща списък във стринг
print(newS)
