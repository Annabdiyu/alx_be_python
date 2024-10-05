class Book:
    def __init__(self, title):
        self.title = title
        self.is_checked_out = False  

class Library:
    def __init__(self):
        self._books = []  
        self.selected_book = None  
    
    def add_book(self, book):
        self._books.append(book)
        print(f"Added book: {book.title}")
    

    def select_book(self, title):
        for book in self._books:
            if book.title == title:
                self.selected_book = book
                print(f"Selected book: {book.title}")
                return
        print(f"Book '{title}' not found in the library.")

    
    def check_out_book(self):
        if self.selected_book and not self.selected_book.is_checked_out:
            self.selected_book.is_checked_out = True
            print(f"Checked out: {self.selected_book.title}")
        elif self.selected_book:
            print(f"Book '{self.selected_book.title}' is already checked out.")
        else:
            print("No book selected.")

    
    def return_book(self):
        if self.selected_book and self.selected_book.is_checked_out:
            self.selected_book.is_checked_out = False
            print(f"Returned: {self.selected_book.title}")
        elif self.selected_book:
            print(f"Book '{self.selected_book.title}' was not checked out.")
        else:
            print("No book selected.")

    
    def list_available_books(self):
        available_books = [book.title for book in self._books if not book.is_checked_out]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f" - {title}")
        else:
            print("No books are available.")
