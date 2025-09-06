"""
Generates a Sample Dataset and Writes it to a Text File.

This script demonstrates basic file I/O operations in Python. It creates a new
file with a name prefixed by "temporary_data_" and proceeds to populate it
with a structured, two-column dataset.

The generated data follows a simple quadratic relationship (y = x^2), where the
first column represents an integer current from 0 to 19, and the second column
represents the corresponding squared voltage.

The output file is tab-separated and includes a main title, column headers,
and section markers ('loop1', 'loop2') to showcase how to structure a data log.
"""


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

