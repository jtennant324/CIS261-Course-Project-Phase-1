#Jessica Tennant
#CIS261
#Course Project Phase 3: Using Files to Store and Retrieve Data from datetime import datetime

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

# Function to input employee details and write to file
def input_employee_data(file_name):
    from_date, to_date = input_dates()
    employee_name = input("Enter employee name: ")
    try:
        hours_worked = float(input(f"Enter hours worked for {employee_name} from {from_date} to {to_date}: "))
        hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
        income_tax_rate = float(input(f"Enter income tax rate (as a decimal, e.g., 0.15 for 15%): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hours, rate, and tax.")
        return None  # Return None indicates invalid entry

    # Write the data to the file in pipe-delimited format
    with open(file_name, "a") as file:
        file.write(f"{from_date}|{to_date}|{employee_name}|{hours_worked}|{hourly_rate}|{income_tax_rate}\n")

    return {
        "from_date": from_date,
        "to_date": to_date,
        "employee_name": employee_name,
        "hours_worked": hours_worked,
        "hourly_rate": hourly_rate,
        "income_tax_rate": income_tax_rate
    }

# Function to calculate payroll for employee
def calculate_payroll(hours_worked, hourly_rate, income_tax_rate):
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * income_tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Function to generate a report from the file
def generate_report(file_name):
    while True:
        from_date_filter = input("Enter From Date for the report (mm/dd/yyyy) or 'All' for all records: ")
        if from_date_filter.lower() == "all":
            break
        try:
            # Validate if the provided from_date is in the correct format
            datetime.strptime(from_date_filter, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy.")

    totals = {
        "total_employees": 0,
        "total_hours_worked": 0,
        "total_gross_pay": 0,
        "total_income_tax": 0,
        "total_net_pay": 0
    }

    print("\nEmployee Records:")
    records_found = False  # Track if any matching records are found

    try:
        with open(file_name, "r") as file:
            for line in file:
                from_date, to_date, employee_name, hours_worked, hourly_rate, income_tax_rate = line.strip().split("|")
                hours_worked = float(hours_worked)
                hourly_rate = float(hourly_rate)
                income_tax_rate = float(income_tax_rate)

                # Only process records matching the exact from_date_filter
                if from_date_filter.lower() == "all" or from_date == from_date_filter:
                    records_found = True
                    gross_pay, income_tax, net_pay = calculate_payroll(hours_worked, hourly_rate, income_tax_rate)

                    # Print employee record in a single line
                    print(f"From: {from_date}, To: {to_date}, Name: {employee_name}, "
                          f"Hours: {hours_worked:.1f}, Pay Rate: {hourly_rate:.2f}, "
                          f"Gross Pay: {gross_pay:.2f}, Tax: {income_tax:.2f}, Net Pay: {net_pay:.2f}")

                    # Update totals
                    totals["total_employees"] += 1
                    totals["total_hours_worked"] += hours_worked
                    totals["total_gross_pay"] += gross_pay
                    totals["total_income_tax"] += income_tax
                    totals["total_net_pay"] += net_pay

        if not records_found:
            print(f"No records found for From Date: {from_date_filter}")

    except FileNotFoundError:
        print("No data file found. Please add employee records first.")

    # Display totals only if records are found
    if records_found:
        display_totals(totals)

# Function to display summary totals from a dictionary object
def display_totals(totals):
    print("\nTotals:")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours Worked: {totals['total_hours_worked']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Income Taxes: ${totals['total_income_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

# Function for adding employees with immediate continuation prompt
def add_employee_data(file_name):
    while True:
        input_employee_data(file_name)
        cont = input("Would you like to add another employee? (y/n): ").strip().lower()
        if cont != "y":
            break

# Main function with menu
def main():
    file_name = "employee_data.txt"
    while True:
        print("\nSelect an option:")
        print("1 - Add Employee Data")
        print("2 - Display Records")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee_data(file_name)
        elif choice == "2":
            generate_report(file_name)
        elif choice == "3":
            input("Press any key to continue...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

# Run the program
if __name__ == "__main__":
    main()
