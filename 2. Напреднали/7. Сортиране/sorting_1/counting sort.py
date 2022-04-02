# Първоначален списък с елементи
arr = [10, 7, 8, 9, 1, 5,9,7,8,5,1,1,1,1]
print(arr)

# set(arr) взема само уникалните елементи от първоначалния списък и ги връща сортирани
# list(set-a) превръща обратно множеството в списък, за да бъде итеративно
arr_set=list(set(arr))
print(arr_set)

# Нов празен списък, в който преброяваме броя на елементите от arr_set
arr_counts=[]
for i in range(len(arr_set)):
    arr_counts.append(arr.count(arr_set[i]))
print(arr_counts)
# Нов празен списък за подредените елементи
new_arr=[]
for i in range(len(arr_set)):
    new_arr+=[arr_set[i]]*arr_counts[i]
    #Добавяме n на брой пъти (записано в масива arr_counts), поредното число от конвертираното множество
print(new_arr)
