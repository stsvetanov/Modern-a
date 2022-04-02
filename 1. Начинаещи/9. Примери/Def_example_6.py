#ФН ГГФ_К2_80036

def getCount(number):
    br = 0
    while int(number)!=0:
        br+=1
        number/=10

    return br

def sumFunc(number):
    sum = 0
    while int(number)!=0:
        sum += int(number)%10
        number/=10

    return sum

def multipFunc(number):
    sum = 0
    while int(number) != 0:
        sum += int(number) % 10
        number /= 10

    return sum
def solve(number):
    count = getCount(number)
    sum = sumFunc(number)/count
    d= {number:multipFunc(number)}

    return count, sum, d

# if __name__== '__main__':
#     l = []
#     print("Въведи броя на числата, които ще въвеждаш")
#     n = int(input())
#     for i in range(n):
#         l.append(int(input()))
#     for i in range(len(l)):
#         a,b,c = solve(l[i])
#         print(a)
#         print(b)
#         print(c)


# Вариант 2:
def solver(i):
    getc=len(str(i)) # броя на цифрите в числото
    avg=round(sum([int(k) for k in list(str(i))])/getc,2)
    pro=1
    for k in list(str(i)):
        pro*=int(k)
    return (getc,avg,{i:pro})

def kbd_list_input(n):
    l = []
    for i in range(n):
        l.append(int(input()))
    return l

print("Въведи броя на числата, които ще въвеждаш")
n = int(input())
L=kbd_list_input(n)
result=list(map(solver,L))
print(result)







