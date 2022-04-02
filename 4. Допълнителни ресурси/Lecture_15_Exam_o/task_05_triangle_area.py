import math

a = 2
b = 2
c = 3
p = (a + b + c) / 2


S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Area is: {0:.3f}".format(S))
