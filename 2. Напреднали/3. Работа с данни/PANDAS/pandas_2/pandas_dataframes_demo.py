# Program to create DataFrame
# a = pd.DataFrame(Data)
# Hire data can be: Dictionary, Series, 2D-numpy Ndarray
import pandas as pd  # Import Panda Library
#
# # Program to Create Data Frame with two dictionaries
# dict1 ={'a': 1, 'b': 2, 'c': 3, 'd': 4}        # Define Dictionary 1
# dict2 ={'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9} # Define Dictionary 2
# Data = {'first': dict1, 'second': dict2}  # Define Data with dict1 and dict2
# df = pd.DataFrame(Data)  # Create DataFrame
#
# print(df)
# df["second"].hist()

# # Program to create Dataframe of three series
# import pandas as pd
#
# s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])  # Define series 1
# s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  # Define series 2
# s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])  # Define series 3
#
# Data = {'first': s1, 'second': s2, 'third': s3}  # Define Data
# dfseries = pd.DataFrame(Data)  # Create DataFrame
# print(dfseries)
# print(dfseries["third"])

#Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print(df)

# select two columns
# print(df[['Name', 'Qualification']])

#
# # Program to create DataFrame from 2D array
# d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
# d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2
# Data ={'first': d1, 'second': d2} # Define Data
# df2d = pd.DataFrame(Data)    # Create DataFrame
# print(df2d)

