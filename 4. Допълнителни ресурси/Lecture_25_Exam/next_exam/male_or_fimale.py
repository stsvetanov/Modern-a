def char_count(text):
    counter_e_i = 0
    counter_o_a = 0
    size = len(text)
    for element in text:
        if element == "o" or element == "a":
            counter_o_a = counter_o_a + 1
        elif element == "e" or element == "i":
            counter_e_i += 1
    return counter_o_a / counter_e_i


text_1 = "Me Tarzeaaaaaaaaaaaaaaen, you Jane"
text_2 = "I like diamonds!!!"

ratio_text1 = char_count(text_1)
ratio_text2 = char_count(text_2)

print(ratio_text1)
print(ratio_text2)

if ratio_text1 > ratio_text2:
    print("text_2 Most likely female.")
elif ratio_text2 == ratio_text1:
    print("I cannot decide.")
else:
    print("text_1 is most likely female." )