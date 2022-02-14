import math
import argparse

parser = argparse.ArgumentParser(description="Loan Calculator")

parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

parameters = [args.type, args.payment, args.principal, args.periods, args.interest]
num_of_parameters = 5
for value in parameters:
    if value is None:
        num_of_parameters -= 1

is_negative = False
for value in parameters:
    try:
        if float(value) < 0:
            is_negative = True
    except TypeError:
        continue
    except ValueError:
        continue

if args.type == "annuity":
    if num_of_parameters < 4:
        calc_type = "e"
    elif is_negative:
        calc_type = "e"
    elif args.payment is None:
        calc_type = "a"
    elif args.principal is None:
        calc_type = "p"
    elif args.periods is None:
        calc_type = "n"
    elif args.interest is None:
        calc_type = "i"
    else:
        print("Incorrect parameters")

    if calc_type == "n":
        loan_principal = float(args.principal)
        monthly_payment = float(args.payment)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        months = math.log(monthly_payment / (monthly_payment - (i * loan_principal)), 1 + i)
        Overpayment = (monthly_payment * math.ceil(months)) - loan_principal
        year = math.floor(math.ceil(months) / 12)
        months = math.ceil(months - (year * 12))
        print("It will take " + str(int(year)) + " years and " + str(int(months)) + " months to repay this loan!")
        print("Overpayment = " + str(int(Overpayment)))

    elif calc_type == "a":
        loan_principal = float(args.principal)
        periods = float(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        annuity_payment = loan_principal * (i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)
        annuity_payment = math.ceil(annuity_payment)
        print("Your annuity payment = " + str(int(annuity_payment)) + "!")
        Overpayment = (annuity_payment * periods) - loan_principal
        print("Overpayment = " + str(int(Overpayment)))

    elif calc_type == "p":
        annuity_payment = float(args.payment)
        periods = float(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        loan_principal = int(annuity_payment / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)))
        Overpayment = (annuity_payment * periods) - loan_principal
        print("Your loan principal = " + str(int(loan_principal)) + "!")
        print("Overpayment = " + str(int(Overpayment)))

    else:
        print("Incorrect parameters")

elif args.type == "diff":
    if num_of_parameters < 4:
        print("Incorrect parameters")
    elif is_negative:
        print("Incorrect parameters")
    elif args.payment is not None:
        print("Incorrect parameters")
    elif args.interest is None:
        print("Incorrect parameters")
    else:
        loan_principal = float(args.principal)
        periods = float(args.periods)
        loan_interest = float(args.interest)
        i = loan_interest / (12 * 100)
        payment_sum = 0
        for current_month in range(int(periods)):
            D_m = loan_principal/periods + i * (loan_principal - (loan_principal * current_month)/periods)
            D_m = int(math.ceil(D_m))
            payment_sum += D_m
            print("Month " + str(current_month + 1) + ": payment is " + str(D_m))
        print("")

        Overpayment = payment_sum - loan_principal
        print("Overpayment = " + str(int(Overpayment)))

else:
    print("Incorrect parameters")
