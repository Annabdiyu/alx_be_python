monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(monthly_income)
print(monthly_expenses)
print("Your monthly savings are", "$" + str(monthly_savings))
print("Projected savings after one year, with interest, is:", "$" + str(Projected_Savings))
