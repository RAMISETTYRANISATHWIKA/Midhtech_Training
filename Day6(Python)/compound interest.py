while True:
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time (in years): "))
        break
    except ValueError:
        print("Please enter valid numbers.")
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print("Compound Interest:", round(compound_interest, 2))
print("Total Amount:", round(amount, 2))