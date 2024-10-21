#Jessica Tennant
#CIS261
#Course Project Phase 1: Create and Call Functions with Parameters

# This is the function to calculate payroll
def calculate_payroll(hours_worked, hourly_rate, income_tax_rate_percent):
    gross_pay = hours_worked * hourly_rate
    income_tax_rate = income_tax_rate_percent / 100  # Convert percentage to decimal
    income_taxes = gross_pay * income_tax_rate
    net_pay = gross_pay - income_taxes
    return gross_pay, income_taxes, net_pay

# This is the function to display individual employee payroll information
def display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate_percent, gross_pay, income_taxes, net_pay):
    print(f"\nEmployee: {employee_name}")
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {income_tax_rate_percent:.2f}%")
    print(f"Income Taxes: ${income_taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

# This is the main loop processing end totals
def main():
    total_employees = 0
    total_hours_worked = 0
    total_gross_pay = 0
    total_income_taxes = 0
    total_net_pay = 0

    while True:
        employee_name = input("Enter employee's name (or type 'End' to finish): ")
        if employee_name.lower() == 'end':
            break

        try:
            hours_worked = float(input(f"Enter hours worked for {employee_name}: "))
            hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
            income_tax_rate_percent = float(input(f"Enter income tax rate (as a percentage) for {employee_name}: "))

            gross_pay, income_taxes, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate_percent)

            display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate_percent, gross_pay, income_taxes, net_pay)

            # Update totals
            total_employees += 1
            total_hours_worked += hours_worked
            total_gross_pay += gross_pay
            total_income_taxes += income_taxes
            total_net_pay += net_pay

        except ValueError:
            print("Invalid input. Please enter numbers for hours worked, hourly rate, and tax rate.")

    # Display totals for all employees
    if total_employees > 0:
        print("\nSummary of all employees:")
        print(f"Total number of employees: {total_employees}")
        print(f"Total hours worked: {total_hours_worked:.2f}")
        print(f"Total gross pay: ${total_gross_pay:.2f}")
        print(f"Total income Taxes: ${total_income_taxes:.2f}")
        print(f"Total net pay: ${total_net_pay:.2f}")
    else:
        print("No employees were entered.")

# Run the program
if __name__ == "__main__":
    main()
