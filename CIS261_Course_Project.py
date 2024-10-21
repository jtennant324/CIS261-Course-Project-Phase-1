#Jessica Tennant
#CIS261
#Course Project Phase 1: Create and Call Functions with Parameters

#This is the function for payroll
def calculate_payroll(hours_worked, hourly_rate, income_tax_rate_percent):
    income_tax_rate = income_tax_rate_percent / 100  # Convert percentage to decimal
    gross_pay = hours_worked * hourly_rate
    income_taxes = gross_pay * income_tax_rate
    net_pay = gross_pay - income_taxes
    return gross_pay, income_taxes, net_pay

# This function displays each employee's payroll information
def display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate_percent, gross_pay, income_taxes, net_pay):
    print(f"\nEmployee: {employee_name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Income Tax Rate: {income_tax_rate_percent:.2f}%")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Taxes: ${income_taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

# This is the main loop for user input
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

            # Adding input validation for income_tax_rate_percent
            while True:
                try:
                    income_tax_rate_percent = float(input(f"Enter income tax rate (as a percentage) for {employee_name}: "))
                    break  # Exit loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter a valid number for the income tax rate.")

            # Calculates payroll
            gross_pay, income_taxes, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate_percent)

            # Displays individual data
            display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate_percent, gross_pay, income_taxes, net_pay)

            # Updates totals
            total_employees += 1
            total_hours_worked += hours_worked
            total_gross_pay += gross_pay
            total_income_taxes += income_taxes
            total_net_pay += net_pay

        except ValueError:
            print("Invalid input. Please enter valid numbers for hours worked, hourly rate, and tax rate.")

    # This displays totals for all employees at user 'end'
    if total_employees > 0:
        print("\nPayroll Summary for All Employees")
        print(f"Total Employees: {total_employees}")
        print(f"Total Hours Worked: {total_hours_worked}")
        print(f"Total Gross Pay: ${total_gross_pay:.2f}")
        print(f"Total Income Taxes: ${total_income_taxes:.2f}")
        print(f"Total Net Pay: ${total_net_pay:.2f}")
    else:
        print("No employees were entered.")

# Run the program
if __name__ == "__main__":
    main()
