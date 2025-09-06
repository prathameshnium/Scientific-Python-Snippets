"""
Batch File Header Stripper.

This script performs an in-place modification of all files located within a
specified directory ('raw_data'). It iterates through each file, reads its
contents while skipping the first two lines, and then overwrites the original
file with the remaining content.

This is primarily used for preprocessing raw data files to remove fixed-size
headers before further analysis or import into other programs.

**WARNING:** This is a destructive operation. It permanently modifies the files
in the target directory. It is highly recommended to back up the original
data before running this script.
"""

import pandas as pd

import numpy

import os

import re



directory = 'raw_data'

 

for filename in os.scandir(directory):



    if filename.is_file():
        with open(filename,'r') as f:
            f.readline()
            f.readline()
            f_content=f.read()
        with open(filename,'w') as f1:
            f1.write(f_content)
           
