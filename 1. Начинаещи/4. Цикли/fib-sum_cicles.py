a,b=1,1
n=int(input("Въведете числото n"))
S=a
for i in range (n):
	a,b=b,a+b
	S=S+b
print(S)
