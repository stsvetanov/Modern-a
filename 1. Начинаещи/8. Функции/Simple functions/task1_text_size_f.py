def text_size(text):
    if len(text) < 8:
        print(text)
    else:
        text = text[:10]
        print(text + '...')


user_input = input("Enter some text: ")
text_size(user_input)


