class Book:
    def __init__(self, title, author, isbn, publisher, year_published, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year_published = year_published
        self.genre = genre
        
    def display_details(self):
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
                f"Publisher: {self.publisher}, Year Published: {self.year_published}, Genre: {self.genre}")

class LibraryBook(Book):
    def __init__(self, title, author, isbn, publisher, year_published, genre, location, status):
        super().__init__(title, author, isbn, publisher, year_published, genre)
        self.location = location
        self.status = status
        
    def change_status(self, new_status):
        self.status = new_status
        
    def display_complete_details(self):
        basic_details = super().display_details()
        return f"{basic_details}, Location: {self.location}, Status: {self.status}"

# Example usage
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 
                   "Charles Scribner's Sons", 1925, "Novel", "A12", "Available")

print(book.display_complete_details())  # Display all details including status and location

# Changing status
book.change_status("Checked Out")
print(book.display_complete_details())  # Status should now be "Checked Out"
