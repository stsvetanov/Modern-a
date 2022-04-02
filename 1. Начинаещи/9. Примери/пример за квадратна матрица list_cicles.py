# По дадено число N (въвежда се от клавиатурата) да се генерира и отпе­чата квадратна матрица,
# съдържаща числата от 0 до N2-1, разположени като спирала, започваща от центъра на матрицата и
# движеща се по часовниковата стрелка, тръгвайки в началото надолу (вж. примерите).

N=int(input("Input integer odd number: "))
if N%2==0: N=N+1
# N**2 е броя на елементите в матрицата
# N е броя на редовете и колоните в матрицата
center_indexes=((N-1)//2,(N-1)//2) # форматът е (ред,колона)
print("Central point of indexes: ",center_indexes)
numbers=[i for i in range(N**2)]
print("Numbers to be rotated: ", numbers)
L=[[0]*N for i in range(N)] # създаване на списък със подсписъците, който ще запълваме с numbers, с размерност N*N
print(L)

# Test: N=3
# numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8]
# L=[[4,5,6],[3,0,7],[2,1,8]] или [4,5,6,3,0,7,2,1,8]
# при тест с м-ца 3*3: center_indexes(1,1)
# N-1=2
ind_r=center_indexes[0]
ind_c=center_indexes[1]

print("\nPrinting of ind_r,ind_c,number,next_r,next_c:\n")
while (len(numbers)>0):
# т.к. не се използва условие за проверка на индексите на L, то е напълно въжможно при неправилен алгоритъм да се генерират грешни ин декси
# и в последствие да дава грешка "out of range"

    if ind_r == center_indexes[0] and ind_c==center_indexes[1]: # Движение от централната точка
        next_r = ind_r + 1
        next_c = ind_c

    elif ind_r < center_indexes[0] and next_r==ind_r:
        next_c = ind_c+1 # движение на дясно
        next_r=ind_r
    elif ind_r > center_indexes[0] and next_r==ind_r:
        next_c = ind_c-1 # движение на ляво
        next_r=ind_r
    elif ind_c > center_indexes[1] and next_c == ind_c:
        next_c = ind_c
        next_r = ind_r + 1 # движение на горе
    elif ind_c < center_indexes[1] and next_c == ind_c:
        next_c = ind_c
        next_r = ind_r - 1 # движение на долу

# Изключения (особени случаи):

    if ind_c==0 and ind_r>0: # движение в колона 0 и N-1
        next_r=ind_r-1 # движение на горе
        next_c=ind_c
    elif ind_c==N-1 and ind_r<N-1:
        next_r = ind_r + 1 # движение на долу
        next_c = ind_c
    # движение спрямо левия диагонал
    if ind_r==ind_c and ind_c<center_indexes[1]: # вътрешен горен ляв ъгъл, движението е на дясно
        next_c=ind_c+1
        next_r=ind_r
    elif ind_r==ind_c and ind_c>center_indexes[1]: # вътрешен долен десен ъгъл, движението е надолу, започва нова спирала
        next_c=ind_c
        next_r=ind_r+1
    # движение спрямо десния диагонал
    if ind_r+ind_c==N-1 and ind_c<center_indexes[1]: # вътрешен долен ляв ъгъл, движението е нагоре
        next_c=ind_c
        next_r=ind_r-1
    elif ind_r+ind_c==N-1 and ind_c>center_indexes[1]:# вътрешен горен десн ъгъл, движението е надолу
        next_c=ind_c
        next_r=ind_r+1


    out_number=numbers.pop(0)
    print([ind_r,ind_c,out_number,next_r,next_c])
    L[ind_r][ind_c]=out_number


    ind_r=next_r
    ind_c=next_c

print("\nPrinting results:")
for k in range(N):
    print(L[k])
if len(numbers)==0: message="\nAll numbers were rotated in clock wise from the centeral point."
else: message="There is some error"
print (message)

