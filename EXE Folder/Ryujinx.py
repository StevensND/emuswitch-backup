import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
import subprocess

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select directory")
    if not directory:
        print("No directory selected.")
        input("Press Enter to exit.")
        return None
    return directory

def compress_directory():
    # Select base directory
    base_directory = select_directory()
    if not base_directory:
        return

    # Select output file
    output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".zip", filetypes=(("Zip Files", "*.zip"),))

    if not output_file:
        print("No output file location or name selected.")
        input("Press Enter to exit.")
        return

    # Create a .zip file in write mode
    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        # Get the absolute path of the "save" folder inside "user"
        save_folder = os.path.join(base_directory, "bis", "user", "save")

        # Traverse files and folders in the "save" folder
        for root_folder, _, filenames in os.walk(save_folder):
            # Get the relative path of the current folder
            relative_folder = os.path.relpath(root_folder, save_folder)

            for filename in filenames:
                file_path = os.path.join(root_folder, filename)

                # Build the destination path for the file within the ZIP
                relative_file = os.path.join("save", relative_folder, filename)

                # Add the file to the .zip file with the preserved relative path
                zipf.write(file_path, arcname=relative_file)

    print("Compressed file copy created at:", output_file)
    input("Press Enter to exit.")

compress_directory()
