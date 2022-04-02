import os


def find_file(start_directory: str, file_name_to_find: str) -> list:
    for dirpath, _, file_names in os.walk(start_directory):
        for fn in file_names:
            if fn == file_name_to_find:
                return dirpath+fn

    return -1


print(find_file('D:\eBooks', 'Clean_Code.pdf'))




