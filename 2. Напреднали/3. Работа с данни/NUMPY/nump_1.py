import numpy as np
import random as rd

rows=5
cols=4
shape=(rows,cols)

# 1. Напишете Python програма, за да създадете 2D масив с 1-ци на първия ред и
# последния ред, първата и последната колона и 0-ли в осталата част.
print("Task 1:")

mat=np.zeros(shape,dtype=int)
# l=[[...],[...],[...]] => l[1][2], npm[1,2]
mat[0,:]=mat[-1,:]=1 # всички клетки от първи ред = всички клетки от последен ред = 1
mat[:,0]=mat[:,-1]=1 # всички клетки от първа колона = всички клетки от последна колона = 1

print(mat)
#
# 2. Напишете програма Python, за да добавите граница (от 0-ли) около съществуващ масив.
print("Task 2:")
L=[rd.randint(1,100) for i in range(shape[0]*shape[1])]
print(L)

mat=np.zeros((shape[0]+2,shape[1]+2),dtype=int)
# mat=np.zeros((7,6),dtype=int)
matL=np.array(L).reshape(shape)
mat[1:-1,1:-1]=matL
print(mat)

# 3. Напишете Python програма, за да преобразувате градуси по Целзий в градуси по Фаренхайт.
# Градусите по Целзий се съхраняват в NumPy масив. F = (9 * С + 32 * 5) / 5
print("Task 3:")
Celsius=[rd.randint(0,100) for i in range(20)] # списък с произволни стойности от 0 до 100
shape=(5,4)
mat_c=np.array(Celsius).reshape(shape)
print(mat_c)
mat_f=(mat_c*9+32*5)/5 # нова матрица със същите размери, но със стойностите по фаренхайт
mat_c[1:4,1:3]=(mat_c[1:4,1:3]*9+32*5)/5 # преобразуване на стойности за конкретен диапазон от клетки
# частична промяна на матрицата, чрез точно указани диапазони за редовете и колоните
print(mat_c)
print(mat_f)


# # 4. Напишете Python програма, за да преобразувате градуси по Фаренхайт в градуси по Целзий.
# # Градусите по Фаренхайт се съхраняват в NumPy масив. С = 5 * (F-32) / 9
# # Градусите по Целзий се съхраняват в NumPy масив. F = (9 ° С + 32 * 5) / 5
# print("Task 4:")
# Farenh=[rd.randint(0,100) for i in range(20)]
# shape=(5,4)
# mat_f=np.array(Farenh).reshape(shape)
# print(mat_f)
# mat_c=5*(mat_f-32)
# print(mat_c)
# print(mat_f)


# 5. Напишете Python програма, за да проверите дали всеки елемент от 1-D масив също присъства във и втория масив.
print("Task 5:")
# L_1=[rd.randint(1,100) for i in range(20)]
# L_2=[rd.randint(1,100) for i in range(20)]
L_1=list(range(1,11))
L_2=list(range(-5,16))
mat_1=np.array(L_1)
#mat_2=np.zeros((7,6),dtype=int)
#mat_2[1:-1,1:-1]=mat_1
mat_2=np.array(L_2)
check=True
for r in range(mat_1.size):
    if mat_1[r] not in mat_2:
        check=False
        break
print(mat_1)
print(mat_2)
print(check)
#
print("Task 6")
# 6. Напишете Python програма, за да намерите общите елементи в два масива.
L_1=[rd.randint(1,100) for i in range(20)]
L_2=[rd.randint(1,100) for i in range(20)]
mat_1=np.array(L_1).reshape(shape)
mat_2=np.array(L_2).reshape(shape)
print(mat_1)
print(mat_2)

