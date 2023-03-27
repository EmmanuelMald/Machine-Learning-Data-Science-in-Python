"""
CLASS 1. What a dataset is?

A dataset is a file where you have a table with data.
 It has tags for columns and rows
 
       Columns has names and rows has index. Also index can be changed for names or letters.

It works with csv, xlsx, txt, and others.

How to upload data?

All files are separated by a special character called "separator", usually is a comma.

pandas is the library that is used to open, import and change datasets.
"""
import pandas as pd

"""
A csv can be open from different ways, the first one is to put an 'r' before the complete route file
r=raw

"""

data=pd.read_csv(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\GITHUB\Machine-Learning-Data-Science-Python\Machine-Learning-Data-Science-in-Python\Cleaning Data\titanic3.csv")


# Second way is writting double \

data1=pd.read_csv("C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\GITHUB\\Machine-Learning-Data-Science-Python\\Machine-Learning-Data-Science-in-Python\\Cleaning Data\\titanic3.csv")

print(data.head()) #Shows the first five rows of the file

# What if the separator is not a coma? The parameters of pd.read_csv are shown below
"""
pd.read_csv(filepath, separator, dtype, header, names, skiprows,index_col, skip_blank_lines)
            
            filepath= dataset location
            
            separador= It can be any character, is written into simple quotation marks and accepts regular expressions
            
            dtype= default is None, but it can be changed to datetime if used or another data type
            
            header=None, Can be an integer or list. header use the first row as name columns of the dataframe, 
            header = 0 is the first row
            
            names= You can add a column names list
            
            skiprows=None (default), allow us not reading a column
            if we write skiprows=12, it will read columns since the column 12
            
            index_col=None (default), allow us to write the rows names of a dataset
            
            skip_blank_lines=True or False (if True: blank lines will be omitted)

            na_filter=True or False ( if True, delete rows with any none value)
            
"""

