import math
from math import ceil

def welcome():
    print("What do you want to calculate?")
    print("type 'n' for number of monthly payments,")
    print("type 'a' for the monthly payment:")
    print("type 'p' for loan principal:")
    operation = input()

    if operation == 'n':
        print("Enter the loan principal:")
        principal = int(input())
        print("Enter the monthly payment:")
        monthly_payment = int(input())
        print("Enter the loan interest")
        loan_interest = float(input()) / 12 / 100
        number_of_payments(principal, monthly_payment, loan_interest)
    elif operation == 'a':
        print("Enter the loan principal:")
        principal = int(input())
        print("Enter the number of periods:")
        periods = int(input())
        print("Enter the loan interest:")
        loan_interest = float(input()) / 12 / 100

        annuity(principal, periods, loan_interest)
    elif operation == 'p':
        print("Enter the annuity payment:")
        annuity_payment = float(input())
        print("Enter the number of periods:")
        periods = int(input())
        print("Enter the loan interest:")
        loan_interest = float(input()) / 12 / 100
        loan_principal(annuity_payment, periods, loan_interest)

#

def number_of_payments(principal, monthly_payment, loan_interest):
    result =  (monthly_payment / (monthly_payment - loan_interest * principal))
    months = math.log(result, (1 + loan_interest))
    years = math.ceil(months) / 12
    month = math.ceil(months) % 12


    if months % 12 == 0:
        if years == 1:
            print(f"It will take {int(years)} year to repay this loan!")
        else:
            print(f"It will take {int(years)} years to repay this loan!")
    else:
        if years == 1:
            y = "year"
        else:
            y = "years"
        if month == 1:
            m = "month"
        else:
            m = "months"
        print(f"It will take {math.ceil(int(years))} {y} and {math.ceil(int(month))} {m} to repay this loan!")




    # if result % 2 != 0:
    #     lastpayment = amount - (months - 1) * math.ceil(result)
    #     print("Your monthly payment = {} and the last payment = {}.".format(math.ceil(result), lastpayment))
    # else:
    #     print("Your monthly payment = {}".format(result))



def annuity(principal, periods, loan_interest):
    result = principal * (((loan_interest * (1 + loan_interest)**periods)) / ((1 + loan_interest)**periods - 1))
    print(f"Your monthly payment = {math.ceil(result)}!")

def loan_principal(annuity_payment, periods, loan_interest):
    result = annuity_payment / ((loan_interest * (1 + loan_interest)**periods) / (((1 + loan_interest)**periods) - 1))
    print(f"Your loan principal = {int(result)}!")

welcome()

#   def number_of_months(amount, payment):
#     result = amount / payment
#     if int(result) == 1:
#         print("It will take {} month to repay the loan".format(int(result)))
#
#     elif result % 2 != 0:
#         print("It will take {} months to repay the loan".format(math.ceil(result)))
#     else:
#         print("It will take {} months to repay the loan".format(int(result)))