condition=np.in1d(mat_1, mat_2).reshape(shape)
print(condition)
common=mat_1[condition]
print(common)
condition=np.in1d(mat_2, mat_1).reshape(shape)
print(condition)
common=mat_2[condition]
print(common)
# np.in1d(A,B,assume_unique=True) - връща всички елементи от А, които се срещат в B, като
# assume_unique=True означава, че повтарящите се елементи няма да бъдат проверявани и връщани
#
# # или
common=np.intersect1d(mat_1, mat_2) # връща всички елементи от А, които се срещат в B, но сортирани и без повторенията
print(common)
#
# # ако е с цикли, само тогава има значение дали масивите не са с еднакъв shape
# com=[]
# mat_1_1D=mat_1.reshape(mat_1.shape[0]*mat_1.shape[1])
# # mat_1_1D=mat_1.reshape(mat_1.size) # алтернатива на горния ред
# mat_2_1D=mat_2.reshape(mat_2.shape[0]*mat_2.shape[1])
# for i in mat_1_1D:
#     for j in mat_2_1D:
#         if i == j:
#             com.append(i)
# mat_com=np.array(list(set(com)))
# print(mat_com)
#
# # 7. Напишете Python програма, за да получите уникалните елементи от даден масив.
# print("Task 7")
# mat_1=np.array([1,2,3,4,5,4,3,2,1,2,3,4])
# unique=np.array(list(set(mat_1)))
# # set(mat_1) превръщаме в множество, а всяко множество е с уникални (т.е. без повтаряне) елементи
# # list(set(mat_1)) преобразуваме множеството в списък и така го подаваме на numpy за образуване на масив
# # Когато матрицата е двумерна или с по-голям размер, тогава първо трябва да направим .reshape до едномерна
# # и едва след това да преобразуваме в множество: set(mat_1.reshape(mat_1.size))
# print(unique)
#
# # 8. Напишете Python програма, за да намерите обединението на два масива.
# # Обединението да върне уникалния, сортиран набор от стойности, от двата входни масива.
# print("Task 8")
# L_1=[rd.randint(1,10) for i in range(5)]
# L_2=[rd.randint(1,10) for i in range(5)]
# mat_1=np.array(L_1)
# mat_2=np.array(L_2)
# # Без повторения на числата дори и да има такива
# joined=np.array(list(set(mat_1)|set(mat_2)))
# set(mat_1)|set(mat_2) връща в сортиран ред обединението
# print(mat_1)
# print(mat_2)
# print(joined)
# # с повторения на числата, ако има такива:
# mat=L_1+L_2
# mat=np.array(mat)
# mat.sort() #.sort като метод променя подредбата в обекта
# # np.sort(mat) # np.sort в този случай (за разлика от ред 124) не сортира ?!
# print(mat)

# # 9.  Напишете Python програма, която проверява дали масивът е палиндром
# # (т.е. четен в обратен ред същия масив ли се получава)
# # ако е с четен брой елементи:
# print("Task 9")
# L_1=[rd.randint(1,100) for i in range(20)]
# # L_1=[1,1,1,1,1,5,1,1,1,1,1] # нечетен брой
# L_1=[1,2,1,2,2,1,2,1] # четен брой
#
# mat_1=np.array(L_1)
#
# m_1 = mat_1[0:np.size(mat_1) // 2]
# if np.size(mat_1)%2==0:
#     m_2=mat_1[np.size(mat_1)//2::]
# else:
#     m_2 = mat_1[np.size(mat_1) // 2 + 1::]
# m_2 = m_2[::-1]  # четене в обратен ред
# check = m_1 == m_2
# # check e вектор с проверките за равенство на елементите, има дължина=mat_1.size//2 и е също np.array
# # Проверка дали всички елементи съвпадат, т.е. ако върне True ще имаме палиндром, ако върне False ще имам
# if False in check:
#     print(False)
# else:
#     print(True)
# print(mat_1)
# print(m_1)
# print(m_2)
# print(check)

#
#
#
# 10. Напишете Python програма, за да създадете 2-D масив с 1-ци по диагонала и нули под и над диагонала.
print("Task 10")
n=5
mat=np.zeros((n,n),dtype=int)
for i in range(n):
    mat[i,i]=1
print(mat)
#
# 11. Напишете Python програма, за да премахнете всички стойности в масив,
# за които е вярно: 2 * value == value ^ 2. Колко елемента има филтрирания масив?
print("Task 11")
# L_1=[rd.randint(1,100) for i in range(20)]
L_1=[1,2,0,4,3,5,9,16]
mat_1=np.array(L_1)
print(mat_1)
condition=np.where(2*mat_1 == mat_1**2)
# np.where връща индексите на елементите, които отговарят на поставеното условие
filtered=mat_1[condition]
print(condition)
print(filtered)
print(np.size(filtered))

# 12. Напишете Python програма, която да замени с 1 всички стойности в масив,
# за който е вярно: 2 * value > value +15. Колко елемента са с подменени стойности и колко са 1-ци?
print("Task 12")
L_1=[rd.randint(1,100) for i in range(20)]
mat_1=np.array(L_1)
print(mat_1)
condition=np.where(2*mat_1 > mat_1+15)
print(condition)
mat_1[condition]=1
print(mat_1)
print(np.size(condition)) # брой елементи с подменени стойности
onces=np.where(mat_1==1)
print(np.size(onces)) # общ брой на единиците


# 13. 1) квадратна матрица от нули, а по главния диагонал да има случайни числа.
# 2) каква сумата на числата по диагонала ?

n=5
shape=(n,n)
mat=np.zeros(shape,dtype=int)
for i in range(n):
    mat[i,i]=rd.randint(1,100)
print(mat)
print(mat.diagonal())
print(sum(mat.diagonal()))
print(mat.sum())


