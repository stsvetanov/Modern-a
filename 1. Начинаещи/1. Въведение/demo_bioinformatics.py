# # store a short DNA sequence in the variable my_dna
# my_dna = "ATGCGTA"
# # now print the DNA sequence
# print(my_dna)

# # Concatenation
# my_dna = "AATT" + "GGCC"
# print(my_dna)

# upstream = "AAA"
# downstream = "GGG"
# my_dna = upstream + "ATGC" + downstream
# # my_dna is now "AAAATGCGGG"
# print(my_dna)

# dna_length = len("AGTC")
# print(dna_length)
# #
# my_number = len("AGTC")
my_dna = "AGTCG"
# # my_number is 4
# print(my_dna.lower())

length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
print("length: " + str(length))
print("A count: " + str(a_count))
print("T count: " + str(t_count))