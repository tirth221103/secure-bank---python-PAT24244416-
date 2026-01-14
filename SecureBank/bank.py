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

