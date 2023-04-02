# Purpose: Calculate the total interest paid for a loan and the total amount paid at the end of the loan.
# Author: Michael Lee
# Date: February 15, 2023

def totalInterestPaid(loanValue, annualRate, numberOfPayments):
   # finds amount owed per month
    monthlyRate = annualRate / 12 / 100
    monthlyPayment = loanValue * (monthlyRate / (1 - (1 + monthlyRate) ** (-numberOfPayments)))
    balance = loanValue
    totalInterest = 0
    # finds the total amount of interest owed
    for i in range(numberOfPayments):
        interest = balance * monthlyRate
        principal = monthlyPayment - interest 
        balance -= principal
        totalInterest += interest
    return totalInterest

if __name__ == "__main__":
# total loan amount (u)
    print("Balance due")
    while True:
        try:
            loanAmount = float(input("Enter a value between 1000.00 and 100000.00: "))
            if loanAmount < 1000.00 or loanAmount > 100000.00:
                print("Error: value is out of bounds.")
            else: 
                break
        except ValueError:
            print("Invalid input. A numeric value was expected.")
# amount of payments (u)
    print("\nTotal Number of Payments")
    while True:
        try:
            numberOfPayments = int(input("Enter a value between 12 and 120: "))
            if numberOfPayments < 12 or numberOfPayments > 120:
                print("Error: value is out of bounds.")
            else: 
                break
        except ValueError:
            print("Invalid input. An integer value was expected.")
        
# interest rate (u)
    print("\nInterest Rate")
    while True:
        try:
            annualRate = float(input("Enter a value between 1.60 and 18.50: "))
            if annualRate < 1.60 or annualRate > 18.50:
                print("Error: value is out of bounds.")
            else:
                break
        except ValueError:
            print("Invalid input. A numeric value was expected.")

    interestPaid = totalInterestPaid(loanAmount, annualRate, numberOfPayments)
    totalPaid = interestPaid + loanAmount
    # output
    print("\nLoan Amount:   ${:.2f}".format(loanAmount))
    print("Interest Rate: {:.2f}%".format(annualRate))
    print("Payments Made: {}".format(numberOfPayments))
    print("Interest Paid: ${:.2f}".format(interestPaid))
    print("Total Paid:    ${:.2f}".format(totalPaid))
