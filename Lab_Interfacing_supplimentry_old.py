import pandas as pd

import numpy

import os

import re

import matplotlib.pyplot as plt


I_range = float(input("Enter value of I: "))
I_div = int(input("Enter division: "))
filename = input("Enter filename: ")

#-------------------------------------
#I=np.linspace(-I_range, I_range,I_div) #dummy
#V=np.linspace(0,0,I_div) #dummy 
I=np.linspace(-I_range,I_range,I_div) #dummy
V=np.linspace(0,0,I_div) #dummy 


#--------------------------------

plt.plot(I, V, marker='o', linestyle='-', color='g', 
label='Square') 
plt.xlabel('I')
plt.ylabel('V') 
plt.title('IV curve')
plt.legend('') 
plt.show()

#---------------------------

#df_I = pd.DataFrame(I)
#df_V = pd.DataFrame(V)

df=pd.DataFrame()

df['I']=pd.DataFrame(I)
df['V']=pd.DataFrame(V)
df.to_csv(r'C:/Users/ketan/OneDrive/Desktop/IV_files/IV_data_at_RT_'+str(filename), index=None, sep='	', mode='w')

