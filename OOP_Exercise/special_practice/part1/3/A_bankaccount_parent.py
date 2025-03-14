# 3. Encapsulation:

# A. Create a BankAccount class with private attributes for balance, and methods for deposit/withdrawal and checking balance.

class BankAccount:

    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance


    def deposit(self, amount):
        if amount <= 0:
            print('please deposit a valid amount')
            return
        self.__balance += amount
        print(f'deposited amount: {amount}')


    def withdrawal(self, drawings):
        if drawings <= 0:
            print('input a valid number that you want to draw')
            return
        if drawings > self.__balance:
            print('you cant draw more than you poseess')
            return
        self.__balance -= drawings
        print(f'withdrawn amount: {drawings}')
        
    
    def checking_balance(self):
        return self.__balance


account1 = BankAccount(1000)

# Deposit 500
account1.deposit(500)

# Withdraw 200
account1.withdrawal(200)

# Check balance
print(f"Current Balance: {account1.checking_balance()}")