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
print("Files in the selected folder:")
for file in files_list:
    #pip install pythonpackage -f ./ -- no-index -- no-deps
    print(f"pip install {file} -f ./ --no-index --no-deps")

# Close the GUI window
root.destroy()
