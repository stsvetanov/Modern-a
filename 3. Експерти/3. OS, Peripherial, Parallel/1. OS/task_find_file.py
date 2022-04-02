import os
import sys


def find_file(start_directory: str, filename: str) -> str:
    result = []

    for dirpath, _, filenames in os.walk(start_directory):
        if filename in filenames:
            result.append(os.path.join(dirpath, filename))

    return result


if len(sys.argv) >= 3:
    filename_to_search_for = sys.argv[1]
    dir_to_search = sys.argv[2]
    found_filename = find_file(dir_to_search, filename_to_search_for)
    if found_filename:
        print("Full path to file: ", found_filename)
    else:
        print("File not found")
else:
    print("Please provide a filename as a first parameter and directory as second")