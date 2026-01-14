# main.py
# Console-based banking application for SecureBank Ltd
# This file handles all user interaction and menu-driven navigation.

from bank import Bank
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def display_menu():
    """
    Display the main application menu.
    """
    print("\n-------------------------------------")
    print("        SECUREBANK APPLICATION")
    print("-------------------------------------")
    print("1. Create New Account")
    print("2. Select Existing Account")
    print("3. List All Accounts")
    print("4. Exit")
    print("-------------------------------------")

def account_menu():
    """
    Display the menu for account-specific operations.
    """
    print("\n------ Account Menu ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Back to Main Menu")
    print("--------------------------")

def main():
    """
    Main function to run the banking application.
    Handles account creation, selection, and transactions.
    """
    bank = Bank()  # Bank object to manage multiple accounts

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # 1. Create a new account
        if choice == "1":
            name = input("Enter customer name: ").strip()
            acc_num = input("Enter account number: ").strip()

            print("\nSelect Account Type:")
            print("1. Savings Account")
            print("2. Checking Account")
            acc_type = input("Enter choice: ").strip()

            # Create Savings Account
            if acc_type == "1":
                interest = float(input("Enter interest rate: "))
                account = SavingsAccount(name, acc_num, interest)
                bank.add_account(account)
                print("Savings Account created successfully.")

            # Create Checking Account
            elif acc_type == "2":
                fee = float(input("Enter transaction fee: "))
                account = CheckingAccount(name, acc_num, fee)
                bank.add_account(account)
                print("Checking Account created successfully.")

            else:
                print("Invalid account type selected.")

        # 2. Select an existing account
        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            account = bank.get_account(acc_num)

            if account is None:
                print("Account not found.")
            else:
                # Submenu for account operations
                while True:
                    account_menu()
                    sub_choice = input("Enter your choice: ").strip()

                    # Perform deposit
                    if sub_choice == "1":
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)

                    # Perform withdrawal
                    elif sub_choice == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)

                    # Check balance
                    elif sub_choice == "3":
                        print(f"Current Balance: {account.get_balance()}")

                    # Show transaction history
                    elif sub_choice == "4":
                        account.show_transactions()

                    # Return to main menu
                    elif sub_choice == "5":
                        break

                    else:
                        print("Invalid choice.")

        # 3. List all existing accounts
        elif choice == "3":
            bank.list_accounts()

        # 4. Exit application
        elif choice == "4":
            print("Exiting application.")
            break

        # Invalid main menu choice
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

