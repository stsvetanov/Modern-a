paragraph = []
while True:
    new_sentence = input("Enter a sentence: ")
    if new_sentence == "":
        break
    else:
        first_letter = new_sentence[0].capitalize()
        paragraph.append(first_letter + new_sentence[1:])

print("You wrote: " + " ".join(paragraph))