# name = input('Enter file:')
name = "words.txt"
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count

print("The most used word {most_used_word} appears {count} times".format(most_used_word=bigword, count=bigcount))

d_view = [(v, k) for k, v in count.iteritems()]
d_view.sort(reverse=True) # natively sort tuples by first element
print(d_view)


