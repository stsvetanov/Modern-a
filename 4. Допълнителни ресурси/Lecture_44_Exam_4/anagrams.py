try:
    words_ = ["shore", "bibles", "heros", "horse", "beta"]
    word_to_check = "horse"
    word_to_check_sorted = sorted(word_to_check)

    anagrams = []
    for word in word_to_check:
        if word != word_to_check and word_to_check_sorted == sorted(word):
            anagrams.append(word)

    if anagrams:
        anagrams.sort()
        for a in anagrams:
            print(a)
    else:
        print("NO ANAGRAMS")

except Exception as e:
    print("INVALID INPUT")