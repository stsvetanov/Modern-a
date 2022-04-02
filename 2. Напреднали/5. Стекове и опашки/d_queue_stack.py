# Зад.1 Да се състави програма за създаване на опашка от цели положителни числа,
# след което я разделя на два стека:
# съдържащи съответно четни и нечетни елементи на опашката.
# => от опашката ще вадим елемент и ще го слагаме във стека

# чрез списъци:
def aslist():
    import random as rd
    опашка=[]
    n=int(input('брой на елементите в опашката: '))
    for i in range(n):
        опашка.append(rd.randint(1,100))
    стек_нечетни=[]
    стек_четни=[]

    while len(опашка)>0:
        print('текуща опашка: ')
        print(опашка)
        print(опашка[0])
        print('стековете преди: ')
        print(стек_нечетни)
        print(стек_четни)
        if опашка[0]%2==0:
            стек_четни.append(опашка.pop(0))
        else:
            стек_нечетни.append(опашка.pop(0))
        print('стековете след: ')
        print(стек_нечетни)
        print(стек_четни)
    print('крайно състояние на опашката:')
    print(опашка)

# чрез collections (клас deque)
def ascollect():
    from collections import deque
    опашка=deque()
    import random as rd
    n=int(input('брой на елементите в опашката: '))
    for i in range(n):
        опашка.append(rd.randint(1,100))
    стек_нечетни=deque()
    стек_четни=deque()
    while len(опашка) > 0:
        print('текуща опашка: ')
        print(опашка)
        print(опашка[0])
        print('стековете преди: ')
        print(стек_нечетни)
        print(стек_четни)
        if опашка[0] % 2 == 0:
            стек_четни.append(опашка.popleft())
        else:
            стек_нечетни.append(опашка.popleft())
        print('стековете след: ')
        print(стек_нечетни)
        print(стек_четни)
    print('крайно състояние на опашката:')
    print(опашка)

# чрез queue (клас LifoQueue)
def asqueue():
    from queue import LifoQueue
    опашка=LifoQueue()
    import random as rd
    n=int(input('брой на елементите в опашката: '))
    for i in range(n):
        опашка.put(rd.randint(1,100))
    print(опашка.queue)
    стек_нечетни=LifoQueue()
    стек_четни=LifoQueue()
    while опашка.qsize()>0:
        fisrt_element = опашка.get()
        print('текуща опашка: ')
        print(опашка.queue)
        print(fisrt_element)
        print('стековете преди: ')
        print(стек_нечетни.queue)
        print(стек_четни.queue)

        if fisrt_element % 2 == 0:
            стек_четни.put(fisrt_element)
        else:
            стек_нечетни.put(fisrt_element)
        print('стековете след: ')
        print(стек_нечетни.queue)
        print(стек_четни.queue)
    print('крайно състояние на опашката:')
    print(опашка.queue)

#ascollect()
#asqueue()

# Да се напише функция, която проверява дали елементите на стек от числа са различни.
# b) да се изведе статистика за всяко число, колко пъти се повтаря във стека
def зад2():
    import random as rd
    import pandas as pd
    стек=[]
    s2=[]
    n=15
    for i in range(n):
        k=rd.randint(1,100)
        стек.append(k)
        s2.append(k)
        # prawim dwa identi§ni steka, no s razli§ni id-ta

    #Fastest way:
    #df=pd.DataFrame(стек)
    #print('статистика: ')
    #print(df.value_counts())
    a=set()
    while len(стек)>0:
        a.add(стек.pop())
    if len(a)==n:
        print('Стекът е с различни числа:')
    else:
        print('В стека има еднакви числа')
    a=list(a)
    dic=dict()
    for i in range(len(a)):
        dic[a[i]]=0
    while len(s2)>0:
        el=s2.pop()
        if el in dic:
            dic[el]+=1
    print(dic)
зад2()
