"""
Batch Parser for LCR Meter Data Files.

This script iterates through all files in a specified directory, reads each file
assuming it is a space-delimited data file from an LCR meter or impedance
analyzer, and extracts key measurement columns.

The script is configured to:
  - Skip the first 3 header lines of each data file.
  - Extract the following columns: '#Freq', 'Cp', 'G', 'E1', 'E2', 'Z1', 'Z2',
    'M1', 'M2', and 'tand'.

NOTE: The user must update the 'directory' variable to point to the location
of their data files before running.
"""


import pandas as pd

import numpy

import os

import re



directory = 'C:/Path'

 

for filename in os.scandir(directory):



    if filename.is_file():

        df=pd.read_table(filename, delimiter=r"\s+", skiprows=3)
        

        df1=df[['#Freq', 'Cp', 'G', 'E1', 'E2', 'Z1', 'Z2', 'M1', 'M2', 'tand']].copy()

