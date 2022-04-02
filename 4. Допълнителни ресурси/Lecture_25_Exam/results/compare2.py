def compare(fname1, fname2):
    same = True

    f1 = open(fname1)
    f2 = open(fname2)

    f1_line = f1.readline()
    f2_line = f2.readline()

    line_no = 1

    while f1_line != '' or f2_line != '':
        f1_line = f1_line.strip('\n')
        f2_line = f2_line.strip('\n')
        if f1_line != f2_line:
            same = False
            if f2_line != '' and f1_line != '':
                return line_no
            elif f2_line == '':
                return line_no
            elif f1_line == '':
                return line_no

        f1_line = f1.readline()
        f2_line = f2.readline()
        line_no += 1
    f1.close()
    f2.close()
    if same:
        return 0

print(compare('BoringTextFile.txt', 'DifferentBoringTextFile-ExtraLine.txt'))