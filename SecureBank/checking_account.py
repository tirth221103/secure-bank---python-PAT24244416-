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


