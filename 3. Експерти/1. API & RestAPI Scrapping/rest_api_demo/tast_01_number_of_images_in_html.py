import requests

TARGET_URL = "http://dir.bg"
IMAGE_TAG = "<img "

response = requests.get(TARGET_URL)
response_text = response.text
# print(response_text)

if IMAGE_TAG in response_text:
    print("Има картинки")

image_count = 0
found_index = 0

while found_index != -1:
    found_index = response_text.find(IMAGE_TAG, found_index)
    if found_index != -1:
        image_count += 1
        found_index += 1


print("{} images found on page {}".format(image_count, TARGET_URL))
