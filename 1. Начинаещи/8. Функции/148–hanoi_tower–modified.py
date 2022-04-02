def hanoi(n, fr, to, spare):
    if n == 1:
        print("Премести диск 1 от колона " + fr + " в колона " + to + ".")
    else:
        hanoi(n - 1, fr, spare, to)
        print("Премести диск " + str(n) + " от колона " + fr + " в колона " + to + ".")
        hanoi(n - 1, spare, to, fr)

# Main
print("Въведи брой дискове:")
n = int(input())
hanoi(n, "A", "B", "C")
