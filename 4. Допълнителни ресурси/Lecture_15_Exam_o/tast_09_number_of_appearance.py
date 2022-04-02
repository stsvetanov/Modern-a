# import requests
#
# str = "Имало едно време едно .."
# print(str.find("едно"))
#
# TARGET_URL = "http://dir.bg"
# IMAGE_TAG = "<img "
#
# response = requests.get(TARGET_URL)
# response_text = response.text
#
# if IMAGE_TAG in response_text:
#     print("Има картинки")
#
# image_count = 0
# found_index = 0
#
# while found_index != -1:
#     found_index = response_text.find(IMAGE_TAG, found_index)
#     if found_index != -1:
#         image_count += 1
#         found_index += 1
#
# #  Алтернативно решение
# # print(textfind.count(word))
#
#
# print("{} images found on page {}".format(image_count, TARGET_URL))


# text = 'Имало едно време едно ...'
text = 'Ималоедновремеедно...Ималоедновремеедно'
n = 0
pattern = 'едно'
searcher = text.split()
for word in searcher:
    if word == pattern:
        n += 1
print('Думата се съдържа',n,'в текста')
