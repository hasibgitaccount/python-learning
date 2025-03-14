# 6. File Handling:

# A. Write methods to save and load object data (like a BankAccount class) to/from a file.

import json

class BankAccount:
    
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        return self.__balance

    def save_to_file(self, filename):
        account_data = {'balance' : self.__balance}
        try:
            with open(filename, 'w') as json_file:
                json.dump(account_data, json_file)
                print(f'account saved to {filename}')
        except Exception as e:
            print(f'Error: {e}')

    @classmethod
    def load_from_file(cls, loading):
        try:
            with open(loading, 'r') as convert_json:
                conversion = json.load(convert_json)
                variable = conversion.get('balance', 0)
                print(f"account loaded from: '{loading}' with balance: {variable}")
                return cls(variable)
        except FileNotFoundError as e:
            print(f'files not found: {e}')
            return None
        except Exception as e:
            print(f'Error: {e}')
            return None
        

account1 = BankAccount(1000)
account1.deposit(500)
account1.save_to_file('account.json')

# Later... load from file!
account2 = BankAccount.load_from_file('account.json')

if account2:
    print(f'Loaded account balance: {account2.check_balance()}')