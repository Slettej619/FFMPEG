import os
import shutil

def copy_and_rename_files_in_order(source_folders, parent_directory):
    # Create the destination folder within the parent directory
    destination_folder = os.path.join(parent_directory, "xxx_video_buffer")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Counter for file numbering
    file_number = 1

    for folder in source_folders:
        for filename in sorted(os.listdir(folder)):
            # Construct the full file path
            file_path = os.path.join(folder, filename)

            # Extract the file extension
            _, file_extension = os.path.splitext(filename)

            # Extract folder name and append it to the new file name
            folder_name = os.path.basename(folder)
            new_filename = f"frame_{file_number}_{folder_name}{file_extension}"

            # Construct the destination file path
            dest_file_path = os.path.join(destination_folder, new_filename)

            # Copy the file to the destination folder
            shutil.copy2(file_path, dest_file_path)

            # Increment the file number
            file_number += 1

    print("Files copied and renamed successfully.")

# Define the parent directory
parent_directory = "D:\\xxx\xxx"

# Define the source folders
source_folders = [
    os.path.join(parent_directory, f"PURSE_{i}") for i in range(xx, xx) if i != x
]

# Call the function to copy and rename the files
copy_and_rename_files_in_order(source_folders, parent_directory)
