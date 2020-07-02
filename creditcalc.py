import argparse
import math


# print("""What do you want to calculate?
# type \"n\" - for count of months,
# type \"a\" - for annuity monthly payment,
# type \"p\" - for credit principal:
# """)
# what_person_wants_to_calculate = "l"
# if what_person_wants_to_calculate == "p":
#     pass
#
#
def principal_calculator(annuity_monthly_payment, count_of_periods, credit_interest_in_percent):
    nominal_interest_rate = credit_interest_in_percent / 1200
    credit_principal = annuity_monthly_payment / (
            (nominal_interest_rate * (1 + nominal_interest_rate) ** count_of_periods) / (
            (1 + nominal_interest_rate) ** count_of_periods - 1))
    overpayment = annuity_monthly_payment * count_of_periods - credit_principal
    return f"Your credit_principal = {credit_principal:.2f}!\nOverpayment = {overpayment:.0f}"


#
#
# if what_person_wants_to_calculate == "a":
#     pass
# print("Enter credit principal:")
def annuity_payment(credit_principal, periods, credit_interest_in_percent):
    nominal_interest_rate = credit_interest_in_percent / 1200
    annuity_payment = math.ceil(
        credit_principal * ((1 + nominal_interest_rate) ** periods * nominal_interest_rate) / (
                (1 + nominal_interest_rate) ** periods - 1))
    overpayment = annuity_payment * periods - credit_principal
    return f"Your annuity payment = {annuity_payment}!\nOverpayment = {overpayment:.0f}"


# print(f"Your annuity payment = {annuity_payment}!")
def length_of_time(credit_principal, annuity_monthly_payment, credit_interest_in_percent):
    nominal_interest_rate = credit_interest_in_percent / 1200
    number_of_months = math.ceil(
        math.log((annuity_monthly_payment / (annuity_monthly_payment - nominal_interest_rate * credit_principal)),
                 (1 + nominal_interest_rate)))
    number_of_years = number_of_months // 12
    remaining_number_of_months = number_of_months % 12
    overpayment = number_of_months * annuity_monthly_payment - credit_principal
    if number_of_years == 0 and remaining_number_of_months == 1:
        return f"You need 1 month to repay this credit!\nOverpayment = {overpayment:.0f}"
    elif number_of_years == 0 and remaining_number_of_months != 1:
        return f"You need {number_of_months} months to repay this credit!\nOverpayment = {overpayment}"
    elif remaining_number_of_months == 0 and number_of_years == 1:
        return f"You need 1 year to repay this credit!\nOverpayment = {overpayment:.0f}"
    elif remaining_number_of_months == 0 and number_of_years != 1:
        return f"You need {number_of_years} years to repay this credit!\nOverpayment = {overpayment:.0f}"
    elif remaining_number_of_months == 1 and number_of_years != 1:
        return f"You need {number_of_years} years and 1 month to repay this credit!\nOverpayment = {overpayment:.0ft}"
    elif remaining_number_of_months != 1 and number_of_years != 1:
        return (
            f"You need {number_of_years} years and {number_of_months} months to repay this credit!\nOverpayment = {overpayment:.0f}")


def differentiable_payment(credit_principal, credit_interest_in_percent, periods, current_period):
    nominal_interest_rate = credit_interest_in_percent / 12 / 100
    mth_differentiated_payment = math.ceil(credit_principal / periods + nominal_interest_rate * (
            credit_principal - ((credit_principal * (current_period - 1)) / periods)))
    return mth_differentiated_payment


def Main():
    global time
    global principal
    parser = argparse.ArgumentParser()
    parser.add_argument("-type", "--type", help="enter type of calculation", type=str, )
    parser.add_argument("-payment", "--payment", help="Enter the monthly payment", type=float, )
    parser.add_argument("-principal", "--principal", help="Enter the credit principal", type=float)
    parser.add_argument("-interest", "--interest", help="Enter the monthly interest", type=float)
    parser.add_argument("-periods", "--periods", help="Enter the number of periods", type=int)
    args = parser.parse_args()
    time = 0

    if not args.type:
        print("Incorrect parameters")

    elif args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters")
    elif args.type == "annuity" and args.principal and args.payment and args.interest:
        if args.principal > 0 and args.payment > 0 and args.interest > 0:
            time = length_of_time(args.principal, args.payment, args.interest)
            print(time)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity" and args.periods and args.payment and args.interest:
        if args.periods > 0 and args.payment > 0 and args.interest > 0:
            principal = principal_calculator(args.payment, args.periods, args.interest)
            print(principal)
        else:
            print("Incorrect parameters")
    elif args.type == "annuity" and args.periods and args.principal and args.interest:
        if args.periods > 0 and args.principal > 0 and args.interest > 0:
            annuity = annuity_payment(args.principal, args.periods, args.interest)
            print(annuity)
        else:
            print("Incorrect parameters")
    elif args.type == "diff" and args.periods and args.principal and args.interest:
        if args.periods > 0 and args.principal > 0 and args.interest > 0:
            total = 0
            for i in range(1, args.periods + 1):
                amount_paid = differentiable_payment(args.principal, args.interest, args.periods, i)
                print(f"Month {i}: paid out {amount_paid}")
                total += amount_paid
            overpayment = total - args.principal
            print(f"\nOverpayment: {overpayment:.0f}")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")


if __name__ == '__main__':
    Main()
