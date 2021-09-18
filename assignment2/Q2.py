def months_to_buy(total_cost, portion_saved, annual_salary, semi_annual_raise):
    portion_down_payment = 0.25*total_cost
    months = 0
    current_savings = 0
    raised_month = 6
    monthly_salary = (annual_salary/12)
    while (current_savings < portion_down_payment):
        if (months == raised_month):
            annual_salary += annual_salary*semi_annual_raise
            monthly_salary = (annual_salary/12)
            raised_month += 6
        current_savings += monthly_salary*portion_saved
        months += 1
    return months

salary = float(input("Enter your annual salary: "))
percent_saved_decimal = float(input("Enter the percent of your salary to save, as a decimal: "))
total = float(input("Enter the cost of your dream home: "))
semi_raise_decimal = float(input("Enter the semiannual raise, as a decimal: "))


result = months_to_buy(total,percent_saved_decimal,salary,semi_raise_decimal)
print(f"Number of months: {result}")