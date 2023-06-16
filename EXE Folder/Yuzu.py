import sys
from pathlib import Path
import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog

def resolve_path(path: str | Path) -> Path:
    if getattr(sys, "frozen", False):
        # If the script is running as a bundled app (.exe)
        script_dir = Path(sys.executable).resolve().parent
    else:
        # If the script is running in development mode
        script_dir = Path(__file__).resolve().parent

    config_folder = script_dir.parent / 'config'
    resolved_path = config_folder / path
    return resolved_path

def open_qt_config():
    # Locate "qt-config.ini" file in the "config" folder
    qt_config_file = resolve_path("qt-config.ini")

    # Check if "qt-config.ini" file exists
    if not os.path.isfile(qt_config_file):
        print("No 'qt-config.ini' file found in the 'config' folder.")
        input("Press Enter to exit.")
        return

    # Read nand_directory from qt-config.ini
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
            return

    # Select output file
    output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".zip", filetypes=(("Zip Files", "*.zip"),))

    if not output_file:
        print("No output file location or name selected.")
        return

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

if __name__ == "__main__":
    open_qt_config()
    input("Press Enter to exit.")