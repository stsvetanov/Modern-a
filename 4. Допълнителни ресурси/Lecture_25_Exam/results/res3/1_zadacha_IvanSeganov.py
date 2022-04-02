def compare(text1, text2):
    text1 = open(text1).read().splitlines()
    text2 = open(text2).read().splitlines()

    diff = set(text2).difference(text1)
    if len(diff) == 0:
        diff = "0"

    return diff

text1 = '../BoringTextFile.txt'

# Тестове с 3те различни варианта
# text2 = '../BoringTextFile.txt' # 1. Вариант - файловете са еднакви и извежда 0
# text2 = '../DifferentBoringTextFile-ExtraLine.txt' # 2. Вариант - Има допълнителна линия и разлики
text2 = '../DifferentBoringTextFile-SameLength.txt' # 3. Вариант - Еднаква дължина на файла но има и разлики

otg = list(compare(text1, text2))
for elem in otg:
    print(elem)