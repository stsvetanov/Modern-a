'''
1. Модифицирайте програмта на изчисляване на комплиментарна ДНК, така че да чете входните данни
от файл и да записва резултата в друг файл.
'''

def complement_dna(dna):
    rep_1 = dna.replace("A", "t")
    rep_2 = rep_1.replace("T", "s")
    rep_3 = rep_2.replace("G", "c")
    rep_4 = rep_3.replace("C", "g")
    complementary_dna = rep_4.upper()
    return complementary_dna


dnk = open("dnk.txt")

for line in dnk:
    print(line)
    complement_dna(line)
dnk.close()

dnk_c = complement_dna(line)

comp_dnk = open("complementary_dnk.txt", "w")
comp_dnk.write(dnk_c)
print(dnk_c, end="")
comp_dnk.close()