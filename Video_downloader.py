import tkinter
import customtkinter
from pytube import YouTube

# function or command
def download_video():
    try:
        ytlink = url_var.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()
        video.download()
        FinishLabel.configure(text="Downloaded successfully!", text_color="green")
    except Exception as e:
        FinishLabel.configure(text=f"Error: {e}", text_color="red")

# System Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# adding UI elements
title = customtkinter.CTkLabel(app, text="Insert the YouTube link to download")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
ytlink = customtkinter.CTkEntry(app, textvariable=url_var, width=350, height=40)
ytlink.pack(padx=10, pady=10)

# button
download = customtkinter.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=10)

# finished downloading label
FinishLabel = customtkinter.CTkLabel(app, text="")
FinishLabel.pack(padx=10, pady=10)

# Run App
app.mainloop()
