#Jessica Tennant
#CIS261
#Course Project Phase 2: Using Lists and Dictionaries to Store and Retrieve Data

from datetime import datetime

# Function to input and validate the from date and to date for the hours worked
def input_dates():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            to_date = input("Enter to date (mm/dd/yyyy): ")

            # Validate that the dates are in the correct format and are real dates
            from_date_obj = datetime.strptime(from_date, "%m/%d/%Y")
            to_date_obj = datetime.strptime(to_date, "%m/%d/%Y")

            # Check if the 'to_date' is after or the same as 'from_date'
            if to_date_obj < from_date_obj:
                print("The 'to date' cannot be earlier than the 'from date'. Please re-enter.")
                continue

            return from_date, to_date  # Return the dates if they're valid

        except ValueError:
            print("Invalid date format or value. Please use mm/dd/yyyy formatting.")

# Function to input employee details to add to list
def input_employee_data():
    from_date, to_date = input_dates()
    employee_name = input("Enter employee name: ")
    try:
        hours_worked = float(input(f"Enter hours worked for {employee_name} from {from_date} to {to_date}: "))
        hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
        income_tax_rate = float(input(f"Enter income tax rate (as a percentage) for {employee_name}: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours, rate, and tax.")
        return None  # Return None indicates invalid entry
    
    return {
        "from_date": from_date,
        "to_date": to_date,
        "employee_name": employee_name,
        "hours_worked": hours_worked,
        "hourly_rate": hourly_rate,
        "income_tax_rate": income_tax_rate
    }

# Function to calculate payroll for employee
def calculate_payroll(employee_data):
    gross_pay = employee_data["hours_worked"] * employee_data["hourly_rate"]
    income_tax = gross_pay * (employee_data["income_tax_rate"] / 100)
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Function to process and display individual employee data from list
def process_and_display_employee_data(employee_list):
    totals = {
        "total_employees": 0,
        "total_hours_worked": 0,
        "total_gross_pay": 0,
        "total_income_tax": 0,
        "total_net_pay": 0
    }

    for employee_data in employee_list:
        gross_pay, income_tax, net_pay = calculate_payroll(employee_data)
        
        # Display individual employee data
        print(f"Employee Payroll Data:")
        print(f"From Date: {employee_data['from_date']}")
        print(f"To Date: {employee_data['to_date']}")
        print(f"Employee Name: {employee_data['employee_name']}")
        print(f"Hours Worked: {employee_data['hours_worked']:.2f}")
        print(f"Hourly Rate: ${employee_data['hourly_rate']:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {employee_data['income_tax_rate']:.2f}%")
        print(f"Income Taxes: ${income_tax:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print("\n-------------------------\n")  # Separator for readability

        # Update totals
        totals["total_employees"] += 1
        totals["total_hours_worked"] += employee_data["hours_worked"]
        totals["total_gross_pay"] += gross_pay
        totals["total_income_tax"] += income_tax
        totals["total_net_pay"] += net_pay

    return totals

# Function to display summary totals from a dictionary object
def display_totals(totals):
    print("Summary of All Employees:")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours Worked: {totals['total_hours_worked']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Income Taxes: ${totals['total_income_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

# Main function to run the program
def main():
    employee_list = []
    while True:
        employee_data = input_employee_data()
        if employee_data is None:
            continue  # Skip to the next loop iteration if entry was invalid
        employee_list.append(employee_data)

        # Ask if the user wants to add another employee and add a newline afterward
        cont = input("Add another employee? (yes/no): ")
        print()  # Adds a blank line for readability after each employee entry
        if cont.lower() != 'yes':
            break

    totals = process_and_display_employee_data(employee_list)
    display_totals(totals)

# Run the program
if __name__ == "__main__":
    main()
