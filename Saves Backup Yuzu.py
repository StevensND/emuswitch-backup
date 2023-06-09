import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
import subprocess

def open_qt_config():
    # Locate "config" folder
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_folder = os.path.join(script_dir, 'config')

    # Check if "config" folder exists
    if not os.path.exists(config_folder):
        print("No 'config' folder found.")
        return

    # Locate "qt-config.ini" file in the "config" folder
    qt_config_file = os.path.join(config_folder, "qt-config.ini")

    # Check if "qt-config.ini" file exists
    if not os.path.isfile(qt_config_file):
        print("No 'qt-config.ini' file found in the 'config' folder.")
        return

# Read nand_directory from qt-config.ini
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_folder = os.path.join(script_dir, 'config')
qt_config_file = os.path.join(config_folder, "qt-config.ini")

if not os.path.isfile(qt_config_file):
    print("No 'qt-config.ini' file found in the 'config' folder.")
    input("Press Enter to exit.")
    exit()

with open(qt_config_file, 'r') as file:
    for line in file:
        if line.startswith('nand_directory='):
            input_folder = line.replace('nand_directory=', '').strip()
            # Append additional information to the input_folder path
            input_folder = os.path.join(input_folder, 'user', 'save')
            break
    else:
        print("No 'nand_directory' entry found in 'qt-config.ini'.")
        input("Press Enter to exit.")
        exit()

# Select output file
output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".zip", filetypes=(("Zip Files", "*.zip"),))

if not output_file:
    print("No output file location or name selected.")
    input("Press Enter to exit.")
    exit()

# Create a .zip file in write mode
with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    # Traverse files and folders in the input folder
    for root_folder, subfolders, filenames in os.walk(input_folder):
        # Get the relative path of the current folder
        relative_folder = os.path.relpath(root_folder, input_folder)
        
        # Exclude the "cache" folder from being included in the .zip file
        if 'cache' in subfolders:
            subfolders.remove('cache')
        
        # Traverse files in the current folder
        for filename in filenames:
            # Build the source and destination paths for each file
            input_file = os.path.join(root_folder, filename)
            relative_file = os.path.join(relative_folder, filename)
            
            # Add the file to the .zip file with the preserved relative path
            zipf.write(input_file, arcname=relative_file)
            
print("Compressed file copy created at:", output_file)
input("Press Enter to exit.")