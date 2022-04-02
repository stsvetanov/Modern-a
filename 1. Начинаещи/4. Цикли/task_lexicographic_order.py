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

len_first_word = len(first_word)
len_second_word = len(second_word)
len_shorter_word = len_first_word < len_first_word and len_first_word or len_second_word
equal = True

if len_first_word == len_second_word:
    for letter in range(len_shorter_word):
        if first_word[letter] < second_word[letter]:
            print("First")
            equal = False
            break
        elif first_word[letter] > second_word[letter]:
            print("Second")
            equal = False
            break
else:
    print(len_first_word < len_second_word and "First" or "Second")
    equal = False

if equal:
    print("Equal")
