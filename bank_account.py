class BankAccount:
    def __init__(self, account_number, initial_balance):
        #if i put assert it raise an error in check balance
        #assert initial_balance >= 1, f"initial_balance {initial_balance} is less than 1"
        self.account_number = account_number
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.initial_balance += amount
        return f"Deposited amount = {amount} | Total balance = {self.initial_balance}"
    
    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount
            return f"Withdrew amount = {amount} | Total balance = {self.initial_balance}"
        return "You don't have enough balance!"
    
    def check_balance(self):
        return f"Account {self.account_number} has a balance of {self.initial_balance}"
