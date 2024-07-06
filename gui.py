import tkinter as tk
from tkinter import messagebox
from bank_account import BankAccount
import database as db

def handle_create_account():
    username = entry_username.get()

    account_number = int(entry_account_number.get())
    initial_balance = float(entry_initial_balance.get())

    
    
    if initial_balance < 1:
        messagebox.showerror("Error", "Initial balance must be at least 1.")
        return
    
    try:
        account = db.create_account(username, account_number, initial_balance)
        messagebox.showinfo("Success", "Account created successfully!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def handle_deposit():
    username = entry_username.get()
    amount = float(entry_amount.get())
    
    try:
        account = db.get_account(username)
        message = account.deposit(amount)
        db.update_balance(username, account.initial_balance)
        messagebox.showinfo("Success", message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def handle_withdraw():
    username = entry_username.get()
    amount = float(entry_amount.get())
    
    try:
        account = db.get_account(username)
        message = account.withdraw(amount)
        db.update_balance(username, account.initial_balance)
        messagebox.showinfo("Success", message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def handle_check_balance():
    username = entry_username.get()
    
    try:
        account = db.get_account(username)
        message = account.check_balance()
        messagebox.showinfo("Balance", message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Bank Account Manager")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Account Number").grid(row=1, column=0)
entry_account_number = tk.Entry(root)
entry_account_number.grid(row=1, column=1)

tk.Label(root, text="Initial Balance").grid(row=2, column=0)
entry_initial_balance = tk.Entry(root)
entry_initial_balance.grid(row=2, column=1)

tk.Label(root, text="Amount").grid(row=3, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=3, column=1)

tk.Button(root, text="Create Account", command=handle_create_account).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Deposit", command=handle_deposit).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Withdraw", command=handle_withdraw).grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Check Balance", command=handle_check_balance).grid(row=7, column=0, columnspan=2)

root.mainloop()

# Close the database connection when the GUI is closed
db.close_connection()


"""
Explanation
bank_account.py: Contains the BankAccount class with methods for depositing, withdrawing, and checking balance.
database.py: Manages the SQLite database, including creating accounts, retrieving account details, and updating balances.
gui.py: Implements the GUI using tkinter and handles user interactions. It imports functions from database.py and uses the BankAccount class from bank_account.py.
"""
