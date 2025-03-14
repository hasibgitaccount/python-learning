# 3. Encapsulation:

# B. Implement basic getter and setter methods for encapsulation.

class BankAccount:

    def __init__(self, initial_balance = 0):
        self.__balance = initial_balance


    @property
    def balance(self):
        return self.__balance
    

    @balance.setter
    def balance(self, new_balance):
        if new_balance <= 0:
            print('balance has to be positive')
            return
        self.__balance = new_balance
        print(f'updated balance: {self.__balance}')


    def deposit(self, amount):
        if amount < 0:
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
        
    
account1 = BankAccount(1000)

# Check current balance
print("Initial balance:", account1.balance)

# Deposit 500
account1.deposit(500)

# Withdraw 300
account1.withdrawal(300)

# Try to withdraw more than balance
account1.withdrawal(2000)

# Set balance to 2000 using setter
account1.balance = 2000

# Try to set a negative balance
account1.balance = -100

# Final balance check
print("Final balance:", account1.balance)

