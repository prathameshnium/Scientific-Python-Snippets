Scientific-Python-Snippets
(formaly mini-tests)

A curated collection of small, reusable Python scripts for common data handling, file manipulation, and automation tasks. This repository serves as a personal library of snippets and utilities, often incorporating simple graphical user interfaces (GUIs) with Tkinter for ease of use.

 Table of Contents
Features

Dependencies

Script Descriptions

Usage

 Features
This toolkit provides scripts to perform a variety of common tasks, including:

GUI Interaction: File and folder selection dialogs using Tkinter.

Data Parsing: Reading and cleaning data from structured text and CSV files.

Batch Processing: Applying an operation (like stripping headers) to all files in a directory.

Data Generation: Creating sample datasets for testing and simulation.

Command Generation: Automating the creation of shell commands for programs like gnuplot and pip.

Interactive Plotting: Selecting and annotating data points directly on a matplotlib graph.

 Dependencies
The scripts in this repository primarily rely on the following standard Python libraries. To run all scripts, ensure you have them installed:

pip install pandas numpy matplotlib

Note: tkinter is part of the standard Python library and typically does not require a separate installation.

 Script Descriptions
Here is a brief overview of each script included in this toolkit:

Filename

Description

csv_file_picker.py

Opens a GUI dialog to select a single .csv file and returns its absolute path.

generate_gnuplot_script.py

Asks the user for a folder and generates a gnuplot command to plot data from all files within it.

generate_local_pip_commands.py

Asks the user for a folder and generates offline pip install commands for all package files found.

generate_squared_data.py

Creates a sample two-column dataset (y = x²) and saves it to a structured text file.

gui_file_lister.py

Opens a GUI dialog to select a folder and prints the full path of every file within it recursively.

interactive_data_picker.py

Displays an interactive matplotlib plot where users can click to select and annotate data points.

lcr_data_parser.py

A batch processor that extracts specific columns of data from LCR meter files in a directory.

numpy_range_examples.py

A reference script demonstrating different methods to generate numerical sequences with NumPy.

strip_file_headers.py

(Destructive) Removes the first two lines from every file in a specified directory.

strip_header_single_file.py

Removes the first two lines from a specific file and saves the result to a new file.

timestamped_filename_generator.py

Runs an infinite loop that continuously prints unique, timestamped filenames to the console.

