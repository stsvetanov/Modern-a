a,b=1,1
n=int(input("Въведете броя на числата в редицата на Фибоначи: "))
for i in range(n):
	a=b,a+b
print(b)