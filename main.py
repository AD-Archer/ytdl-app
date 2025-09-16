import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

class YTDLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Variables
        self.url = tk.StringVar()
        self.quality = tk.StringVar(value="720p")
        self.audio_only = tk.BooleanVar()
        self.download_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="YouTube Downloader", font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        # URL Input
        url_frame = tk.Frame(self.root)
        url_frame.pack(pady=10)
        url_label = tk.Label(url_frame, text="YouTube URL:", font=("Arial", 12))
        url_label.pack(side=tk.LEFT)
        url_entry = tk.Entry(url_frame, textvariable=self.url, width=40, font=("Arial", 10))
        url_entry.pack(side=tk.LEFT, padx=10)

        # Quality Selection
        quality_frame = tk.Frame(self.root)
        quality_frame.pack(pady=10)
        quality_label = tk.Label(quality_frame, text="Quality:", font=("Arial", 12))
        quality_label.pack(side=tk.LEFT)
        qualities = ["240p", "360p", "480p", "720p", "1080p", "4K"]
        quality_menu = tk.OptionMenu(quality_frame, self.quality, *qualities)
        quality_menu.config(font=("Arial", 10))
        quality_menu.pack(side=tk.LEFT, padx=10)

        # Audio Only Checkbox
        audio_check = tk.Checkbutton(self.root, text="Audio Only", variable=self.audio_only, font=("Arial", 12))
        audio_check.pack(pady=10)

        # Download Location
        path_frame = tk.Frame(self.root)
        path_frame.pack(pady=10)
        path_label = tk.Label(path_frame, text="Download Location:", font=("Arial", 12))
        path_label.pack(side=tk.LEFT)
        path_entry = tk.Entry(path_frame, textvariable=self.download_path, width=30, font=("Arial", 10))
        path_entry.pack(side=tk.LEFT, padx=10)
        browse_button = tk.Button(path_frame, text="Browse", command=self.browse_path, font=("Arial", 10))
        browse_button.pack(side=tk.LEFT)

        # Download Button
        download_button = tk.Button(self.root, text="Download", command=self.download, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        download_button.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(self.root, text="", font=("Arial", 10), fg="blue")
        self.status_label.pack(pady=10)

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.download_path.set(path)

    def download(self):
        url = self.url.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        quality = self.quality.get()
        audio_only = self.audio_only.get()
        path = self.download_path.get()

        # Map quality to yt-dlp format
        quality_map = {
            "240p": "best[height<=240]",
            "360p": "best[height<=360]",
            "480p": "best[height<=480]",
            "720p": "best[height<=720]",
            "1080p": "best[height<=1080]",
            "4K": "best[height>=2160]"
        }

        format_str = quality_map.get(quality, "best")

        # yt-dlp options
        ydl_opts = {
            'format': format_str,
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        }

        if audio_only:
            ydl_opts['extractaudio'] = True
            ydl_opts['audioformat'] = 'mp3'

        self.status_label.config(text="Downloading...", fg="orange")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text="Download completed successfully!", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = YTDLApp(root)
    root.mainloop()