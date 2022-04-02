# Сортиране:
# _______________________
arr = [7, 3, 5, 1, 9, 8, 4, 6,6,6,1]
# метод на мехурчето
def bubble(arr):
# Нека е даден масив arr от числа
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr

# метод на пряката селекция
def SelSort(A):
    for i in range(len(A)):
    # Търсим най-малкия елемент в останалата част от масива
        min_indx = i
        for j in range(i+1, len(A)):
            if A[min_indx] > A[j]: min_indx = j
            # Поставяме най-малкия елемент в началото, като го
            # разменяме с елемента разположен там
        A[i], A[min_indx] = A[min_indx], A[i]
        print(arr)
    return(A)
# метод на сортиране чрез вмъкване
def sortINS(arr):
    #print(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Местим елементите от arr[0..i-1], които са по-големи # от текущия елемент key, с 1 позиция в дясно
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    return (arr)
# метод "Бързо сортиране"
def qSort(arr):
    def partition(arr, low, high):
    # Най - левия елемент: този с индекс low
    # Най - десния елемент: този с индекс high
    # Случаен елемент: с функция от рода на random
    # Среден елемент: този с индекс low + high // 2
        i = (low-1) # индекс на последния по-малък елемент от pivot
        pivot = arr[high] # за pivot избираме най-десния елемент
        for j in range(low, high):
        # Ако текущия елемент е <= на pivot
            if arr[j] <= pivot:
            # отива в ляво с размяна с елемента след последния от малките # и увеличаваме индекса на малките с 1
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(arr, low, high):
        if len(arr) == 1:return arr
        if low < high:
        # pi е индекса на pivot, arr[pi] е на правилна позиция
            pi = partition(arr, low, high)
        # Сортираме елементите преди и след pivot
            quickSort(arr, low, pi-1)
            quickSort(arr, pi + 1, high)
    b=quickSort(arr,0,len(arr)-1)
    print(b)
    return b
def quickSort(a):
    if len(a) == 0:
        return a
    half = len(a) // 2
    f = [i for i in a if i < a[half]]
    # f e lqwo
    s = [i for i in a if i == a[half]]
    # s e pivot-a
    t = [i for i in a if i > a[half]]
    # t e dqsno
    return quickSort(f) + s + quickSort(t)

# Сортиране с броене
def sortCount(arr):
    output=[]
    arrset=list(set(arr))
    counts=[arr.count(a) for a in arrset]
    for i in range(len(arrset)):
        output.extend([arrset[i]]*counts[i])
        print(output)
    return output

def binSearch(arr,n):
    # arr=quickSort(arr)
    # n е числото, което търсим
    left = -1
    right = len(arr)
    while (left + 1 < right):
        mid = (left + right) // 2
        if (arr[mid] >= n):  # Проверка дали P(arr[mid])==true
            right = mid
        else:
            left = mid
    if arr[right] == n:
        s="Открит на позиция: " + str(right)
    else:
        s="Не е открит, трябва да бъде преди позиция: " + str(right)
    return s

# Тестване на функциите за сортиране
print(arr)
arrsorted=quickSort(arr)
print(arrsorted)
a=binSearch(arrsorted,6)
print(a)