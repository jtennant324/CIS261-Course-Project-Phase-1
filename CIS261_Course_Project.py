#Jessica Tennant
#CIS261
#Course Project Phase 4: Add Basic Security to the Application

import os


def load_users(file_name):
    user_ids = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                user_id = line.strip().split("|")[0]
                user_ids.append(user_id)
    return user_ids


def add_users(file_name, user_ids):
    print("Starting data entry...\n")
    with open(file_name, "a") as file:
        while True:
            user_id = input("Enter User ID (or type 'End' to stop): ").strip()
            if user_id.lower() == "end":
                break
            if user_id in user_ids:
                print(f"Error: User ID '{user_id}' already exists. Please try again.")
                continue

            password = input("Enter Password: ").strip()
            authorization = input("Enter Authorization Code (Admin/User): ").strip().capitalize()

            if authorization not in ["Admin", "User"]:
                print("Error: Authorization code must be 'Admin' or 'User'. Please try again.")
                continue

            file.write(f"{user_id}|{password}|{authorization}\n")
            user_ids.append(user_id)


def display_users(file_name):
    print("\nDisplaying all user data:")
    print("User ID | Password | Authorization Code")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("No user data found.")


class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization


def login_process(file_name):
    print("\nStarting login process...")
    user_data = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                user_id, password, authorization = line.strip().split("|")
                user_data[user_id] = (password, authorization)

    while True:
        user_id = input("Enter your User ID: ").strip()
        if user_id not in user_data:
            print("Error: User ID not found. Please try again.\n")
            continue

        password = input("Enter your Password: ").strip()
        if user_data[user_id][0] != password:
            print("Error: Incorrect password. Please try again.\n")
            continue

        user_auth = user_data[user_id][1]
        user_login = Login(user_id, password, user_auth)

        print(f"\nWelcome, {user_login.user_id}. Your authorization level is {user_login.authorization}.")
        if user_login.authorization == "Admin":
            print("Admin access granted. You can add and display data.")
            admin_menu(file_name, user_login)
        elif user_login.authorization == "User":
            print("User access granted. You can view data only.")
            user_menu(file_name, user_login)
        break


def admin_menu(file_name, user_login):
    while True:
        print("\nAdmin Menu:")
        print("1 - Add Users")
        print("2 - Display All User Data")
        print("3 - Logout")
        print("4 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_ids = load_users(file_name)
            add_users(file_name, user_ids)
        elif choice == "2":
            display_users(file_name)
        elif choice == "3":
            print("Logging out...")
            break
        elif choice == "4":
            print("Goodbye...")
            input("Press any key to continue...")
            break
        else:
            print("Invalid choice. Please try again.")


def user_menu(file_name, user_login):
    while True:
        print("\nUser Menu:")
        print("1 - Display All User Data")
        print("2 - Logout")
        print("3 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_users(file_name)
        elif choice == "2":
            print("Logging out...\n")
            break
        elif choice == "3":
            print("Goodbye...")
            input("Press any key to continue...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    file_name = "user_data.txt"
    user_ids = load_users(file_name)

    add_users(file_name, user_ids)

    display_users(file_name)

    while True:
        login_process(file_name)


if __name__ == "__main__":
    main()
