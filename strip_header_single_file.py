"""
Removes the Header from a Single Data File.

This script performs a simple file cleaning operation. It reads a specified
input file ('mod_10K.txt'), discards the first two lines which are assumed to be
a header, and then writes all of the remaining content into a new output file
('mod_10K_new.txt').

This is a non-destructive operation, as the original file is left unchanged.
The script is useful for preparing individual data files for analysis or
import where the header information is not needed.

NOTE: The input and output filenames are hardcoded. To use this script on
different files, the user must modify the filename strings directly in the code.
"""

with open('mod_10K.txt','r') as f:
    f.readline()
    f.readline()
    f_content=f.read()
#print(f_content)


with open('mod_10K_new.txt','w') as f1:
    f1.write(f_content)

