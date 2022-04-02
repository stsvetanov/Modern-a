'''
A = T
T = A
G = C
C = G
'''

# compliment = {'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}

def complement_dna(dna):
    replacement1 = dna.replace('A', 't')
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('G', 'c')
    replacement4 = replacement3.replace('C', 'g')
    complementary_dna = replacement4.upper()

    return complementary_dna


my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print(complement_dna(my_dna))
