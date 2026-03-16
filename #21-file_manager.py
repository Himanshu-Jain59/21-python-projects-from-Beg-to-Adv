import os
import shutil
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from tkinter import filedialog

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
}

class OrganizerHandler(FileSystemEventHandler):

    def __init__(self, folder):
        self.folder = folder

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        # wait until file is ready
        for i in range(5):
            try:
                with open(file_path, "rb"):
                    break
            except PermissionError:
                time.sleep(1)

        if not is_duplicate(file_path):
            organize_file(file_path, self.folder)
        else:
            os.remove(file_path)
            print("Duplicate file removed:", file_path)
            
# Duplicate Detection
def get_file_hash(path):
    hasher = hashlib.md5()

    with open(path, 'rb') as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
    

def backup_file(file_path, base_folder):

    backup_folder = os.path.join(base_folder, "Backup")

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    filename = os.path.basename(file_path)

    backup_path = os.path.join(backup_folder, filename)

    shutil.copy2(file_path, backup_path)

def organize_file(file_path, base_folder):

    if not os.path.isfile(file_path):
        return

    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[1].lower()

    destination_folder = "Others"

    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            destination_folder = folder
            break

    folder_path = os.path.join(base_folder, destination_folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    new_path = os.path.join(folder_path, filename)

    if os.path.exists(new_path):
        filename = str(int(time.time())) + "_" + filename
        new_path = os.path.join(folder_path, filename)

    shutil.move(file_path, new_path)
    backup_file(new_path, base_folder)


seen_hashes = set()

def is_duplicate(file_path):

    file_hash = get_file_hash(file_path)

    if file_hash in seen_hashes:
        return True

    seen_hashes.add(file_hash)
    return False

def start_monitoring(folder):

    event_handler = OrganizerHandler(folder)

    observer = Observer()
    observer.schedule(event_handler, folder, recursive=False)

    observer.start()

    print("Monitoring folder:", folder)

    try:
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()

def process_existing_files(folder):

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):

            try:
                if not is_duplicate(file_path):
                    organize_file(file_path, folder)
                else:
                    os.remove(file_path)
                    print("Duplicate file removed:", file_path)

            except PermissionError:
                print("File locked, skipping:", file_path)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")

    return folder

if __name__ == "__main__":

    folder_to_watch = open_file_dialog()

    if not os.path.exists(folder_to_watch):
        os.makedirs(folder_to_watch)
    
    process_existing_files(folder_to_watch)

    start_monitoring(folder_to_watch)