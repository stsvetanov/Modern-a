








# /working_directory
#         utils_module.py
#                 def print_with_indent(what: str)
#                     ...
#
#         program.py
#
# import utils_module
# from utils_module import print_with_indent
# from utils_module import print_with_indent as some_fancy_name
# from utils_module import *    # не е добра практика

# from utils import convert_fahrenheit_to_celsius
# from utils import TEMP_WATER_FREEZING_F
#
# print("Program")
#
# deg_c = convert_fahrenheit_to_celsius(32)
# print("C: ", deg_c)
# print("Water freezes at {} deg F".format(TEMP_WATER_FREEZING_F))
#
# # =======================================
#
# import utils
#
# deg_c = utils.convert_fahrenheit_to_celsius(32)
# print("C: ", deg_c)
# print("Water freezes at {} deg F".format(utils.TEMP_WATER_FREEZING_F))