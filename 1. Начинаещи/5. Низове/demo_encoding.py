import base64

info_read_from_a_file = b'\xd0\x90! \xd0\x9a\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0, \xd0\xba\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0 \xd0\xb2 UTF-8 :\xd0\xbe)'
print(info_read_from_a_file)
print(info_read_from_a_file.decode())

info_to_be_written_out = 'Да видим това дали ще можем да го прочетем после?'.encode('utf-8')
print(info_to_be_written_out)
print(info_to_be_written_out.decode())

output = "Hi, my name is .."
decoded_output = output.encode()
print(decoded_output)

output = "Здрасти! Моето име е ..."
decoded_output = output.encode()
print(decoded_output)

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

print(chr(65))

# encoded_string= base64.b64encode(img_file.read())
# print(encoded_string.decode('utf-8'))
