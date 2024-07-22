import os
import zipfile
from pathlib import Path

import shutil


def zip_folder(folder_path, zip_path):
    """
    Zips the contents of an entire folder (including subfolders).

    :param folder_path: Path to the folder to be zipped.
    :param zip_path: Path where the zip file will be saved.
    """
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=folder_path)
                    zipf.write(file_path, arcname)
        print(f"Successfully created zip file: {zip_path}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
        print("Please check the permissions of the files and the destination directory.")


# Example usage:

dics = Path('E:\\')
repo_dir = dics / 'diffusion-people-1.0'
karina_folder = dics / 'Karina' / 'hdr' / 'to_dataset' / 'karina'
dataset_folder = karina_folder / 'top' / 'valid'
zip  = repo_dir / 'valid.zip'
zip_folder(dataset_folder, zip)
