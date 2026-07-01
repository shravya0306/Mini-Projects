from tkinter import *

class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")      # Set window title
        window.configure(bg="white")         # Set background color

        # -------------------- LABELS --------------------
        # These are static text labels for the form
        Label(window, font="Helvetica 12 bold", bg="light green", text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="Total Payment").grid(row=5, column=1, sticky=W)

        # -------------------- INPUT FIELDS --------------------
        # User can type Annual Interest Rate
        self.AnnualinterestRateVar = StringVar()
        Entry(window, textvariable=self.AnnualinterestRateVar, justify=RIGHT).grid(row=1, column=2)

        # User can type Number of Years
        self.NoofyearsVar = StringVar()
        Entry(window, textvariable=self.NoofyearsVar, justify=RIGHT).grid(row=2, column=2)

        # User can type Loan Amount
        self.LoanAmntVar = StringVar()
        Entry(window, textvariable=self.LoanAmntVar, justify=RIGHT).grid(row=3, column=2)

        # -------------------- OUTPUT LABELS --------------------
        # This will show calculated Monthly Payment
        self.monthlypaymentVar = StringVar()
        Label(window, font="Helvetica 12 bold", bg="brown", fg="white",
              textvariable=self.monthlypaymentVar).grid(row=4, column=2, sticky=E)

        # This will show calculated Total Payment
        self.TotalPaymentVar = StringVar()
        Label(window, font="Helvetica 12 bold", bg="purple", fg="white",
              textvariable=self.TotalPaymentVar).grid(row=5, column=2, sticky=E)

        # -------------------- BUTTONS --------------------
        # Button to compute monthly and total payments
        Button(window, text="Compute Payment", bg="red", fg="white",
               font="Helvetica 12 bold", command=self.ComputePayment).grid(row=6, column=2, sticky=E)

        # Button to clear all input and output fields
        Button(window, text="Clear", bg="red", fg="white",
               font="Helvetica 12 bold", command=self.delete).grid(row=7, column=2, padx=20, pady=20, sticky=E)

        window.mainloop()

    # -------------------- FUNCTION TO CALCULATE PAYMENTS --------------------
    def ComputePayment(self):
        # Get user inputs and calculate monthly payment
        monthlyPayment = self.getMonthlyPayment(
            float(self.LoanAmntVar.get()),                # Loan Amount
            float(self.AnnualinterestRateVar.get()) / 1200, # Monthly interest rate
            int(self.NoofyearsVar.get())                  # Number of years
        )

        # Set calculated monthly payment
        self.monthlypaymentVar.set(format(monthlyPayment, '10.2f'))

        # Calculate and set total payment
        totalPayment = float(self.monthlypaymentVar.get()) * 12 * int(self.NoofyearsVar.get())
        self.TotalPaymentVar.set(format(totalPayment, '10.2f'))

    # Formula for loan amortization (monthly payments)
    def getMonthlyPayment(self, LoanAmntVar, monthlyInterestRate, NoofyearsVar):
        monthlyPayment = LoanAmntVar * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-NoofyearsVar * 12))
        return monthlyPayment

    # -------------------- FUNCTION TO CLEAR FIELDS --------------------
    def delete(self):
        self.AnnualinterestRateVar.set("")   # Clear interest rate
        self.NoofyearsVar.set("")            # Clear years
        self.LoanAmntVar.set("")             # Clear loan amount
        self.monthlypaymentVar.set("")       # Clear monthly payment
        self.TotalPaymentVar.set("")         # Clear total payment


# Run the application
LoanCalculator()
