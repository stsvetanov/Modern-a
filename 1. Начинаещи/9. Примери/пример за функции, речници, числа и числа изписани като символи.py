# Да се създаде списък от числа написани и с цифри (figures), и с букви (letters) и
# повтарящи се числа, написани и по двата начина.
# Ключовете в речника са:
# f- има стойност списъка на цифрите
# l- има стойност списъка на буквите
# fnl- има стойност повтарящите се числа (т.е. които са написани и с цифри, и с букви)
# Да се отговори на въпросите:
# - Колко са числата написани само с цифри?
# - Колко са числата написани само с букви?
# - Колко са числата, които са написани и по двата начина?
# - Колко са числата написани само по единия начин?


# Решение: 1) т.к. в задачата не се казва дали числата представени с букви са от някоя бройна система,
# то ще приемем, че на всяка цифра й съответства малка буква от латинската азбука, като съответствията няма
# да ги правим последователни, а на случаен принцип. 2) не е посочено колко големи могат да бъдат числата,
# затова ще сложим някакво ограничение, например до 1000.

import random as rd
letters=rd.choices('abcdefghijklmnopqrstuvwxyz',k=10)
figures=[str(i) for i in range(10)]
Cifre_fl=dict(zip(figures,letters))
print(Cifre_fl)
Cifre_lf=dict(zip(letters,figures))
print(Cifre_lf)

def l2f(alpha):
    fig=str(int(''.join([Cifre_lf[s] for s in alpha])))
    return fig

def f2l(numeri):
    fig=''.join([Cifre_fl[s] for s in str(numeri)])
    return fig

def mix(numeri):
    # 50 % от цифрите се подменят с техните буквени означения
    numeri=str(numeri)
    indexes_2alpha=rd.choices(list(range(len(numeri))),k=len(numeri)//2)
    fig = ''
    for i,s in enumerate(numeri):
        if i in indexes_2alpha:
            fig+=Cifre_fl[s]
        else:
            fig+=s
    return fig
def partial_convertion(what,convert_to='alpha'):
    # what може да бъде както изцяло от цифри, така и изцяло от букви или смесено
    # convert_to може да приема стойности 'alpha' и 'numeri'
    if convert_to=='alpha':
        new_alpha=''
        what=str(what)
        for w in what:
            if w in Cifre_fl: new_alpha+=Cifre_fl[w]
            else:new_alpha += w
        return new_alpha
    elif convert_to=='numeri':
        new_numero = ''
        for w in what:
            if w in Cifre_lf: new_numero += Cifre_lf[w]
            else:new_numero += w
        return new_numero

def auto_generator():
    numbers=list(range(1000))
    l1=rd.choices(numbers,k=rd.randint(1,100)) # fixed
    l1str=[str(l) for l in l1]
    l2=list(map(f2l,rd.choices(numbers,k=rd.randint(1,100)))) # to alpha
    l3=list(map(mix,rd.choices(numbers,k=rd.randint(1,100)))) # mixed
    L=list(set(l1str+l2+l3))
    return L

# - Колко са числата написани само с цифри?
# - Колко са числата написани само с букви?
# - Колко са числата, които са написани и по двата начина?
# - Колко са числата написани само по единия начин?

# ------MAIN-----
L=auto_generator()
print(L)

def how_many(spisyk):
    only_numbers=0 #isdigit(),isnumeric()
    only_letters=0 #isalpha()
    both=0 # same number different way

    ON=[s.isdigit() for s in spisyk]
    OL=[s.isalpha() for s in spisyk]
    print('Колко са числата написани само с цифри? - %d' %(sum(ON)))
    print('Колко са числата написани само с букви? - %d' % (sum(OL)))

    just_cavali=[s for s in spisyk if s.isdigit()] # това са само изписаните с цифри

    for i in range(len(spisyk)):
        if spisyk[i].isdigit():
            pass
        elif spisyk[i].isalpha():
            spisyk[i]=l2f(spisyk[i])
        else:
            spisyk[i] =partial_convertion(spisyk[i],'numeri')
    # след този for разполагаме само с числа, изписани с цифри,
    # като ако числото се среща:
    # 1 път: следва, че е изписано само по един начин
    # 2 пъти: по два начина
    # 3 пъти: по три начина

    D=dict()
    for s in spisyk:
        if s not in D:
            D[s]=spisyk.count(s)
    print(D)
    R= {1:[],2:[],3:[]}
    for k,v in D.items():
        if v==1:R[1].append(k)
        elif v==2:R[2].append(k)
        elif v==3:R[3].append(k)
    for k,v in R.items():
        print(k,v)
    print("Числата изписани по 1 начин са: %d" %(len(R[1])))
    print("Числата изписани по 2 начина са: %d" % (len(R[2])))
    print("Числата изписани по 3 начина са: %d" % (len(R[3])))

how_many(L)