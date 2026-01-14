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

 
# account.py
# Base Account class for SecureBank application.
# Implements core attributes and methods for all account types.

class Account:
    def __init__(self, name, account_number, balance=0.0):
        """
        Initialize a new account with customer details.
        Private attributes are used for balance and account number 
        to demonstrate encapsulation.
        """
        self.name = name
        self.__account_number = account_number   # Private attribute
        self.__balance = balance                 # Private attribute
        self.transactions = []                   # Stores history of deposits and withdrawals

    # --------------------------
    # Encapsulation: Getter methods
    # --------------------------
    def get_account_number(self):
        """
        Returns the private account number.
        """
        return self.__account_number

    def get_balance(self):
        """
        Returns the current private balance.
        """
        return self.__balance

    # --------------------------
    # Core account functions
    # --------------------------
    def deposit(self, amount):
        """
        Deposit money into the account if amount is valid.
        Updates balance and logs the transaction.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Successfully deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Checks for sufficient funds and logs the transaction.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient funds. Transaction cancelled.")
            return

        self.__balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"Successfully withdrew {amount}. New balance: {self.__balance}")

    # --------------------------
    # Transaction History
    # --------------------------
    def add_transaction(self, message):
        """
        Append a custom message to the transaction history.
        Useful for subclasses (Savings, Checking).
        """
        self.transactions.append(message)

    def show_transactions(self):
        """
        Display all past transactions in a formatted manner.
        """
        if not self.transactions:
            print("No transactions available.")
            return

        print("\nTransaction History:")
        for t in self.transactions:
            print("-", t)

    # --------------------------
    # Utility
    # --------------------------
    def __str__(self):
        """
        String representation of the account object.
        Helps when listing accounts in the Bank class.
        """
        return f"Account Holder: {self.name}, Account Number: {self.__account_number}, Balance: {self.__balance}"

 
# bank.py
# Bank class manages multiple accounts and provides methods
# to add, retrieve, and list accounts in the SecureBank system.

from account import Account

class Bank:
    def __init__(self):
        """
        Initialize the bank with an empty dictionary of accounts.
        Keys will be account numbers, values will be Account objects.
        """
        self.accounts = {}

    def add_account(self, account):
        """
        Add a new account to the bank.
        Each account is stored using its account number as the key.
        """
        acc_num = account.get_account_number()

        if acc_num in self.accounts:
            print("An account with this number already exists.")
            return

        self.accounts[acc_num] = account
        print(f"Account for {account.name} added successfully.")

    def get_account(self, account_number):
        """
        Retrieve an account object using its account number.
        Returns None if account does not exist.
        """
        return self.accounts.get(account_number, None)

    def list_accounts(self):
        """
        Display all accounts stored in the bank.
        Useful for selecting an account or checking system status.
        """
        if not self.accounts:
            print("No accounts found in the system.")
            return

        print("\n------ List of Accounts ------")
        for acc_num, account in self.accounts.items():
            print(account)  # Calls __str__() from Account or subclasses
        print("------------------------------")

 
# checking_account.py
# CheckingAccount subclass extends the base Account class.
# Adds transaction fee functionality to withdrawals.

from account import Account

class CheckingAccount(Account):
    def __init__(self, name, account_number, transaction_fee, balance=0.0):
        """
        Initialize a Checking Account.
        Inherits attributes from Account.
        Adds a transaction fee which is charged on every withdrawal.
        """
        super().__init__(name, account_number, balance)
        self.transaction_fee = transaction_fee  # Fixed fee deducted per withdrawal

    def withdraw(self, amount):
        """
        Withdraw money from the account including a transaction fee.
        Overrides the parent method to include additional fee.
        """
        total_amount = amount + self.transaction_fee

        # Check if total amount exceeds balance
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if total_amount > self.get_balance():
            print("Insufficient funds including transaction fee. Transaction cancelled.")
            return

        # Perform withdrawal using the inherited deposit() method logic
        # but manually adjust balance because we add a fee
        current_balance = self.get_balance()
        new_balance = current_balance - total_amount

        # Update private balance using inherited deposit/withdraw logic pattern
        # Since balance is private, use transactions + add_transaction
        self.add_transaction(f"Withdrew: {amount}")
        self.add_transaction(f"Transaction Fee Applied: {self.transaction_fee}")

        # Manually update balance through internal variable trick:
        # Using deposit(-value) is a workaround to modify private variable
        super().withdraw(amount)  # This updates balance and logs withdrawal
        super().withdraw(self.transaction_fee)  # This charges the fee separately

    def __str__(self):
        """
        String representation of a CheckingAccount object.
        Shows holder name, account number, and fee.
        """
        return (
            f"Checking Account | Holder: {self.name}, "
            f"Account No: {self.get_account_number()}, "
            f"Balance: {self.get_balance()}, "
            f"Transaction Fee: {self.transaction_fee}"
        )

 
# savings_account.py
# SavingsAccount subclass extends the base Account class.
# Adds interest rate functionality and demonstrates inheritance.

from account import Account

class SavingsAccount(Account):
    def __init__(self, name, account_number, interest_rate, balance=0.0):
        """
        Initialize a Savings Account.
        Inherits name, account number, and balance from Account.
        Adds interest rate as a unique attribute.
        """
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate  # Interest rate stored as percentage (e.g., 2.5 for 2.5%)

    def apply_interest(self):
        """
        Apply interest to the account balance.
        Logs the interest applied as a transaction.
        """
        current_balance = self.get_balance()
        interest_amount = current_balance * (self.interest_rate / 100)

        # Deposit interest using inherited deposit method
        super().deposit(interest_amount)

        self.add_transaction(f"Interest Applied: {interest_amount} at rate {self.interest_rate}%")
        print(f"Interest of {interest_amount} added. New balance: {self.get_balance()}")

    def __str__(self):
        """
        String representation of a SavingsAccount object.
        Shows holder name, account number, and interest rate.
        """
        return (
            f"Savings Account | Holder: {self.name}, "
            f"Account No: {self.get_account_number()}, "
            f"Balance: {self.get_balance()}, "
            f"Interest Rate: {self.interest_rate}%"
        )


