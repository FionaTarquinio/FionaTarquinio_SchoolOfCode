money_start = float(input("How much money do you have? ($)\n"))
saving_years = float(input("How many years do you want to save over?\n"))
interest_rate = float(input("What is the % interest rate?\n"))/100
money_result = float(money_start * interest_rate * saving_years)
print(f"You will earn ${money_result:.2f} in uncompounded interest")
print(f"Is this more than $10,000? {money_result > 10000}")
