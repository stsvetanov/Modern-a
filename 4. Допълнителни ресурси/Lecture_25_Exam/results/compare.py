def compare(filename1, filename2):
    """Input is two strings containing file names.
        Output is 0 if files are identical;
        or the line number where they first differ."""
    # Write the code!
    f = open(filename1, "r")
    g = open(filename2, "r")
    content1 = f.readlines()
    content2 = g.readlines()
    f.close()
    g.close()
    for index, line1 in enumerate(content1):
        line2 = content2[index]
        if line1 != line2:
            return index
    if len(content1) != len(content2):
        return index
    else:
        return 0


print(compare("BoringTextFile.txt", "DifferentBoringTextFile-ExtraLine.txt"))
