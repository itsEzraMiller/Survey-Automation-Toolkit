from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# Hide the empty tkinter window
root = tk.Tk()
root.withdraw()

# Ask the user to choose a folder
folder_path = filedialog.askdirectory(
    title="Select the folder containing your photos"
)

# Convert the chosen folder into a Path object
folder = Path(folder_path)

if not folder_path:
    print("\nNo folder selected.")
    quit()

# Check that the folder exists
if not folder.exists() or not folder.is_dir():
    print("\nError: Folder not found.")
    quit()

# Get every file, ignoring hidden files
allowed_extensions = [".jpg", ".jpeg", ".png", ".mp4"]

files = sorted(
    [
        file
        for file in folder.iterdir()
        if file.is_file()
        and not file.name.startswith(".")
        and file.suffix.lower() in allowed_extensions
    ]
)

print(f"\nFound {len(files)} files.\n")

if len(files) == 0:
    print("No files found.")
    quit()

# Ask for filename prefix
prefix = input("Enter filename prefix: ").strip()

print("\nPreview:\n")

new_paths = []

for i, file in enumerate(files, start=1):

    extension = file.suffix
    new_name = f"{prefix}_{i:03}{extension}"
    new_path = folder / new_name

    # Check if destination already exists
    if new_path.exists():
        print(f"ERROR: {new_name} already exists.")
        quit()

    new_paths.append((file, new_path))

    print(f"{file.name}  →  {new_name}")

confirm = input("\nRename these files? (y/n): ")

if confirm.lower() not in ["y", "yes"]:
    print("\nCancelled.")
    quit()

# Rename everything
for old_file, new_file in new_paths:
    old_file.rename(new_file)

print("\nDone!")