name = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a"

alfabet={"a":1,"e":2, "i":3, "o":4, "u":5}
name_split = list(name)
print(name_split)

counter = 0

for n in name_split:
    if not alfabet.get(n): continue
    counter = counter + (int(alfabet.get(n)))

# sum = 0
#
# for number in numbers:
#     sum = sum+number

print("Сумата от гласните в думата е " + str(counter))

