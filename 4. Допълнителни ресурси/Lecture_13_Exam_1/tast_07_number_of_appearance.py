
text = 'Ималоедновремеедно...Ималоедновремеедно'
count = 0
pattern = 'едно'
# searcher = text.split()
# for word in searcher:
#     if word == pattern:
#         count += 1

index = 0
while index != -1:
    index = text.find(pattern, index)
    if index != -1:
        count += 1
        index += 1

print(f'Думата {pattern} се съдържа {count} пъти в текста')


