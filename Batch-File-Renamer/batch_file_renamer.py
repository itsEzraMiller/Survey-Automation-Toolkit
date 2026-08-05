import sys
import re
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# -----------------------------
# Welcome message
# -----------------------------

print("=" * 45)
print("          BATCH FILE RENAMER")
print("=" * 45)

print("\nThis tool renames photos and videos")
print("using a prefix and sequential numbering.")
print("Your files stay in their original folder.\n")


# -----------------------------
# Choose a folder
# -----------------------------

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(
    title="Select the folder containing your photos/videos"
)

if not folder_path:
    print("No folder selected. Program cancelled.")
    sys.exit()

folder = Path(folder_path)


# -----------------------------
# Find supported files
# -----------------------------

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

print(f"Found {len(files)} supported files.\n")


# -----------------------------
# Handle empty folders
# -----------------------------

if len(files) == 0:
    print("No supported photos or videos were found.")
    print("Supported file types: JPG, JPEG, PNG and MP4.")
    sys.exit()


# -----------------------------
# Choose filename prefix
# -----------------------------

prefix = input("Enter filename prefix: ").strip()

if not prefix:
    print("No prefix entered. Program cancelled.")
    sys.exit()

# Remove characters that aren't safe in filenames on Windows/Mac/Linux
prefix = re.sub(r'[<>:"/\\|?*]', "_", prefix)


# -----------------------------
# Create preview
# -----------------------------

print("\nPreview:")
print("-" * 45)

new_paths = []

for i, file in enumerate(files, start=1):

    extension = file.suffix
    new_name = f"{prefix}_{i:03}{extension}"
    new_path = folder / new_name

    # Check whether the destination already exists
    if new_path.exists():
        print(f"\nERROR: {new_name} already exists.")
        print("No files have been renamed.")
        sys.exit()

    new_paths.append((file, new_path))

    print(f"{file.name}  →  {new_name}")


# -----------------------------
# Confirm before renaming
# -----------------------------

confirm = input("\nRename these files? (y/n): ")

if confirm.lower() not in ["y", "yes"]:
    print("\nCancelled. No files were changed.")
    sys.exit()


# -----------------------------
# Rename files
# -----------------------------

print("\nRenaming files...")

total_files = len(new_paths)
renamed_count = 0
failed = []

for i, (old_file, new_file) in enumerate(new_paths, start=1):

    try:
        old_file.rename(new_file)
        renamed_count += 1
        print(f"Renaming file {i} of {total_files}...")
    except OSError as e:
        failed.append((old_file.name, str(e)))
        print(f"FAILED: {old_file.name} — {e}")


# -----------------------------
# Finished
# -----------------------------

print("\n" + "=" * 45)
print(f"Successfully renamed {renamed_count} of {total_files} files.")
print("=" * 45)

if failed:
    print(f"\n{len(failed)} file(s) could not be renamed:")
    for name, err in failed:
        print(f"  - {name}: {err}")