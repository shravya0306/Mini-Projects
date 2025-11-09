from tkinter import *  #import the whol module

class CurrencyConverter:    #create class

    def __init__(self):     #special method in pyhton class
        window=Tk()         #create application window
        window.title("Currency Converter")     #add title
        window.configure(bg="light pink")      #add background color

        
        #adding Label widgets to application window
        Label(window,font="Helvetica 12 bold",bg="black",fg="white",text="Amount to convert").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="black",fg="white",text="Conversion rate").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="black",fg="white",text="Converted amount").grid(row=3,column=1,sticky=W)


        #create objects and add entry functions
        self.AmnttoConvertVar=StringVar()
        Entry(window,textvariable=self.AmnttoConvertVar,justify=RIGHT).grid(row=1,column=2)
        self.ConversionRateVar=StringVar()
        Entry(window,textvariable=self.ConversionRateVar,justify=RIGHT).grid(row=2,column=2)
        self.ConvertedAmntVar=StringVar()
        lblConvertedAmnt=Label(window,font="Helvetica 12 bold",bg="black",fg="white",textvariable=self.ConvertedAmntVar).grid(row=3,column=2,sticky=E)



        #create convert and clear buttons

        bt1=Button(window,text="Convert",font="Helvetica 12 bold",bg="red",fg="white",command=self.Converted_Amount).grid(row=4,column=2,sticky=E)
        bt2=Button(window,text="Clear",font="Helvetica 12 bold",bg="red",fg="white",command=self.delete_all).grid(row=4,column=6,padx=25,pady=25,sticky=E)

        
        window.mainloop()
        
    #Function to do the conversion
    def Converted_Amount(self):
        amt=float(self.ConversionRateVar.get())
        ConvertedAmntVar=float(self.AmnttoConvertVar.get())*amt
        self.ConvertedAmntVar.set(format(ConvertedAmntVar,'10.2f'))

    #Function to clear all
    def delete_all(self):
        self.AmnttoConvertVar.set("")
        self.ConversionRateVar.set("")
        self.ConvertedAmntVar.set("")

CurrencyConverter()

        
        
        
