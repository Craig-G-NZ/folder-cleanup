# folder-cleanup
Part of my automation for my home server setup. Jenkins periodically calls the script to clean up any empty folders.

    delete-folders.py "folder_path" "telegram_api_token" "telegram_chat_id"

If the telegram api and chat id variables are provided you will receive a message. If not provided the folders will be deleted with no notification.
