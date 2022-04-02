buffer = []

file_handler = open("./mbox-short.txt", "r", encoding="utf-8")

for line in file_handler:
    if line == '\n':
        continue
    else:
        buffer.append(line)

file_handler.close()

file_handler = open("strip_mbox-short.txt", "w", encoding="utf-8")

for line in buffer:
    file_handler.write(line)

file_handler.close()
