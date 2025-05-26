##Prompt the user for financial details

monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

##calculate monthly savings
monthly_savings = int(monthly_income) - int(monthly_expense)
print("Your monthly savings is:", (monthly_savings))


##project annual savings
projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05

print("Projected savings after one year, with interest, is:", (projected_savings))