# Примитивно сортиране (пълно изчерпване) или още
# Сортиране с пермутации / Bogo Sort
# Вариант 1:
import random
def is_sorted_1(data):
    """Determine whether the data is sorted."""
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bogosort(data):
    """Shuffle data until sorted."""
    while not is_sorted_1(data):
        random.shuffle(data)
    return data

l=[1,2,5,3,4]
#print(bogosort(l))

# Вариант 2:
from itertools import permutations
def is_sorted_2(seq):
    seq=list(seq)
    n = len(seq)
    if n<2: return True
    else:
        for i in range(n-1):
            if seq[i]>seq[i+1]:
                return False
                break
    return True
def permutation_sort(seq):
    k=next(list(perm) for perm in list(permutations(seq)) if is_sorted_2(perm))
    return k
# print(l)
# print(permutation_sort(l))

# Сортиране със сливане / Merge Sort
# Вариант 1 (снимката с черен фон):
def merge_sort(arr,low,high):
    if high-low<=1:
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid,high)
    i,j=low,mid
    tmp=[]
    while i <mid and j<high:
        if arr[i]<arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<mid:
        tmp.append(arr[i])
        i+=1
    while j<high:
        tmp.append(arr[j])
        j+=1
    arr[low:high]=tmp
    print(tmp)
# merge_sort(l,0,len(l))
# print(l)

# Вариант 2:
def merge_sort_2(seq):
    if len(seq)>1:
        mid = len(seq)//2
        left = seq[:mid]
        right = seq[mid:]
        merge_sort_2(left)
        merge_sort_2(right)
        i, j, k = 0, 0, 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                seq[k] = left[i]
                i += 1
            else:
                seq[k] = right[j]
                j += 1
            k += 1
        while i<len(left):
            seq[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            seq[k] = right[j]
            j += 1
            k += 1
# merge_sort_2(l)
# print(l)

# Шейкър сортиране / Shuttle sort, или "Двупосочно мехурче"
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
        swapped = False
        for i in range (start, end):
            if (a[i] > a[i + 1]) :
                a[i], a[i + 1]= a[i + 1], a[i]
                swapped = True
                # най-малкия елемент бяга на ляво
        if (swapped == False): break
        swapped = False
        end = end-1
        # цикъл отдясно на ляво:
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1
# cocktailSort(l)
# print(l)

# Сортиране на Шел:
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
            # Все едно се изпълнявва:
            # gapInsertionSort(l,0,2)
            # gapInsertionSort(l,1,2)
        print("След разместване с отстояние",sublistcount,"Списъка е",alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
            #range(0+2=2,5,стъпка=2)
            #i =[2,4]
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue

# shellSort(l)
# print(l)

# Сортиране с ведра (Bucket-Sort)
def bucketSort(x):
    arr = []
    slot_num = 10 # 10 slots, size is 0.1
    for i in range(slot_num):
        arr.append([])
        # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
        # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i]) # concatenate the result
        k=0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1
    return x

def buckets(x):
    f=[[] for i in range(10)]
    new=[]
    for i in range(len(x)):
        n=int(str(x[i])[0]) #първата цифра от числото
        f[n].append(x[i])
    print(f)
    for ll in f:
        if ll!=[]:
            p=permutation_sort(ll)
            new.extend(p)
    x=new
    return x

def buckets123(x):

    b=[[],[],[]]
    # b[0]=[] # за едноцифрени числа
    # b[1]=[] # за двуцифрени числа
    # b[2]=[] # за трицифрени числа
    for y in x:
        if len(str(y))==1: b[0].append(y)
        elif len(str(y)) == 2: b[1].append(y)
        else: b[2].append(y)
    f=[[] for i in range(19)]
    new=[]
    for bb in range(len(b)):
        if bb==0: f[0].extend(b[0])
        elif bb==1:
            for bbb in b[bb]:
                n=int(str(bbb)[0]) #първата цифра от двуцифреното числото
                f[n].append(bbb)
        else:
            for bbb in b[bb]:
                n=int(str(bbb)[0])+9 #първата цифра от трицифреното числото
                f[n].append(bbb)
    # print(f)
    for ll in f:
        if ll!=[]:
            p=permutation_sort(ll)
            new.extend(p)
    x=new
    return x
# l=[93,42,69,202,90,100,52,51,22,29,201,101]
# print(l)
# print(buckets123(l))

# Radix-sort сортиране
def radixsort(x):
    #x=[(7,4,6) (5,1,5) (2,4,6) (2, 1, 4) (3, 2, 4)]
    # wsqka redica ima ednakyw broj elementi
    n=len(x[0]) #брой на елементите в редиците
    k=len(x) # колко редици имам
    d = dict()
    ii=list(range(n))[::-1]
    for i in ii:
        if len(d)==0:
            for kk in range(k-1):
                d[kk]=x[kk][i]
            d={k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        else:
            for dk in d.keys():
                d[dk]=x[dk][i]
            d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    import numpy as np
    dkl=np.array(list(d.keys()))
    xnp=np.array(x)
    return xnp[dkl]

test=[[7,4,6], [5,1,5], [2,4,6], [2, 1, 4], [3, 2, 4]]
print(radixsort(test))

# d={0:6,1:5,2:6,3:4,4:4}

def SContainer(l):
    # Пример за използване на модула sortedcontainers
    # Документация: http://www.grantjenks.com/docs/sortedcontainers/
    import sortedcontainers as sc
    sl = sc.SortedList() # създава празен обект
    sl.update(l) # конвертира подаден списък като SortedList
    print(sl)
    sl.add(0) # добавянето на нов елемент винаги става на подходящото място в сортирания списък
    print(sl)
    sl.remove(0) # ако елементът не съществува, получаваме грешка
    sl.discard(1) # ако елементът не съществува, НЕ получаваме грешка
    sl.pop() # по аналогия на списъците, ако не подадем индекс, връща и премахва последния елемент
    # виж SortedDic и SortedSet

def SCollections():
    # ValueSortedDict - речник сортиран по стойност.
    # ItemSortedDict - речник с функции като ключове за сортиране
    # OrderedDict - сортиран речник с богати възможности за индексиране
    # OrderedSet - сортирано множество с богати възможности за индексиране
    # IndexableDict - речник с възможност за числово индексиране
    # IndexableSet - множество с възможност за числово индексиране
    # Документация: http://www.grantjenks.com/docs/sortedcollections/
