from tkinter import Tk, Button, DoubleVar, Label, Entry

# Create the main window
window = Tk()
window.title("Feet to meter conversion app")   # Set window title
window.configure(background="yellow")          # Set background color
window.geometry("320x220")                     # Set fixed window size
window.resizable(width=False, height=False)    # Disable resizing


# Function to convert feet to meters
def convert():
    value = float(ft_entry.get())       # Get value from feet entry box
    meter = value * 0.3048              # Convert feet to meters
    mt_value.set("%.4f" % meter)        # Show result in meter entry (4 decimals)


# Function to clear both input and output fields
def clear():
    ft_value.set("")    # Clear feet entry
    mt_value.set("")    # Clear meter entry


# Label for feet input
ft_lbl = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

# Entry box for feet value
ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')   # Clear any default value


# Label for meter output
mt_lbl = Label(window, text="Meter", bg="brown", fg="white", width=14)
mt_lbl.grid(column=0, row=1)

# Entry box for meter value (output)
mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')   # Clear any default value


# Convert button
convert_btn = Button(window, text="Convert", bg="red", fg="white", width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

# Clear button
clear_btn = Button(window, text="Clear", bg="black", fg="white", width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15)


# Run the Tkinter event loop
window.mainloop()
