
def function_score(s):
    if s < 2.5:
        print("Слаб (2)")
    if 2.5 <= s < 3.5:
        print("Среден (3)")
    if 3.5 <= s < 4.5:
        print("Добър (4)")
    if 4.5 <= s < 5.5:
        print("Много добър (5)")
    if 5.5 <= s:
        print("Отличен (6)")


score = float(input("Въведи оценка: "))
function_score(score)
