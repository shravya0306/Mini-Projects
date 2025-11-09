from tkinter import *
# Creating a Calculator Application using Tkinter
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg="lime green", bd=29, insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)
        self.user_input.insert(0, "0")

        # Number buttons
        self.button1 = Button(self, bg="light yellow", bd=12, text="7", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(7))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="light yellow", bd=12, text="8", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(8))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = Button(self, bg="light yellow", bd=12, text="9", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(9))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg="light yellow", bd=12, text="4", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self, bg="light yellow", bd=12, text="5", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = Button(self, bg="light yellow", bd=12, text="6", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = Button(self, bg="light yellow", bd=12, text="1", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8 = Button(self, bg="light yellow", bd=12, text="2", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9 = Button(self, bg="light yellow", bd=12, text="3", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button10 = Button(self, bg="light yellow", bd=12, text="0", padx=33, pady=25,
                               font=("Helvetica", 20, "bold"), command=lambda: self.buttonClick(0))
        self.button10.grid(row=5, column=0, sticky=W)

        # Operators
        self.Addbutton = Button(self, bg="orange", bd=12, text="+", padx=36, pady=25,
                                command=lambda: self.buttonClick("+"), font=("Helvetica", 20, "bold"))
        self.Addbutton.grid(row=2, column=3, sticky=W)

        self.Subbutton = Button(self, bg="orange", bd=12, text="-", padx=39, pady=25,
                                command=lambda: self.buttonClick("-"), font=("Helvetica", 20, "bold"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        self.Mulbutton = Button(self, bg="orange", bd=12, text="x", padx=38, pady=25,
                                command=lambda: self.buttonClick("*"), font=("Helvetica", 20, "bold"))
        self.Mulbutton.grid(row=4, column=3, sticky=W)

        self.Divbutton = Button(self, bg="orange", bd=12, text="/", padx=39, pady=25,
                                command=lambda: self.buttonClick("/"), font=("Helvetica", 20, "bold"))
        self.Divbutton.grid(row=5, column=3, sticky=W)

        # Equal and Clear
        self.Equalbutton = Button(self, bg="orange", bd=12, text="=", padx=100, pady=25,
                                  command=self.CalculateTask, font=("Helvetica", 20, "bold"))
        self.Equalbutton.grid(row=5, column=1, sticky=W, columnspan=2)

        self.Clearbutton = Button(self, bg="orange", bd=12, text="AC", padx=28, pady=7,
                                  command=self.ClearDisplay, font=("Helvetica", 20, "bold"))
        self.Clearbutton.grid(row=1, sticky=W, columnspan=4)

    # Functions must be OUTSIDE create_widgets
    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.Displaytext(self.answer)
            self.task = str(self.answer)
        except SyntaxError:
            self.Displaytext("Invalid Syntax!")
            self.task = ""
        except ZeroDivisionError:
            self.Displaytext("Cannot divide by 0")
            self.task = ""

    def Displaytext(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


calculator = Tk()
calculator.title("CALCULATOR")
app = Application(calculator)
calculator.resizable(height=False, width=False)
calculator.mainloop()
