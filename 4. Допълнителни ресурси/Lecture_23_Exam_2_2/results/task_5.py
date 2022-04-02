def matched(str):
    count = 0
    count_open = 0
    count_close = 0
    for i in str:
        count += 1

        if i == ")" and count_open == 0:
            print(f"WRONG {count}")
            exit()
        elif i == "(":
            count_open += 1
        elif i == ")":
            count_open -= 1
            count_close += 1

    if count_open != 0:
        print("WRONG")
    else:
        print(f"OK {count_close}")


inpt = input("Enter str. for () check:")
matched(inpt)