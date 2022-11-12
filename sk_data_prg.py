import pandas as pd

import numpy

import os

import re



directory = 'C:/Users/ketan/OneDrive/Desktop/10.07.2015_5T'

 

for filename in os.scandir(directory):



    if filename.is_file():

        df=pd.read_table(filename, delimiter=r"\s+", skiprows=3)
        

        df1=df[['#Freq', 'Cp', 'G', 'E1', 'E2', 'Z1', 'Z2', 'M1', 'M2', 'tand']].copy()

        df1.to_csv(r'C:/Users/ketan/OneDrive/Desktop/10.07.2015_5T\Cal_data2\mod_'+str(filename.name), index=None, sep='	', mode='w')
