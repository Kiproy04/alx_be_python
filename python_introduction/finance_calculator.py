##Prompt the user for financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

##calculate monthly savings
monthly_savings = monthly_income - monthly_expense
print("Your total monthly savings is:", monthly_savings)


##project annual savings
annual_rate = 0.005
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * annual_rate))

print("Projected savings after one year, with interest, is:", projected_savings)