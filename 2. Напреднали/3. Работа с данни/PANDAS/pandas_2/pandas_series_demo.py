# Program to create series
# a = pd.Series(Data)
# # Hire data can be: Value, Dictionary, NdArray (N-dimensional array)
import pandas as pd  # Import Panda Library
#
#  # # Program to Create series with scalar values
# Data = [1, 3, 4, 5, 6, 2, 15]  # Numeric data
# #
# # Creating series with default index values
# s = pd.Series(Data)
# print(s)
# #
# # predefined index values
# Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#
# # Creating series with predefined index values
# si = pd.Series(Data, Index)
# print(si)
#
# Program to Create Dictionary series
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Creating series of Dictionary type
sd = pd.Series(dictionary)
print(sd)

# Program to Create ndarray series
Data = [[2, 3, 4], [5, 6, 7], [5, 9, 7]]  # Defining 2darray

# Creating series of 2darray
snd = pd.Series(Data)
print(snd)
