"""
GUI-Based CSV File Selector Utility.

This script defines a reusable function, `select_file()`, that opens a
graphical file dialog window for the user. The dialog is specifically
configured to filter for and display only files with the '.csv' extension,
guiding the user to select the correct file type.

Upon selection, the function returns the full, absolute path of the chosen file
as a string. The selected path is also printed to the console for immediate
user feedback.

This utility is designed to be easily integrated into larger data analysis
workflows, allowing for interactive file input without needing to hardcode
file paths.
"""


import os
import tkinter
from tkinter import filedialog

def select_file():
    # Initialize tkinter window
    root = tkinter.Tk()
    root.withdraw()
    root.update()
    root.deiconify()
    root.focus_set()

    # Search for file path
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(
        parent=root, initialdir=currdir, title='Please select a CSV file',
        filetypes=[("CSV files", "*.csv")]
    )

    # Close the tkinter window
    root.destroy()

    # Print the selected file path
    if tempdir:
        print("File selected is: %s" % tempdir)
    return tempdir


# Call the function to select the file
selected_file = str(select_file())

# Print the selected file path
print(f"Selected file: {selected_file}")
