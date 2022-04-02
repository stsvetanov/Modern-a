# y=a*x^2+b*x+c

from random import randint
l=[randint(0,100) for i in range(5)]
def fotx(x,a=1,b=0,c=0):
    return a*x**2+b*x+c

for i in l:
    # print("x=%d, a=1, b=0, c=0, y=%d" %(i,fotx(i)))
    y=fotx(i)
    print(i,y)