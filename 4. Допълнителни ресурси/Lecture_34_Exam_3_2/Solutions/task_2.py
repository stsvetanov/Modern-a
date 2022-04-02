fhand = open('../task2.txt')
wordsfile = []
n = 0
try:
    for line in fhand:
        line = line.rstrip()
        wordsfile.append(line)
    word = input("Enter word:")
    for each in wordsfile:
        if word == each:
            continue
        if sorted(word) == sorted(each):
            print(each)
            n += 1
        if n == 0:
            print("No Anagrams")
except:
    print("INVALID INPUT")