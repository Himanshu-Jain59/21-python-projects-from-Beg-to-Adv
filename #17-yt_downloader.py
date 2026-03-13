import pytube
import tkinter as tk
from tkinter import filedialog

def download(url,save_path):
    try:
        yt = pytube.YouTube(url)
        streams  = yt.streams.filter(progressive=True,file_extention="mp4")
        higest_resol = streams.get_higest_resolution()
        higest_resol.download(output_path=save_path)
        print("Video Downloaded Successfully")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")

    return folder

if __name__=="__main__":
    root=tk.Tk()
    root.withdraw()

    video_url = input("Enter youtube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("started downloading....")
        download(video_url,save_dir)
    else:
        print("Invalid save location!")