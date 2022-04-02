'''
N = 3

123
234
345
'''

number = int(input("Enter some number: "))

# count = 1
# for i in range(5):
#     print("Outer loop")
#     for k in range(5):
#         print(k)
#         count += 1
#         print(count)

for i in range(1, number + 1):
    print('\n')
    for k in range(i, i + number):
        print(k, end = " ")

