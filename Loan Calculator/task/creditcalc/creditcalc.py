import math
from math import ceil
def welcome():
    print("Enter the loan principal:")
    amount = int(input())
    print("What do you want to calculate?")
    print("type 'm for number of monthly payments,")
    print("type 'p' for the monthly payment:")
    operation = input()

    if operation == 'm':
        print("Enter the monthly payment:")
        payment = int(input())
        number_of_months(amount, payment)
    elif operation == 'p':
        print("Enter the number of months:")
        months = int(input())
        number_of_payments(amount, months)

def number_of_months(amount, payment):
    result = amount / payment
    if int(result) == 1:
        print("It will take {} month to repay the loan".format(int(result)))

    elif result % 2 != 0:
        print("It will take {} months to repay the loan".format(math.ceil(result)))
    else:
        print("It will take {} months to repay the loan".format(int(result)))

def number_of_payments(amount, months):
    result = amount / months

    if result % 2 != 0:

        lastpayment = amount - (months - 1) * math.ceil(result)
        print("Your monthly payment = {} and the last payment = {}.".format(math.ceil(result), lastpayment))
    else:
        print("Your monthly payment = {}".format(result))
welcome()
