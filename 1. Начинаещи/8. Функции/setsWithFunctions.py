def andAB(a, b, aB):
    initArr(aB, False)
    k = 0

    for i in range(0, len(a) - 1 + 1, 1):

        for j in range(0, len(b) - 1 + 1, 1):
            if a[i] == b[j]:
                aB[k] = a[i]
                k = k + 1
    print("Сечението на двете множества е: ")

    for i in range(0, k - 1 + 1, 1):
        print(aB[i])

    return k

def arr2set(a):
    n = len(a)
    elements = 0

    for i in range(0, n - 1 + 1, 1):
        k = 1
        if a[i] != 0:

            for j in range(i + 1, n - 1 + 1, 1):
                if a[i] == a[j]:
                    k = k + 1
                    a[j] = 0

            print(str(a[i]) + ":" + str(k))
            elements = elements + 1

    return elements

def arr2set2(a, b):
    j = 0
    n = len(a)

    for i in range(0, n - 1 + 1, 1):

        if a[i] != 0:
            b[j] = a[i]
            j = j + 1

def initArr(myarray, zero):
    if zero == False:

        for i in range(0, len(myarray) - 1 + 1, 1):
            myarray[i] = 0

    else:
        for i in range(0, len(myarray) - 1 + 1, 1):
            myarray[i] = int(input())

def orAB(a, b, aB):
    n = len(a) + len(b)

    tmpAB = [0] * (n)

    for i in range(0, n - 1 + 1, 1):

        if i < len(a):
            tmpAB[i] = a[i]
        else:
            j = n - i - 1
            tmpAB[i] = b[j]

    br = arr2set(tmpAB)
    setAB = [0] * (br)

    arr2set2(tmpAB, setAB)

    print("Обединението на двете множества е: ")

    initArr(aB, False)

    for i in range(0, br - 1 + 1, 1):
        aB[i] = setAB[i]
        print(setAB[i])

def xorAB(a, b, aB):
    an = len(a)
    bn = len(b)
    initArr(aB, False)
    k = 0

    for i in range(0, an - 1 + 1, 1):
        br = 0
        test1 = a[i] != 0

        for j in range(0, bn - 1 + 1, 1):
            test2 = b[j] != 0
            if test1 and test2:
                if a[i] == b[j]:
                    br = 1
                    j = bn - 1
        if br == 0:
            aB[k] = a[i]
            k = k + 1

    print("XOR на множествата е:")

    for i in range(0, an - 1 + 1, 1):
        if aB[i] != 0:
            print(aB[i])

print("Въведете брой на елементите за масив А.")
n = int(input())
arrA = [0] * (n)

initArr(arrA, True)
br = arr2set(arrA)
setA = [0] * (br)

arr2set2(arrA, setA)

print("Въведете брой на елементите за масив В.")
n = int(input())
arrB = [0] * (n)

initArr(arrB, True)
br = arr2set(arrB)
setB = [0] * (br)

arr2set2(arrB, setB)

aBand = [0] * (len(setA) + len(setB))
aBor = [0] * (len(setA) + len(setB))
aBxor = [0] * (len(setA) + len(setB))

andAB(setA, setB, aBand)
orAB(setA, setB, aBor)
xorAB(aBor, aBand, aBxor)
