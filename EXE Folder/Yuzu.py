import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
import subprocess

def open_qt_config():
    # Prompt the user to select the base directory where the search should start
    root = tk.Tk()
    root.withdraw()
    base_directory = filedialog.askdirectory(title="Select base directory")
    if not base_directory:
        print("No base directory selected.")
        input("Press Enter to exit.")
        return

    # Select output file
    output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".zip", filetypes=(("Zip Files", "*.zip"),))

    if not output_file:
        print("No output file location or name selected.")
        input("Press Enter to exit.")
        return

    # Create a .zip file in write mode
    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        # Traverse files and folders in the base directory and its subdirectories
        for root_folder, _, filenames in os.walk(base_directory):
            # Check if "config" folder exists in the current folder
            config_folder = os.path.join(root_folder, 'config')
            if not os.path.exists(config_folder):
                continue

            # Locate "qt-config.ini" file in the "config" folder
            qt_config_file = os.path.join(config_folder, "qt-config.ini")

            # Check if "qt-config.ini" file exists
            if not os.path.isfile(qt_config_file):
                continue

            # Read nand_directory from qt-config.ini
            with open(qt_config_file, 'r') as file:
                for line in file:
                    if line.startswith('nand_directory='):
                        input_folder = line.replace('nand_directory=', '').strip()
                        # Append additional information to the input_folder path
                        input_folder = os.path.join(input_folder, 'user', 'save')
                        break
                else:
                    print(f"No 'nand_directory' entry found in 'qt-config.ini' of {config_folder}.")
                    continue

            # Traverse files and folders in the input folder
            for root, _, files in os.walk(input_folder):
                # Get the relative path of the current folder
                relative_folder = os.path.relpath(root, input_folder)

                # Exclude the "cache" folder from being included in the .zip file
                if 'cache' in _:
                    _.remove('cache')

                # Traverse files in the current folder
                for filename in files:
                    # Build the source and destination paths for each file
                    input_file = os.path.join(root, filename)
                    relative_file = os.path.join(relative_folder, filename)

                    # Add the file to the .zip file with the preserved relative path
                    zipf.write(input_file, arcname=relative_file)

    print("Compressed file copy created at:", output_file)
    input("Press Enter to exit.")

open_qt_config()
