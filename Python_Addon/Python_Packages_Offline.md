
# Python Offline Package Installation 

---

## Part 1: On the Computer WITH Internet

First, you'll download the necessary package files onto a machine that is connected to the internet.

1.  **Create a Directory:** Make a new folder to hold the packages.
2.  **Download Packages:** Open the Command Prompt (CMD) and run the following command:
    ```bash
    pip download package_name -d "directory_path"
    ```
    * This will save the Python package files (as `.whl` and `.tar` files) into the directory you specified.

---

## Part 2: On the Computer WITHOUT Internet

Next, you'll transfer and install the files on the offline machine.

1.  **Copy Packages:** Copy the folder containing the downloaded packages to the system without internet access.
2.  **Navigate to Directory:** On the offline machine, open CMD and navigate to the folder containing your packages:
    ```bash
    cd directory_path
    ```
3.  **Install Packages:** Run the installation command for each file. You will need to do this for each `.whl` file and then for the `.tar` file.
    ```bash
    pip install pythonpackage -f ./ --no-index --no-deps
    ```
    * Replace `pythonpackage` with the **complete filename** of the package, including the `.whl` or `.tar` extension.
    * **Note:** If you get an error with a `.tar` file, check if the extension is `.tar` or `.tar.gz` and use the correct one in the command.
  
      Source: https://youtu.be/RadXs2Atw7E
    

    Example:

    ```bash
    pip download matplotlib pandas scipy numpy lakeshore pyvisa visa PyMeasure PyVISA-py -d "F:\Python_Packages_2025"
    ```
