'''
# simple script that converts a txt file to csv

Dependencies:
python3, python pandas package

if pandas is not installed, use:
>> pip install pandas

This script runs through the same directory as the txt  files for conversion

If the script is in a different directory, you need to define the path of the txt files
i.e.:
root_dir = 'path/to_the/txt/files',

and add the path when loading the data

'''

import pandas as pd

#load the txt file:
read_txt = pd.read_csv('./your_txt_file_goes_here.txt') # the files are in the same directory with the script

# save file to csv:
read_txt.to_csv('./your_csv_file_goes_here.csv', index=None)
