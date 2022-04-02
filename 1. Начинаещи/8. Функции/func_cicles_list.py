# f(L): проверява дали всеки два съседни  елемента имат еднакъв сбор

L=[4,2,3,0,4,-1,4]

def f(L):
    try: sum(L)
    except: print("Списъкът трябва да съдържа само числа !")
    else:
        sbor=L[0]+L[1]
        print(sbor)
        flag=True
        for i in range(2,len(L)-1,2):
            if sum(L[i:i+2])!=sbor:
                flag=False
                print(L[i:i+2])
                break
        if flag: s="Всеки два съседни елемента имат равен сбор"
        else:
            s = "Не Всеки два съседни елемента имат равен сбор"
        return s

print(f(L))