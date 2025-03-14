# 1. Class Methods and Static Methods:

# A. Implement a class method to create an Account in a banking system.

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
                


# Create an account using the class method
account_1 = Bank.create_account("John Doe", 30, "Male", 5000)

# Let's print the object
print(account_1)

