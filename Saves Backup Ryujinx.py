import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
import subprocess

# Get the parent directory of the script's directory
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.dirname(script_dir)

# Select output file
output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".zip", filetypes=(("Zip Files", "*.zip"),))

if not output_file:
    print("No output file location or name selected.")
    input("Press Enter to exit.")
    exit()

# Create a .zip file in write mode
with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    # Traverse files and folders in the parent directory
    for root_folder, subfolders, filenames in os.walk(parent_dir):
        # Get the relative path of the current folder
        relative_folder = os.path.relpath(root_folder, parent_dir)

        # Exclude the "saveMeta" and "scripts" folders from being included in the .zip file
        if 'saveMeta' in subfolders:
            subfolders.remove('saveMeta')
        if 'scripts' in subfolders:
            subfolders.remove('scripts')

        # Traverse files in the current folder
        for filename in filenames:
            # Build the source and destination paths for each file
            input_file = os.path.join(root_folder, filename)
            relative_file = os.path.join(relative_folder, filename)

            # Add the file to the .zip file with the preserved relative path
            zipf.write(input_file, arcname=relative_file)

print("Compressed file copy created at:", output_file)
input("Press Enter to exit.")