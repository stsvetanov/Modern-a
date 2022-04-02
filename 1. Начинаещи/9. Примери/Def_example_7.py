def kursova(chislo):
    proverka = chislo
    suma = 0
    broi = 0
    while proverka != 0:
        cifra = proverka % 10
        proverka = proverka // 10
        suma += cifra
        broi += 1
    sredno = round(suma / broi,2)
    redica = suma, sredno, {chislo:broi}
    return redica

print("Kursova")
inputstr = input("Vuvedete spisuk ot chisla:")
spisuk = inputstr.split()
for i in range(len(spisuk)):
    spisuk[i] = int(spisuk[i])
    redichka = kursova(spisuk[i])
    print(redichka)
    print("\n")
