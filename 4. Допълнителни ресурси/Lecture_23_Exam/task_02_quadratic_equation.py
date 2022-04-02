'''
ax**2 + bx +c
D = b**2 - 4ac

if D > 0:
    x1 = (-b + sqr(D))/2a
'''
from math import sqrt

a = 1
b = 5
c = 4

D = b**2 - 4 * a *c

if D == 0:
    x1 = x2 = -b/2 * a
elif D > 0:
    x1 = (-b + sqrt(D))/2 * a
    x2 = (-b - sqrt(D))/2 * a
    print("Root1 = {}, Root2 = {}".format(x1, x2))
else:
    print("No real roots")
