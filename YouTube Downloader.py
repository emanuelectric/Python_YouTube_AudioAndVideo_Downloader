import os
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import threading
import pytube


def download_video():
    def download():
        video_url = url_entry.get()
        try:
            yt = pytube.YouTube(video_url)
            stream = (
                yt.streams.filter(progressive=True)
                .order_by("resolution")
                .desc()
                .first()
            )

            # Get the title of the YouTube video
            video_title = yt.title

            # Create a folder to save the video in Downloads directory
            download_folder = os.path.join(
                os.path.expanduser("~"), "Downloads", "YouTubeVideos"
            )
            os.makedirs(download_folder, exist_ok=True)

            # Download the video to the created folder with the video title as filename
            stream.download(output_path=download_folder, filename=f"{video_title}.mp4")

            messagebox.showinfo("Success", "Video downloaded successfully!")
            loading_label.config(text="")
            progress_bar["value"] = 0
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            loading_label.config(text="")
            progress_bar["value"] = 0

    loading_label.config(text="Downloading...", fg="blue")
    threading.Thread(target=download).start()


def download_audio():
    def download():
        video_url = url_entry.get()
        try:
            yt = pytube.YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Get the title of the YouTube video
            video_title = yt.title

            # Create a folder to save the audio in Downloads directory
            download_folder = os.path.join(
                os.path.expanduser("~"), "Downloads", "YouTubeAudios"
            )
            os.makedirs(download_folder, exist_ok=True)

            # Download the audio to the created folder with the video title as filename
            audio_file = audio_stream.download(
                output_path=download_folder, filename=f"{video_title}.mp4"
            )

            # Optionally convert to MP3
            base, ext = os.path.splitext(audio_file)
            new_file = base + ".mp3"
            os.rename(audio_file, new_file)

            messagebox.showinfo("Success", "Audio downloaded successfully!")
            loading_label.config(text="")
            progress_bar["value"] = 0
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            loading_label.config(text="")
            progress_bar["value"] = 0

    loading_label.config(text="Downloading...", fg="blue")
    threading.Thread(target=download).start()


# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")

# Create and place the description label
description_label = tk.Label(root, text="Enter the YouTube link:")
description_label.pack(pady=5)

# Create and place the URL entry field
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the Download Video button
download_video_button = tk.Button(root, text="Download Video", command=download_video)
download_video_button.pack(pady=10)

# Create and place the Download Audio button
download_audio_button = tk.Button(root, text="Download Audio", command=download_audio)
download_audio_button.pack(pady=10)

# Create and place the loading label
loading_label = tk.Label(root, text="", fg="blue")
loading_label.pack()

# Create and place the progress bar
progress_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Run the application
root.mainloop()
