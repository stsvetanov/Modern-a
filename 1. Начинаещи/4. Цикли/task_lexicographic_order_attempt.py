first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

# Определяне на броят на сравняваните букви между двете думи.
if len(first_word) <= len(second_word):
    count_letter = len(first_word)
else:
    count_letter = len(second_word)

# Сравнява числовата стойност на буквите по ASCII таблица.
for n in range(count_letter):
    if first_word[n] < second_word[n]:
        print("First")
        break
    elif first_word[n] > second_word[n]:
        print("Second")
        break
    else:  # Коя дума е с повече букви.
        if len(first_word) < len(second_word):
            print("First")
            break
        elif len(first_word) > len(second_word):
            print("Second")
            break
        else:
            if n < count_letter - 1:
                continue
            else:
                print("The same word was entered.")