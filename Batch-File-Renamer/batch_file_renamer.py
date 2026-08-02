from pathlib import Path

# Find the folder containing this script
script_folder = Path(__file__).parent

# Locate the sample_files folder
folder = script_folder / "sample_files"

# Get every item inside the folder
files = list(folder.iterdir())

# Remove hidden files
files = sorted(
    [file for file in files if not file.name.startswith(".")]
)

print(f"Found {len(files)} files.\n")

# Ask the user for a filename prefix
prefix = input("Enter a filename prefix: ")

print("\nFiles will be renamed as:\n")

# Show a preview
for i, file in enumerate(files, start=1):
    extension = file.suffix
    new_name = f"{prefix}_{i:03}{extension}"
    print(f"{file.name}  →  {new_name}")

# Ask for confirmation
confirm = input("\nRename these files? (y/n): ")

if confirm.lower() == "y":

    for i, file in enumerate(files, start=1):
        extension = file.suffix
        new_name = f"{prefix}_{i:03}{extension}"

        new_path = folder / new_name

        file.rename(new_path)

    print("\nDone!")

else:
    print("\nNo files were renamed.")