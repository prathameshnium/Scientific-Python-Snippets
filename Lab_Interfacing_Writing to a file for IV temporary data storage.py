filename='ABCD'
filename_new="temporary_data_"+str(filename)+'.txt'

file1 = open(filename_new, "w")


# Append-adds at last
file1 = open(filename_new, "a") # append mode
file1.write("temporary data of "+str(filename)+"\ncurrent\tvoltage\n")
l1=[]
l2=[]

file1 = open(filename_new, "a")
file1.write('loop1\n')
for i in range(20):
    l1.append(i)
    l2.append(i*i)
    file1.write(str(l1[i])+"\t"+str(l2[i]))
    file1.write('\n')

file1.write('loop2\n')

file1.close()

