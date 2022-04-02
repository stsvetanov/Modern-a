from math import sqrt
# Дава възможност да се импортне функция от даден модул, която да се използва директно:
# from <module> import <function>

# import math
# По този начин все едно, че зареждам целия модул, и => няма директен достъп до функциите
# и се налага да укажа първо модула и след това функцията:
# math.sqrt(25)

bi=[1,0,0,1,0]
dec=0
p=[x for x in range(len(bi))]
p.sort(reverse=True)
for i in range(len(bi)):
    if bi[i]==1:
        dec+=2**p[i]
print(dec)
