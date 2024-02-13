money_start = float(input("How much money do you have? ($)\n"))
saving_years = float(input("How many years do you want to save over?\n"))
interest_rate = float(input("What is the % interest rate?\n"))/100
money_result = money_start * interest_rate * saving_years
# money_result is the interest earned without compounding.

print(f"You will earn ${money_result:.2f} in uncompounded interest.\n")
print(f"Will you have more than $10,000 with uncompounded interest after {saving_years} years?\n{(money_result + money_start) > 10000}\n")

# the following lines are to calculate compound interest
compound_periods = int(input("How many times per year is interest added to your savings?\n"))
compound_money_result = money_start * ((1 + interest_rate / compound_periods)**(compound_periods * saving_years) - 1)
# compound_money_result is the compound interest calculated using the compound periods specified by the user.

print(f"You will earn ${compound_money_result:.2f} in compound interest.\n")
print(f"Will you have more than $10,000 with compound interest after {saving_years} years?\n{(compound_money_result + money_start) > 10000}\n")