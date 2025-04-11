import os
import shutil

# Folder you want to organize (can be modified)
TARGET_FOLDER = "/path/to/your/folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def create_folder(folder_name):
    folder_path = os.path.join(TARGET_FOLDER, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_files():
    print(f"Organizing files in: {TARGET_FOLDER}")
    files = [f for f in os.listdir(TARGET_FOLDER) if os.path.isfile(os.path.join(TARGET_FOLDER, f))]

    for file_name in files:
        file_path = os.path.join(TARGET_FOLDER, file_name)
        file_extension = os.path.splitext(file_name)[1]
        category = get_category(file_extension)
        destination_folder = create_folder(category)
        destination_path = os.path.join(destination_folder, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"Moved: {file_name} ➡️ {category}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

    print("✅ File organization complete!")

if __name__ == "__main__":
    organize_files()
