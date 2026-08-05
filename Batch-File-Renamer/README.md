# Batch File Renamer

A simple Python utility for renaming large batches of photos and videos using consistent sequential filenames.

I built this project as a practical introduction to Python automation, file handling, and packaging Python programs into standalone Windows applications.

## What it does

The Batch File Renamer:

- Lets the user choose any folder using a Windows folder browser
- Finds supported photo and video files
- Ignores hidden files
- Sorts files consistently before renaming
- Lets the user choose a filename prefix
- Shows a preview before making changes
- Checks whether destination filenames already exist
- Renames files sequentially
- Shows progress while renaming
- Reports how many files were successfully renamed

### Supported file types

- `.jpg`
- `.jpeg`
- `.png`
- `.mp4`

## Example

Before:

    IMG_0001.JPG
    IMG_0002.JPG
    GX010001.MP4
    GX010002.MP4

The user enters:

    GoPro

The files become:

    GoPro_001.JPG
    GoPro_002.JPG
    GoPro_003.MP4
    GoPro_004.MP4

The original file extensions are preserved.

## How to use

### Option 1 — Windows executable

Download or run:

    batch_file_renamer.exe

No Python installation is required.

1. Open the program.
2. Select the folder containing your photos/videos.
3. Enter a filename prefix.
4. Review the proposed changes.
5. Enter `y` or `yes` to confirm.
6. The files will be renamed in their original folder.

### Option 2 — Run the Python source code

Python is required.

Run:

    python batch_file_renamer.py

## Safety features

The program does not upload files or connect to the internet.

Before renaming, it:

- Shows a preview of the changes.
- Checks for existing destination filenames.
- Requires confirmation from the user.

The program only renames files. It does not move them to another folder.

## Project structure

    Batch-File-Renamer/
    ├── batch_file_renamer.py
    ├── README.md
    ├── .gitignore
    └── sample_files/
        └── .gitkeep

## Python concepts demonstrated

This project uses:

- `pathlib`
- File and folder handling
- List comprehensions
- Filtering files by extension
- Sorting
- `for` loops
- `enumerate()`
- String formatting
- User input
- Conditional statements
- Error checking
- `tkinter` folder selection
- File renaming
- Basic program safety checks

## Why I built it

This project was created as a practical automation tool for working with large numbers of photos and videos.

It was also designed to develop Python skills relevant to GIS, surveying and data automation.

## Screenshots

### Selecting a folder

![Folder selection](screenshots/folder-selection.png)

### Previewing changes

![Rename preview](screenshots/preview.png)