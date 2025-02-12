# GNUploter util for kolkata data
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ketan
#
# Created:     12-02-2025
# Copyright:   (c) ketan 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
from tkinter import filedialog
from tkinter import Tk

def list_files_with_extension(folder_path):
    # List all files in the selected folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files

# Create a GUI window
root = Tk()
root.withdraw()  # Hide the main window

# Open a dialog box and ask the user to select a folder
folder_selected = filedialog.askdirectory()

# Get the list of files with their extensions
files_list = list_files_with_extension(folder_selected)

# Print the list of files
print(f"cd '{folder_selected}'")
print(f"plot ",end='')
for file in files_list:
    #plot 'SEFO_KNO_TScan_207_Hz_-0.0_T.dat'using 2:5
   #

    print(f"'{file}' u 2:5,", end='')

# Close the GUI window
root.destroy()
