from tkinter import Tk, Button, Radiobutton, Label, StringVar, IntVar, Entry

class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")          # Window title
        window.configure(background="sky blue")     # Background color
        window.geometry("375x250")                  # Window size
        window.resizable(width=False, height=False) # Disable resizing

        # -------------------- VARIABLES --------------------
        self.meal_cost = StringVar()    # Stores meal/bill cost
        self.tip_percent = IntVar()     # Stores selected tip percentage
        self.tip = StringVar()          # Stores calculated tip
        self.total_cost = StringVar()   # Stores final bill (meal + tip)

        # -------------------- LABELS --------------------
        tip_percents = Label(window, text="Tip Percentage", bg="black", fg="white")
        tip_percents.grid(row=0, column=0, padx=15)

        bill_amount = Label(window, text="Bill Amount", bg="light pink", fg="white")
        bill_amount.grid(row=0, column=1, padx=15)

        # -------------------- ENTRY FOR BILL AMOUNT --------------------
        bill_amnt_entry = Entry(window, textvariable=self.meal_cost, width=14)
        bill_amnt_entry.grid(row=0, column=2)

        # -------------------- RADIO BUTTONS FOR TIP SELECTION --------------------
        # Each button sets self.tip_percent to a value when selected
        five_tip = Radiobutton(window, text="0.5%", variable=self.tip_percent, value=5)
        five_tip.grid(column=0, row=1)

        ten_tip = Radiobutton(window, text="0.10%", variable=self.tip_percent, value=10)
        ten_tip.grid(column=0, row=2)

        fifteen_tip = Radiobutton(window, text="0.15%", variable=self.tip_percent, value=15)
        fifteen_tip.grid(column=0, row=3)

        twenty_tip = Radiobutton(window, text="0.20%", variable=self.tip_percent, value=20)
        twenty_tip.grid(column=0, row=4)

        twenty_five_tip = Radiobutton(window, text="0.25%", variable=self.tip_percent, value=25)
        twenty_five_tip.grid(column=0, row=5)

        thirty_tip = Radiobutton(window, text="0.30%", variable=self.tip_percent, value=30)
        thirty_tip.grid(column=0, row=6)

        # -------------------- TIP AMOUNT --------------------
        tip_amnt_label = Label(window, text="Tip Amount", bg="brown", fg="white")
        tip_amnt_label.grid(column=1, row=3, padx=15)

        tip_amnt_entry = Entry(window, textvariable=self.tip, width=14)
        tip_amnt_entry.grid(row=3, column=2)

        # -------------------- TOTAL BILL --------------------
        bill_total_label = Label(window, text="Bill Total", bg="dark blue", fg="white")
        bill_total_label.grid(column=1, row=5, padx=15)

        bill_total_entry = Entry(window, textvariable=self.total_cost, width=14)
        bill_total_entry.grid(row=5, column=2)

        # -------------------- BUTTONS --------------------
        calculate_btn = Button(window, text="Calculate", bg="red", fg="white", command=self.calculate)
        calculate_btn.grid(column=1, row=7, padx=15)

        clear_btn = Button(window, text="Clear", bg="grey", fg="white", command=self.clear)
        clear_btn.grid(column=2, row=7)

        window.mainloop()

    # -------------------- FUNCTION TO CALCULATE TIP --------------------
    def calculate(self):
       pre_tip = float(self.meal_cost.get())   # Get bill amount
       percentage = self.tip_percent.get() / 100   # Convert selected tip % into decimal
       tip_amount_entry = pre_tip * percentage     # Calculate tip
       self.tip.set(tip_amount_entry)              # Show tip in entry field

       final_bill = pre_tip + tip_amount_entry     # Add tip to meal cost
       self.total_cost.set(final_bill)             # Show total bill

    # -------------------- FUNCTION TO CLEAR ALL FIELDS --------------------
    def clear(self):
        self.total_cost.set("")   # Clear total bill
        self.meal_cost.set("")    # Clear bill amount
        self.tip.set("")          # Clear tip


# Run the application
TipCalculator()
