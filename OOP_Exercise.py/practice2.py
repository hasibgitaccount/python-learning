class BankAccount:
    def __init__(self, account_holder, balance = 0):

        assert balance >= 0, f'balance cant be less than zero'

        self.account_holder = account_holder
        self.balance = balance
        self.initial_balance = balance
        self.sum_deposit = 0
        self.sum_withdraw = 0


    def deposit_amount(self, money):
        self.sum_deposit += money
        self.balance += money
        return self.balance

    
    def withdraw_amount(self, money):
        if money > self.balance:
            print('insufficient amount of money for withdrawal')
        else:
            self.sum_withdraw += money
            self.balance -= money
            return self.balance

    def display_balance(self):
        return self.balance
    

    def __str__(self):
        return (f'account holder name: {self.account_holder}\n'
                f'initial balance: {self.initial_balance}\n'
                f'total deposit amount: {self.sum_deposit}\n'
                f'total withdraw amount: {self.sum_withdraw}\n'
                f'final balance: {self.display_balance()}'
                )


acc1 = BankAccount('john doe', 500)
acc1.deposit_amount(200)
acc1.withdraw_amount(100)
print(acc1.display_balance())
print(acc1)