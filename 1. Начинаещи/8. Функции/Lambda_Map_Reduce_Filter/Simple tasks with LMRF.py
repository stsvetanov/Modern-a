from functools import reduce
# lambda,map,reduce,filter
# Резултатите от map и filter трябва да се превърне в списък !

# Анонимните функции можем да присвояваме на променливи, тялото на функцията винаги трябва да бъде един израз
a_1=lambda x: x+1
a_2=lambda x: x**2
a_3=lambda x: x//2
a_4= lambda a,b: a+b
a_5= lambda x: x%2==0

a=[a_1,a_2,a_3] # списък от функциите

l=list(range(10))
# l=[0,1,2,3,4,5,6,7,8,9]

for i in a:
    print(list(map(i,l)))

print(list(filter(a_5,l))) #Прави списък от стойностите на l, за които a_5 връща, че са True
print(reduce(a_4,l))
