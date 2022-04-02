# num = int(input("Въведете числото N < 20: "))
# if num < 20:
#     for n in range(num):
#         for m in range(1, num + 1):
#             if n + m < 10:
#                 print("" * (9 - m), n + m, end=" ")
#             else:
#                 print(n + m, end=" ")
#         print()


n=input("Въведете число >1 и <20 или stop: ")
n=int(n)

for i in range(1, n+1):
    for j in range(i, i+n):
        print(j, end='')
    print()
