import sqlite3
from bank_account import BankAccount

conn = sqlite3.connect('bank_accounts.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        username TEXT PRIMARY KEY,
        account_number INTEGER,
        balance REAL
    )
''')
conn.commit()

def create_account(username, account_number, initial_balance):
    try:
        c.execute('INSERT INTO accounts (username, account_number, balance) VALUES (?, ?, ?)', 
                  (username, account_number, initial_balance))
        conn.commit()
        return BankAccount(account_number, initial_balance)
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists!")

def get_account(username):
    c.execute('SELECT account_number, balance FROM accounts WHERE username = ?', (username,))
    result = c.fetchone()
    if result:
        return BankAccount(result[0], result[1])
    else:
        raise ValueError("Account not found!")

def update_balance(username, new_balance):
    c.execute('UPDATE accounts SET balance = ? WHERE username = ?', (new_balance, username))
    conn.commit()

def close_connection():
    conn.close()
