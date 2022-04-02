from collections import defaultdict

with open("catagories.csv") as file_handler:
    header_line = next(file_handler)
    split_header_line = header_line.split(',')
    headers = []
    headers_size = len(split_header_line)
    for header in split_header_line:
        headers.append(header.strip().strip('\"'))

    category_dict = defaultdict(list)

    for line in file_handler:
        split_line = line.split(',')
        for count, category in enumerate(split_line):
            category_dict[headers[count]].append(category.strip("\"").strip())

print(category_dict)
