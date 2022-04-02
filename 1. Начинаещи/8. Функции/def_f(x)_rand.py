# Да се направи списък от 8 произволни цели числа X в интервала [0,100].
# За всяко число да се изчисли формулата f(x)=a*x^2+b*x+c
# Резултатите да се оформят в речник FX от вида: {x:f(x)}

def variant_1():
    from random import randint
    X=[randint(0,100) for i in range(8)]
    a,b,c=randint(0,10),randint(0,10),randint(0,10)
    Y=[a*x**2+b*x+c for x in X]

    FX=dict(zip(X,Y))
    print(a,b,c)
    for i in FX.items():
        # print(i) # това изпечатва по една двойка "ключ:стойност" на ред
        print("При x=%d f(x)=%d" %(i[0],i[1]))

    # for k,v in FX.items():
    #     # алтернативно на горното
    #     print("При x=%d f(x)=%d" %(k,v))

def variant_2():
    from random import randint
    a, b, c = randint(0, 10), randint(0, 10), randint(0, 10)
    FX={}
    for i in range(8):
        x=randint(0,100)
        if x not in FX:
            FX[x]=a*x**2+b*x+c
    for i in FX.items():
        print(i)

variant_2()
