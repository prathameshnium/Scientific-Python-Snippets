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
           
