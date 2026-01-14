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


