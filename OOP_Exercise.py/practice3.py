class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available


    def borrow_book(self):
        if self.available:
            self.available = False
            print(f'you have borrowed {self.title}')
        

    

    def return_book(self):
        if not self.available: 
            self.available = True
            print(f'{self.title} book was returned')
    

    def availability(self):
        if self.available:
            return 'yes'
        else:
            return 'no'



    def __str__(self):
        
        return (f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available:{self.availability()}')
    


def get_valid_input(x):
    while True:
        user_input = input(x).strip().lower()
        if user_input in ['yes' , 'no']:
            return user_input
        
        else:
            print('please enter yes or no')



book1 = Book("The Alchemist", "Paulo Coelho", "978-0062315007")
print(book1)  
borrowing_process = get_valid_input(f'do you want to borrow the book {book1.title} ? (yes/no):')
if borrowing_process == 'yes':
    book1.borrow_book()
else:
    print('you choose not to borrow book')
         
print(book1)  
returning_process = get_valid_input(f'do you want to return your book ? (yes/no):')
if returning_process == 'yes':
    book1.return_book()
else:
    print('you chose not to return book')

print(book1)