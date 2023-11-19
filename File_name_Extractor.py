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
