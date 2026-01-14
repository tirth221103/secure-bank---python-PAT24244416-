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
