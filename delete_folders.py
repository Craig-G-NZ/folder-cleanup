import os
import sys
from datetime import datetime

# Function to delete empty folders and log deleted folder names
def delete_empty_folders(path):
    deleted_folders = []
    for root, dirs, files in os.walk(path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                print(f"Deleting empty folder: {folder_path}")
                deleted_folders.append(folder_path)
                os.rmdir(folder_path)
    return deleted_folders

# Main script
print("Searching for empty folders...")

# Check if the search path is provided as a command line argument
if len(sys.argv) != 2:
    print("Error: Please provide the search path as a command line argument.")
    sys.exit(1)

# Get the search path from the command line argument
search_path = sys.argv[1]

# Check if the provided path exists
if os.path.isdir(search_path):
    # Call the function to delete empty folders
    deleted_folders = delete_empty_folders(search_path)

    # Check if any folders were deleted
    if deleted_folders:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"deleteme_{timestamp}.txt"
        with open(log_filename, 'w') as log_file:
            for folder in deleted_folders:
                log_file.write(folder + '\n')
        print(f"Empty folders deleted successfully. Deleted folders listed in {log_filename}.")
    else:
        print("No empty folders found.")
else:
    print("Error: The specified path does not exist.")
