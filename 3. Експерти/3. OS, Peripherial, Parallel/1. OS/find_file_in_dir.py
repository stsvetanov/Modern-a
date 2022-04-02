import os
# file_name_to_find = "Alice_in_Wonderland.pdf"
import sys


def find_file(file_name_to_find, dir_to_search):
    for path, _, files in os.walk("D:\eBooks"):
        for fn in files:
            if fn == file_name_to_find:
                return path + fn

    return None


file_name_to_find = sys.argv[1]
dir_to_search = sys.argv[2]
print(find_file(file_name_to_find, dir_to_search))
