with open('mod_10K.txt','r') as f:
    f.readline()
    f.readline()
    f_content=f.read()
#print(f_content)


with open('mod_10K_new.txt','w') as f1:
    f1.write(f_content)

#---------------------------------------------------------------------------------------
