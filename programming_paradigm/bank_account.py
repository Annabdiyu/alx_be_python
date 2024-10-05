
class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount  # Add to the balance
        return self.account_balance

    def withdraw(self, amount):

        if amount < self.account_balance:
            self.account_balance -= amount  # Update the balance
            return self.account_balance
        else:
            return "Insufficient funds."

    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")  # Add print to match module 1's output
