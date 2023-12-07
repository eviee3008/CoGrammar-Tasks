''' 
    Finance Calculator, version 2.
    Author: Evie England
    Date: 07/12/23
'''

import math

# Display finance options and ask for user input
print("investment\t- to calculate the amount of interest you'll earn on your investment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan\n")

# Check that finance type input is a valid option
while True:
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if choice != "investment" and choice != "bond":
        print("Invalid input")
    else:
        break

# Define error messages for later use        
error_msg = "Error: data type input invalid"
int_float_msg = ". Please input either an integer or float."
int_msg = ". Please input an integer."

# If-elif block based on user finance option choice

if choice == "investment":
    # If investment is selected, get a number of inputs from the user required to calculate interest
    
    # Use while loops with try-except-else blocks to ensure that inputs of correct data types are inputted
    while True:
        while True:
            try:
                # Get input for deposit amount
                deposit_val = float(input("Please input the amount of money you are depositing: "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_float_msg)
            else:
                break

        while True:
            try:
                # Get input for interest rate
                interest_rate = float(input("Please input the interest rate (you do not need to enter a '%' symbol): "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_float_msg)
            else:
                # Calculate interest rate as a percentage once correct input has been given
                interest_rate = interest_rate / 100
                break

        while True:
            try:
                # Get input for number of years of investment
                years = int(input("Please input the number of years you plan to invest for: "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_float_msg)
            else:
                break

        while True:
            try:
                # Get input for interest type
                interest = input("Please input either 'simple' or 'compound' to indicate which type of interest you would like: ").lower()
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg)
            else:
                # If-else statemnt to ensure that a valid option has been selected
                if interest != "simple" and interest != "compound":
                    print("Invalid input. Please input either 'simple' or 'compound'")
                    continue
                else:
                    break
        break

    # If-elif block based on the interest type chosen by the user
    if interest == "simple":
        # Calculate simple interest, and output final amount after investment
        amount = deposit_val * (1 + (interest_rate * years))
        amount_str = f"Your final amount after {years} years of simple interest will be £{amount:.2f}"
        print(amount_str)

    elif interest == "compound":
        # Calculate compound interest, and output final amount after investment
        amount = deposit_val * math.pow((1 + interest_rate), years)
        amount_str = f"Your final amount after {years} years of compound interest will be £{amount:.2f}"
        print(amount_str)

elif choice == "bond":
    # If bond is selected, get a number of inputs from the user required to calculate payment amount for loan
    
    # Use while loops to ensure that inputs of correct data types are inputted
    while True:
        while True:
            try:
                # Get input for monetary value of the house
                house_val = float(input("Please input the present value of the house (you do not need to enter a currency symbol): "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_float_msg)
            else:
                break

        while True:
            try:
                # Get input for yearly interest rate
                interest_rate = float(input("Please input the interest rate (you do not need to enter a '%' symbol): "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_float_msg)
            else:
                # Calculate interest rate as a percentage once correct input has been given
                interest_rate = interest_rate / 100
                # Calculate monthly interest rate
                monthly_interest_rate = interest_rate / 12
                break

        while True:
            try:
                # Get input for number of years that will be taken to repay the bond
                bond_term_years = int(input("Please input the number of years you plan to take to repay the bond: "))
            except ValueError:
                # Display error message requesting correct data type
                print(error_msg + int_msg)
            else:
                # Calculate the number of months it will take to repay the bond
                bond_term_months = bond_term_years * 12
                break
        break

    # Calculate monthly payment amount for bond
    repayment = (monthly_interest_rate * house_val) / (1 - math.pow((1 + monthly_interest_rate), -bond_term_months))
    print(f"The monthly bond repayment amount will be: £{repayment:.2f}")
    