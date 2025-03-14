# 1. Class Methods and Static Methods:

# B. Use a static method to validate an account number format.

class Bank:

    def __init__(self, name, age, gender, balance = 0):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__balance = balance


    @classmethod
    def create_account(cls, name, age, gender, balance = 0):
        return cls(name, age, gender, balance)
    

    def __str__(self):
        return (f'account holder: {self.__name},'
                f'age: {self.__age},'
                f'gender: {self.__gender},'
                f'balance: {self.__balance}')
    
    @staticmethod
    def validate_account_number(x):
        if isinstance(x, str) and x.isdigit() and len(x) == 8:
            return True
        return False
    

print(Bank.validate_account_number("12345678")) 
print(Bank.validate_account_number("12ABC678")) 
print(Bank.validate_account_number("123456"))