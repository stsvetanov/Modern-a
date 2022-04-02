"""
Задача за напреднали:
Да се пише програма, която при въвеждане на 2 думи от клавиатурта, принтира дали първата ли втората въведена е по къса лексикографски (както е в речника)
input:
dog
cat
output:
Second

input:
dog
dogb
output:
First
"""

first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

my_list = [first_word, second_word]
print(my_list)
my_sorted_list = sorted(my_list)
print(my_sorted_list)

if my_list == my_sorted_list:
    print("First")
else:
    print("Second")
