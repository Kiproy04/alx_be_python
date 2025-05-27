##Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expenses: "))

##calculate monthly savings
monthly_savings = monthly_income - monthly_expense
print("Your monthly savings is:", monthly_savings)


##project annual savings
projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05

print("Projected savings after one year, with interest, is:", projected_savings)