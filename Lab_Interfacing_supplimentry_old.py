import pandas as pd

import numpy as np

import os

import re

import matplotlib.pyplot as plt


I_range = float(input("Enter value of I: "))
I_step= float(input("Enter steps: "))
filename = input("Enter filename: ")





#-------------------------------------
Volt=[]
#I=np.linspace(-I_range, I_range,I_div) #dummy
#V=np.linspace(0,0,I_div) #dummy 
#I=np.linspace(-I_range,I_range,I_div) #dummy
#V=np.linspace(0,0,I_div) #dummy 
I=np.arange(-I_range,I_range,I_step)
#V=np.arange(-I_range,I_range,I_step)
dummy_step=int((2*I_range)/I_step)
#V=np.linspace(0,10,num=dummy_step)
V=np.linspace(0,10,num=dummy_step)


#V=np.arange(0,0,dummy_step)
#print(I)




for ind in np.arange(-I_range,I_range,I_step):
    Volt.append(ind*100)
    


#V1 = np.array(V)
#print(I_step)
#print(dummy_step)

#--------------------------------


print(res)
#--------------------------------

plt.plot(I, Volt, marker='o', linestyle='-', color='g', label='Square') 
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
