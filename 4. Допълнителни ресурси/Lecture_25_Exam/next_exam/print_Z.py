def figure(m, n):
    line = '+' * (m+1)
    print(line)
    for i in range(m-1, 0, -n):
        line = ' ' * i + '+'
        print(line)
    line = '+' * (m+1)
    print(line)


figure(5, 1)


