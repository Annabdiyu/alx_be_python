class Book:
    def __init__(self, title,author):
        self.title = title
        self.author=author
        self.is_checked_out = False  

class Library:
    def __init__(self):
        self._books = []  
    
    def add_book(self, book):

        self._books.append(book)
        print(f"Added book: {book.title}")

    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is either not available or already checked out.")
    

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out.")
    

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book.is_checked_out]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f" - {title}")
        else:
            print("No books are available.")
