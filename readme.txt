# File System Analyzer

## Overview
The File System Analyzer is a command-line tool developed in Python that analyzes and reports on the file system structure and usage on a Linux system. This tool provides insights into the types of files present in a directory, their sizes, permissions, and identifies files that may require attention.

## Features
- Directory Traversal: Traverse through a specified directory and its subdirectories recursively.
- File Type Categorization: Classify files into categories based on their extensions and file signatures.
- Size Analysis: Calculate and display the total size for each file type category.
- File Permissions Report: Generate a report of files with unusual permission settings.
- Large Files Identification: Identify and list files above a certain size threshold.
- User Interface: Simple command-line interface to specify the directory to be analyzed and set parameters.
- Error Handling: Robust error handling for scenarios like inaccessible directories.
- Testing: Comprehensive unit tests to ensure the correctness of the tool's functionalities.
- Random File and Folder Generation: Utility script to generate random files and folders for testing purposes.

## Requirements
- Python 3.x
- Additional Python libraries: [python-magic] (for file signature analysis)

## Usage
1. Clone this repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the tool with the desired directory path and optional parameters:
```
python file_system_analyzer.py <directory_path> [--large-file-threshold <threshold>]
```
- `<directory_path>`: Path to the directory to be analyzed.
- `--large-file-threshold <threshold>`: (Optional) Threshold size for identifying large files (in bytes).

## Example
```
python file_system_analyzer.py /path/to/directory --large-file-threshold 1000000
```

## Notes
- Ensure that you have appropriate permissions to access the specified directory and its contents.
- The tool may take some time to analyze large directories, depending on the size and complexity of the file system.
- With every run check the `permissions_report.txt` file to see the files with unusual permission settings (don't forget to clear the `permissions_report.txt` file with every use).

## Author
Louay ALAMI OUAHABI
louay.alami.ouahabi@gmail.com