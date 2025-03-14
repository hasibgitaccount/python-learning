# 3. Unit Testing and Testing Libraries:

# A. Learn unit testing for your classes (use unittest or pytest) and write tests for various OOP implementations like BankAccount or Person.

import unittest
from sample import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        acc = BankAccount()
        result = acc.deposit(100)
        self.assertTrue(result)
        self.assertEqual(acc.get_balance(), 100)
    
    def test_withdraw_success(self):
        acc = BankAccount(200)
        result = acc.withdraw(100)
        self.assertTrue(result)
        self.assertEqual(acc.get_balance(), 100)

    def test_get_balance(self):
        acc = BankAccount(500)
        self.assertEqual(acc.get_balance(), 500)

    def test_withdraw_insufficient(self):
        acc = BankAccount(50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)


if __name__ == '__main__':
    unittest.main()