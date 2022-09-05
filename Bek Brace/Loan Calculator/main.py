from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.geometry("400x200")
        window.mainloop()
        # Create the input boxes
        Label(window, text="Annual Interest Rate").grid(rown=1,column=1)
        Label(window, text="Number of Years").grid(rown=2,column=1)
        Label(window, text="Loan Amount").grid(rown=3,column=1)
        Label(window, text="Monthly Payment").grid(rown=4,column=1)
        Label(window, text="Total Payment").grid(rown=5,column=1)

        # Taking input from the user.
    self.annualInterestRateVar = StringVar()
    Entry(window, textvariable=self.annualInterestRateVar,justify=LEFT).grid(row=1,column=2)

    self.numberOfYearsVar = StringVar()
    Entry(window, textvariable=self.numberOfYearsVar,justify=LEFT).grid(row=2,column=2)

    self.loanAmountVar = StringVar()
    Entry(window, textvariable=self.loanAmountVar,justify=LEFT).grid(row=3,column=2)

    # Output of monthly payment and total payment
    self.monthlyPaymentVar = StringVar()
    lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

    self.totalPaymentVar = StringVar()
    lblTotalPayment = Label(window, textvariable=self.totalPaymentVar, justify=LEFT).grid(row=4, column=2, sticky=E)
    # note: sticky is a property that sticks the label North South East West which means up and down right and left

    win


    LoanCalculator()

