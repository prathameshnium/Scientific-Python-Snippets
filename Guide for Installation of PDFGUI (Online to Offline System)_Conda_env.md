# Guide for Installation of PDFGUI (Online to Offline System)

This guide outlines the process for installing `diffpy.pdfgui` on a system with an internet connection, packing the environment, and transferring it to an offline system for use.

-----

## Part 1: Online System Setup

### 1\. Initial Setup

First, open the Anaconda Prompt. You will need to add the `conda-forge` channel to your Conda configuration.

```bash
conda config --add channels conda-forge
```

### 2\. Create and Activate the Virtual Environment

This command will create a new, dedicated virtual environment named `diffpy.pdfgui_env` and install the `diffpy.pdfgui` package into it.

```bash
conda create -n diffpy.pdfgui_env diffpy.pdfgui
```

When prompted, press `y` to proceed with the installation.

Once the installation is complete, you must activate the new environment.

```bash
conda activate diffpy.pdfgui_env
```

-----

## Part 2: Exporting the Environment for Offline Use

### 1\. Install Conda-Pack

To package the environment for offline use, you first need to install `conda-pack`.

```bash
conda install -c conda-forge conda-pack
```

### 2\. Pack the Environment

Run the following command to package your `diffpy.pdfgui_env`. This creates a file named `pdfgui_env.tar.gz` in the specified output directory.

**Note:** You will need to replace `D:\pdfgui_Folder\` with your desired output path.

```bash
conda pack -n diffpy.pdfgui_env -o D:\pdfgui_Folder\pdfgui_env.tar.gz -ignore-editable-packages
```

After the command finishes, move the generated `.tar.gz` file to the offline system.

-----

## Part 3: Offline System Setup

### 1\. Prerequisites

The offline system **must have Anaconda installed**.

### 2\. Create Directory and Extract

First, create a new directory for the environment within your Anaconda installation's `envs` folder.

  * **Important**: Replace `"C:\path\to\anaconda3"` with the actual path to your Anaconda installation on the offline machine.

<!-- end list -->

```bash
mkdir C:\path\to\anaconda3\envs\diffpy.pdfgui_env
```

Next, extract the packed file into the newly created directory.

  * **Important**: Use the actual file paths for both the source `.tar.gz` file and the destination directory on your offline machine.

<!-- end list -->

```bash
tar -xzf D:\pdfgui_Folder\pdfgui_env.tar.gz -C C:\path\to\anaconda3\envs\diffpy.pdfgui_env
```

### 3\. Activate and Clean Up

Activate the environment by specifying its full path.

```bash
conda activate C:\path\to\anaconda3\envs\diffpy.pdfgui_env
```

After activating, run the `conda-unpack` command to clean up paths and make the environment fully functional.

```bash
conda-unpack
```

-----

## Part 4: Run PDFGUI

With the environment still activated from the previous step, you can now run the application for the first time.

```bash
pdfgui
```

-----

## Running PDFGUI in a New Session

After the initial installation, every time you want to use the program in a new terminal session, you will need to open the Anaconda Prompt and run two commands.

1.  **Activate the environment** (remember to use your actual Anaconda path):

    ```bash
    conda activate C:\path\to\anaconda3\envs\diffpy.pdfgui_env
    ```

2.  **Run PDFGUI**:

    ```bash
    pdfgui
    ```

### Note on Other Offline Projects

This process is not just for PDFGUI. The general method of using **`conda-pack`** to create an archive, moving it to an offline machine, extracting it into the `envs` folder, and activating it by its full path is a standard procedure that works for almost any other project you need to transfer using a Conda environment.
