"""
Local Python Package Installer Command Generator.

This script provides a graphical user interface (GUI) for a user to select a
folder containing local Python package files (e.g., .whl, .tar.gz).

After a folder is selected, the script scans it for all files and generates a
series of `pip install` commands. Each command is specifically formatted for
offline installation, telling pip to look in the current directory for the
package and to not search the online Python Package Index (PyPI) or install
dependencies.

The resulting commands are printed to the console, ready to be copied and
pasted into a terminal to install all packages from the selected folder.
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
print("Files in the selected folder:",folder_selected)
for file in files_list:
    #pip install pythonpackage -f ./ -- no-index -- no-deps
    print(f"pip install {folder_selected}/{file} -f ./ --no-index --no-deps")

# Close the GUI window
root.destroy()
