import os
import sys
import requests
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

# Function to send a message to Telegram
def send_to_telegram(api_token, chat_id, message):
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

# Main script
print("Searching for empty folders...")

# Check if the required command line arguments are provided
if len(sys.argv) != 4:
    print("Error: Please provide the search path, API token, and chat ID as command line arguments.")
    sys.exit(1)

# Get command line arguments
search_path = sys.argv[1]
api_token = sys.argv[2]
chat_id = sys.argv[3]

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

        # Send a notification to Telegram
        event_name = 'Deleted folders'
        message = f"{event_name}:\n\n"
        for folder in deleted_folders:
            message += f"- {folder}\n"

        send_to_telegram(api_token, chat_id, message)

        print(f"Empty folders deleted successfully. Deleted folders listed in {log_filename}.")
    else:
        print("No empty folders found.")
else:
    print("Error: The specified path does not exist.")
