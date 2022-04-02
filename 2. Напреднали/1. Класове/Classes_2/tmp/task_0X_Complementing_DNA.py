my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

replacement1 = my_dna.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())


def complement(input_string):
    base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compliment_letters = []

    for base in input_string:
        compliment_letters.append(base_complement.get(base))

    # compliment_letters = [base_complement[base] for base in input_string]

    return ''.join(compliment_letters)


def reverse_complement(input_string):
    return complement(input_string[::-1])


print(my_dna)
print(complement(my_dna[::-1]))
print(reverse_complement(my_dna))


# reverse_complement_v2 = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
# print(reverse_complement_v2(my_dna))

print("Translated string: {}".format(my_dna.translate({'A':'T','C':'G','G':'C','T':'A'})))


# Using translate method
firstString = "abc"
secondString = "ghi"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString)

# translate string
print("Translated string:", string.translate(translation))

# translation table - a dictionary
translation = {97: None, 98: None}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))
