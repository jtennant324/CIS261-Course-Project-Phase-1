# Function to calculate payroll
def calculate_payroll(hours_worked, hourly_rate, income_tax_rate):
    gross_pay = hours_worked * hourly_rate
    income_taxes = gross_pay * income_tax_rate
    net_pay = gross_pay - income_taxes
    return gross_pay, income_taxes, net_pay

# Function to display individual employee payroll information
def display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate, gross_pay, income_taxes, net_pay):
    print(f"\nEmployee: {employee_name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Income Tax Rate: {income_tax_rate * 100:.2f}%")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Taxes: ${income_taxes:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

# Main loop for input and processing
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
            income_tax_rate = float(input(f"Enter income tax rate (as a decimal) for {employee_name}: "))

            gross_pay, income_taxes, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate)

            display_employee_data(employee_name, hours_worked, hourly_rate, income_tax_rate, gross_pay, income_taxes, net_pay)

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

