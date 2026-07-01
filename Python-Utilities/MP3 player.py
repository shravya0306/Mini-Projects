import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# -------------------- MAIN WINDOW --------------------
musicplayer = tkr.Tk()
musicplayer.title("Music Player")      # Set window title
musicplayer.geometry("450x350")        # Set window size

# -------------------- SELECT MUSIC DIRECTORY --------------------
directory = askdirectory()             # Ask user to choose a folder
os.chdir(directory)                    # Change working directory to chosen folder
songlist = os.listdir()                # Get list of files in that folder

# -------------------- PLAYLIST LISTBOX --------------------
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold",
                       bg="light green", selectmode=tkr.SINGLE)

# Add songs to the playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)   # Insert song into playlist
    pos += 1

# -------------------- INITIALIZE PYGAME MIXER --------------------
pygame.init()
pygame.mixer.init()

# -------------------- MUSIC CONTROL FUNCTIONS --------------------
def play():
    # Load and play the selected song
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))  # Show song name
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()   # Stop playing

def pause():
    pygame.mixer.music.pause()  # Pause music

def unpause():
    pygame.mixer.music.unpause() # Resume music

# -------------------- BUTTONS --------------------
bt1 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                 text="PLAY", bg="yellow", fg="white", command=play)

bt2 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                 text="STOP", bg="yellow", fg="white", command=stop)

bt3 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                 text="PAUSE", bg="yellow", fg="white", command=pause)

bt4 = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                 text="UNPAUSE", bg="yellow", fg="white", command=unpause)

# -------------------- SONG TITLE LABEL --------------------
var = tkr.StringVar()   # For displaying currently playing song
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

# -------------------- PACKING WIDGETS --------------------
songtitle.pack()
bt1.pack(fill="x")
bt2.pack(fill="x")
bt3.pack(fill="x")
bt4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

# -------------------- RUN THE APP --------------------
musicplayer.mainloop()
