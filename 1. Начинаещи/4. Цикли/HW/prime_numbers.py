from math import sqrt
#
# max_num = int(input("Въведете число: "))

# for n in range(max_num):
#     if n <= 1:
#         continue
#     elif n > 2 and n % 2 == 0:
#         continue
#     elif n > 3 and n % 3 == 0:
#         continue
#     elif n > 5 and n % 5 == 0:
#         continue
#     elif n > 7 and n % 7 == 0:
#         continue
#     elif sqrt(n) == round(sqrt(n)):
#         continue
#     else:
#         print(n)

# number=0
# while True:
#     number=input("Въведете число > 1 или stop: ")
#     if number=="stop":
#         print("Потребителски изход от програмата")
#         break
#     elif int(number)>1:
#         break
# if number!="stop":
#     number=int(number)
#
# for num in range(2, number+1):
#     for i in range(2, num + 1):
#         if num % i == 0 and num > 2:
#             break
#         else:
#             print(num)
#             break

number = int(input("Enter any number: "))

for prime_number in range(2, number+1):
    if number > 1:
        for i in range(2, prime_number):
            if (prime_number % i) == 0:
                break
        else:
            print(prime_number)
