def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    # fr - колона 1
    # to - колона 2
    # spare - колона 3
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
Towers(5,"A", "B", "C")

# https://bg.wikipedia.org/wiki/Файл:Tower_of_Hanoi_4.gif

def hanoi(n, fr, to, spare):
    if n == 1:
        print("Премести диск 1 от колона " + fr + " в колона " + to + ".")
    else:
        hanoi(n - 1, fr, spare, to)
        print("Премести диск " + str(n) + " от колона " + fr + " в колона " + to + ".")
        hanoi(n - 1, spare, to, fr)

# Main
# print("Въведи брой дискове:")
# n = int(input())
hanoi(5, "A", "B", "C")