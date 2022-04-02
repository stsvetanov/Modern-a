'''
input = 4
*
**
***
****
'''

number = int(input("Enter number: "))

for row in range(1, number + 1):
    print(' ' * (number - row) + '* ' * row)

