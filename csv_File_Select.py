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
