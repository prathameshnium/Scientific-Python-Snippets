"""
GUI-Based File Path Lister.

This script provides a simple graphical user interface (GUI) for a user to
select a directory from their file system. Once a directory is chosen, the
script recursively scans it and all of its subdirectories.

The full, absolute path of every file found during the scan is then printed
to the console, one file per line. This is useful for generating file lists
for reports, batch processing, or system audits.

This script has no file output; its sole output is to the standard console.
"""

import os
import tkinter as tk
from tkinter import filedialog

# Create a dialog box to select the folder
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

# Extract the file names with all path for all files in the folder
file_names = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_names.append(os.path.join(root, file))

for i in range(len(file_names)):
    print(file_names[i])
