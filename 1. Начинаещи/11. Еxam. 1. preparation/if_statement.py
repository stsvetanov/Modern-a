def print_marks(mark):
    if mark < 2.5:
        print('poor')
    elif mark < 3.5:
        print('middle')
    elif mark < 4.50:
        print('good')
    elif mark < 5.50:
        print('very good')
    else:
        print('excellent')


mark = float(input('Enter mark: '))
print_marks(mark)
