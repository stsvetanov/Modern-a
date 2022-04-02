def compare(filename1, filename2):
    f = open(filename1, "r")
    g = open(filename2, "r")
    content1 = f.readline()
    content2 = g.readline()
    line_number = 1
    while content1 != '' or content2 != '':
        line1 = content1.strip('\n')
        line2 = content2.strip('\n')
        if line1 != line2:
            return line_number

        content1 = f.readline()
        content2 = g.readline()
        line_number += 1
    f.close()
    g.close()

    return 0


print(compare('BoringTextFile.txt', 'DifferentBoringTextFile-ExtraLine.txt'))