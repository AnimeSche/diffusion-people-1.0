import os
import zipfile
from pathlib import Path


def zip_folder(folder_path, zip_path):
    """
    Zips the contents of an entire folder (including subfolders).

    :param folder_path: Path to the folder to be zipped.
    :param zip_path: Path where the zip file will be saved.
    """
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname)


# Example usage:

dics = Path('E:')
folder_to_zip = dics / 'Karina' / 'hdr' / 'to_dataset' / 'karina' / 'top'
output_zip = os.getcwd()
zip_folder(folder_to_zip, output_zip)
