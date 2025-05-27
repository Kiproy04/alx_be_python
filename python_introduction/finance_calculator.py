##Prompt the user for financial details

Monthly_income = float(input("Enter your monthly income: "))
Monthly_expense = float(input("Enter your total monthly expenses: "))

##calculate monthly savings
Monthly_savings = Monthly_income - Monthly_expense
print("Your monthly savings is:", (Monthly_savings))


##project annual savings
projected_savings = (Monthly_savings * 12 + (Monthly_savings * 12 * 0.05))

print("Projected savings after one year, with interest, is:", (projected_savings))