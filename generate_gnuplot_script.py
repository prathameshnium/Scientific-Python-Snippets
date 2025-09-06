# GNUploter util for kolkata data

"""
Gnuplot Plotting Command Generator.

This script provides a graphical user interface (GUI) for a user to select a
folder containing scientific data files.

After a folder is selected, the script scans it for all files and automatically
constructs a complete gnuplot command. The generated command is designed to
plot column 5 versus column 2 ('using 2:5') for every file in the directory,
overlaying them all onto a single graph.

The final command is printed to the console, ready to be copied and pasted
directly into a gnuplot terminal for execution, saving significant time when
visualizing large batches of data.
"""

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
