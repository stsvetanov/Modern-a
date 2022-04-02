import os

# for dirpath, dirnames, filenames in os.walk('./'):
#     print("Current Directory: ", dirpath)
#     print("Directories", dirnames)
#     print("Files", filenames)
#     print("\n-------------\n\n")

# print('Argument List:', str(sys.argv))


def get_all_abs_filenames_recursive(start_directory: str) -> list:
    result = []

    # start_directory = os.path.abspath(start_directory)
    # if not start_directory.endswith('/'):
    #     start_directory += '/'

    for dirpath, _, filenames in os.walk(start_directory):
        for fn in filenames:
            result.append(dirpath+ fn)
            # result.append(fn)
    return result


all_abs_filenames = get_all_abs_filenames_recursive('D:\eBooks')
# all_abs_filenames = get_all_abs_filenames_recursive('./')

print(all_abs_filenames)



