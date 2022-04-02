# from __future__ import with_statement
from difflib import Differ

filename1 = "../BoringTextFile.TXT"
filename2 = "../DifferentBoringTextFile-ExtraLine.TXT"
filename3 = "../DifferentBoringTextFile-SameLength.TXT"

def Differnce_file(compare, original):
    with open(compare, 'r') as file1:
        with open(original, 'r') as file2:
            difference = set(file1).difference(file2)
#We can use intersection() method instead of difference() if we need to print the common items
    # rotate compare - original

    with open('diff.txt', 'w') as file_out:
        for line in difference:
            file_out.write(line)

Differnce_file(filename2, filename1)

with open("diff.txt") as fp:
    print("\n Difference b/n file 1 and file 2:\n", fp.read())

Differnce_file(filename3, filename1)

with open("diff.txt") as fp:
    print("\n Difference b/n file 1 and file 3: \n", fp.read())








#
#
# with open(filename1) as f1, open(filename2) as f2:
#     differ = Differ('- ')
#
#     for line in differ.compare(f1.readlines(), f2.readlines()):
#         # if f1.readlines() != f2.readlines():
#         #     print(line)
#         if line.startswith(" "):
#             print(line[2:], end="")

# from difflib import Differ
#
# with open('cfg1.txt') as f1, open('cfg2.txt') as f2:
#     differ = Differ()
#
#     for line in differ.compare(f1.readlines(), f2.readlines()):
#         if line.startswith(" "):
#             print(line[2:], end="")


# with open(filename1) as f1:
#    with open(filename2) as f2:
#       file1list = f1.read().splitlines()
#       file2list = f2.read().splitlines()
#       list1length = len(file1list)
#       list2length = len(file2list)
#       if list1length == list2length:
#           for index in range(len(file1list)):
#               if file1list[index] == file2list[index]:
#                   print(file1list[index] + "==" + file2list[index])
#               else:
#                   print(file1list[index] + "!=" + file2list[index]+" Not-Equel")
#       else:
#           print ("difference inthe size of the file and number of lines")
#

# with open(filename1, 'r') as file1:
#     with open(filename2, 'r') as file2:
#         print(type(file2))
#         same = file1.difference(file2)
#
# same.discard('\n')
# print (same)
# with open('some_output_file.txt', 'w') as file_out:
#     for line in same:
#         file_out.write(line)
#
# count = 0
# with open(filename1) as f1, open(filename2) as f2:
#     while True:
#         for line1 in f1:
#             count += 1
#             for line2 in f2
#      ...
#      out_file.write(parsed_line)
#
#     if not line1:
#


#             break
# with open(filename1) as f1:
#    with open(filename2) as f2:
#        while True:
#             count += 1
#             line = fp.readline( )
#
#         if not lin
#             break
#         print("Line{}: {}".format(count, line.strip( )))