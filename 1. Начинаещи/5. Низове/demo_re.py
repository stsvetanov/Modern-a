import re

# hand = open('mbox-short.txt')
#
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)


# # We could change our program to match only lines where “From:” was at the beginning of the line
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)

# ############
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('ˆF..m:', line):
#         print(line)


# ############
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('ˆF..m:.+@', line):
#         print(line)

# #################
# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print(lst)

# read all the lines in a file and print out anything that looks like an email address
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\S+@\S+', line)
#     if len(x) > 0:
#         print(x)

# # # read all the lines in a file and print out anything that looks like an email address
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)

######################
# hand = "Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772"
# # hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('ˆDetails:.*rev=([0-9]+)', line)
#     if len(x) > 0:
#         print(x)

# New Revision: 39772
# hand = open("mbox-short.txt")
# nums = list()
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('New Revision: ([0-9]+)', line)
#     if len(x) == 1:
#         val = float(x[0])
#         nums.append(val)
# print(len(nums))
# print(sum(nums)/len(nums))
