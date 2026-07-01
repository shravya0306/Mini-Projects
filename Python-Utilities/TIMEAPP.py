#Importing Modules
from tkinter import *
from time import strftime


root=Tk() #Creates tkinter window
root.title("Digital Computer Clock")  #Adds title to the tkinter window

def time(): #Function used to display timw on the label
    string=strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000,time)

#styling the label widget
lbl=Label(root,font=("arial",160,"bold"),bg="black",fg="white")
lbl.pack(anchor="center",fil="both",expand=1)  #packs widgets into rows and columns and positions labels

time() #calling the time funtion
mainloop() #runs the application program
