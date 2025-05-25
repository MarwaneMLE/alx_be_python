monthly_income = float(input("Enter your monthly income: "))
monthly_expences = float(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income - monthly_expences
annual_savings = monthly_savings * 12
project_savings = annual_savings + (annual_savings * 0.05)
print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${int(project_savings)}.")
