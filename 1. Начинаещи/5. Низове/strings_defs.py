def indexI(a):
    # a може да бъде списък
    n = len(a)
    for i in range(n):
        if a[i] > 0:
            print(i)
    print("Край")

# Main
n = 5
# arr = [0] * (n) # списък от 5 елемента, запълнен с нули
#
# for i in range(n):
#     arr[i] = int(input()) # от клавиатурата (input) се въвежда число, а с
#     # функцията int() преобразуваме въведения стринг в цяло число, ако е възможно
def indexI_2(a):
    # a може да бъде списък
    l=[a[i] for i in range(len(a)) if a[i] > 0]
    return (l)
st='Въведете число от списъка с индекс '
arr=[int(input(st + str(i) + ': ')) for i in range(n)]
# indexI(arr)
print(indexI_2(arr))
# range(start=0, stop, step=1)
# range(stop)