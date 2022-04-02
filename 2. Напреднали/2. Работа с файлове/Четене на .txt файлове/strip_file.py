import os

with open("mbox-short.txt", "r") as input_file:
    with open("strip_mbox-short.txt", "w") as output:
        for line in input_file:
            if line != "\n":
                output.write(line)

os.remove("mbox-short.txt")
os.rename("strip_mbox-short.txt", "mbox-short.txt")
