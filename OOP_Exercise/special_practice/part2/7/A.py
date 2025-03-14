# 7. Strategy Pattern (ML Relevance):

# A. Implement a PaymentStrategy interface with different payment methods (like credit card and PayPal). In ML, this can relate to various model selection strategies.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass



class CreditCardPayment(PaymentStrategy):

    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number

    def pay(self, amount):
        print(f'paying ${amount} using credit card.')
        print(f'name is: {self.name}')
        print(f'card number: {self.card_number}')

    

class PaypalPayment(PaymentStrategy):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f'user has spend: ${amount} using paypal.')
        print(f'email is: {self.email}')

    

class PaymentContext:

    def __init__(self, strategy: PaymentStrategy):
         self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)



credit_card = CreditCardPayment('alice', '1111-2222-3333-4444')
paypal = PaypalPayment('mdhasib0296@gmail.com')

payment = PaymentContext(credit_card)
payment.pay(100)

payment.set_strategy(paypal)
payment.pay(75)