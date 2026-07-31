# Batch File Renamer

A Python tool that batch renames files in a folder using a user-defined prefix and sequential numbering.

This project was built as part of my Survey Automation Toolkit portfolio to automate repetitive file management tasks commonly encountered in surveying, GIS, drone mapping and photogrammetry workflows.

## Features

- Rename all files in a folder
- User-defined filename prefix
- Automatic sequential numbering (001, 002, 003...)
- Preserves original file extensions
- Simple command-line interface

## Example

### Before

```
IMG_0345.JPG
IMG_0346.JPG
IMG_0347.JPG
```

### Input

```
Prefix: Maastricht
```

### After

```
Maastricht_001.JPG
Maastricht_002.JPG
Maastricht_003.JPG
```

## Skills Demonstrated

- Python
- File and folder handling
- pathlib
- Loops
- Functions
- User input
- String formatting
- Automation

## Future Improvements

- Sort files by capture date
- Preview changes before renaming
- Ignore non-image files
- Rename recursively through subfolders
- Graphical user interface (GUI)
- Drag-and-drop folder support

## Repository Structure

```
Batch-File-Renamer/
├── batch_file_renamer.py
├── README.md
└── sample_files/
```

## Author

**Ezra Miller**

Bachelor of Engineering (Honours) (Surveying)  
Bachelor of Commerce (Business Analytics)

GitHub: https://github.com/itsEzraMiller