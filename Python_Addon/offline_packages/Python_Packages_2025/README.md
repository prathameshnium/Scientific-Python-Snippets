# Offline Python Packages for Scientific Computing Sep-2025

## About This Directory

This directory contains a comprehensive collection of Python packages and their dependencies, designed for setting up a full scientific and instrument control environment on a computer **without an internet connection**.

The collection is stored as a **multi-part ZIP archive**. You must download all parts (total 4.) and extract and install the packages.

---

## Packages Included 

This archive includes a wide range of essential libraries. The key packages are:
### what I downloaded pandas scipy numpy lakeshore pyvisa visa PyMeasure PyVISA-py 

* **pandas**: 
* **scipy**: 
* **numpy**: 
* **lakeshore**: 
* **pyvisa**: 
* **visa**: 
* **PyMeasure**: 
* **PyVISA-py**: 
#### Total list that got downloaded
   ```bash
matplotlib pandas scipy numpy lakeshore pyvisa visa PyMeasure PyVISA-py contourpy cycler fonttools kiwisolver packaging pillow pyparsing pyqtgraph pyserial python-dateutil pytz requests charset_normalizer idna urllib3 certifi six typing_extensions tzdata wakepy iso8601 pint flexcache flexparser platformdirs
  ```

---

### Step 2: Install the Packages Offline

After joining and extracting the files, you will have a folder full of `.whl` and `.tar.gz` package files.

1.  Open a Command Prompt or Terminal on the offline machine.
2.  Navigate into the folder containing the extracted package files.
    ```bash
    cd path/to/your/extracted_packages_folder
    ```
3.  Install the packages using `pip`, telling it to look only in the current folder:
    ```bash
    pip install pythonpackage -f ./ --no-index --no-deps
    ```
    * You may need to install certain packages (like NumPy) before others. It's often best to install the packages one by one, starting with the core dependencies.
