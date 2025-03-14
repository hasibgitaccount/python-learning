# 7. Exception Handling:

# A. Handle exceptions like insufficient balance when withdrawing from a BankAccount class.

class InsufficientFundsError(Exception):
    'when trying to withdraw more than what you have'
    pass

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
        try:
            if drawings <= 0:
                raise ValueError('this is not withdrawal')
            if drawings > self.__balance:
                raise InsufficientFundsError('lacking enough funding')

            self.__balance -= drawings
            print(f'withdrawn amount: {drawings}')

        except ValueError as e:
            print(f'cant withdraw more than you have: {e}')

        except InsufficientFundsError as e:
            print(f'Error: {e}')

        except Exception as e:
            print(f'An unexpected error occured: {e}')
        
    
    def checking_balance(self):
        return self.__balance


account = BankAccount(1000)

# Valid deposit
account.deposit(500)

# Valid withdrawal
account.withdrawal(200)

# Insufficient funds error
account.withdrawal(2000)

# Invalid withdrawal (negative amount)
account.withdrawal(-100)

# Check balance
print(f'Balance: {account.checking_balance()}')