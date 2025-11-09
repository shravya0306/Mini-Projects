from tkinter import *
from tkinter import font
import datetime

def quit_app(event=None):
    root.destroy()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    if timeLeft.total_seconds() > 0:
        timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
        txt.set(timeLeft)
        root.after(1000, cant_wait)
    else:
        txt.set("Time's up!")

# main window
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")

# bind quit key (press 'x' to exit)
root.bind("<x>", quit_app)

# set end time first
endTime = datetime.datetime(2025, 9, 30, 9, 0, 0)

# font and label
fnt = font.Font(family="Helvetica", size=90, weight="bold")
txt = StringVar()
lbl = Label(root, textvariable=txt, font=fnt, fg="white", bg="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

# start countdown
cant_wait()

root.mainloop()
