# 4. Composition:

# A. Create Library and Book classes where a Library has many Books and can check if a book is available for borrowing.

class Book:

    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = 'borrowed' if self.is_borrowed else 'available'
        return f'{self.title} by {self.author} - {status}'
    


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        

    def add_books(self, book):
        self.books.append(book)
        print(f'Book: {book.title} added to {self.name}')
    

    def show_books(self):
        print(f'\nBooks in {self.name}')

        if not self.books:
            print('no books in the library')
        else:
            for book in self.books:
                print(book)

            
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f'you borrowed: "{book.title}"')
                    return
                else:
                    print(f'sorry! the book {book.title} is already borrowed')
                    return
        print(f'book "{title}" not found in the library.')

    
    def return_books(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f'you returned: "{book.title}"')
                    return
                else:
                    print(f'the book: "{book.title} is not borrowed."')
                    return
        print(f'{title} is not found in the library')
                


my_library = Library('city library')

book1 = Book('1984', 'george orwell')
book2 = Book('to kill a mockingbird', 'harper lee')

my_library.add_books(book1)
my_library.add_books(book2)

my_library.show_books()

my_library.borrow_book('1984')

my_library.return_books('1984')

my_library.show_books()