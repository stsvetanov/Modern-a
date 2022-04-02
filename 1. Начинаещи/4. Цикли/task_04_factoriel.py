'''
5! = 5*4*3*2
'''

number = int(input("Въведете число: "))

factorial = 1
for i in range(2, number + 1):
    factorial = factorial * i

print(factorial)

