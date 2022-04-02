my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement = []

for nucleotide in my_dna:
    if nucleotide == 'A':
        complement.append('T')
    elif nucleotide == 'C':
        complement.append('G')
    elif nucleotide == 'T':
        complement.append('A')
    else:
        complement.append('C')

# print(complement)
answer = ' '

for comp in complement:
    answer.join(comp)

print(answer)
str1 = ''.join(complement)
# return string
str1.join("sdfsdf")
str1.join("asdffasdf")
print(str1)

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])

print(listToStr)