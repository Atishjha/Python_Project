import os
import shutil
from datetime import datetime

def backup(source_dir , dest_dir):
    """ Backs up files from a source directory to a destination directory.
    Args:
         source_dir : Path to the directory containing the files to be backed up.
         dest_dir : Path to the destination where the backup will be stored.

    """
    # Get current date and format for filename
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Create destination directory with date if it doesn't exist
    dest_path = os.path.join(dest_dir , current_date)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Loop through files in source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir , filename)
        dest_file = os.path.join(dest_path , filename)
        # Check if it's a file (not a directory)
        if os.path.isfile(source_path):
            try:
                shutil.copy2(source_path,dest_file)
                print(f"Copied {filename} to {dest_file}")
            except Exception as e:
                print(f"Error copying {filename}: {e}")

# Example usage (replacing with your directory paths)
source_dir = "C://Users//KIIT0001//Desktop//C practice//Projects//Python Project"
dest_dir = "C://Users//KIIT0001//Desktop//Programminglab//Home work"
backup(source_dir , dest_dir)
