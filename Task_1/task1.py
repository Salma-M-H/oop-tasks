from Library import Library
from Member import Member
from Book import Book


# Create a library
library = Library("City Central Library")

# Create books
book1 = Book("Design Patterns", "Gang of Four", "978-0201633610")
book2 = Book("Clean Code", "Robert Martin", "978-0132350884")
book3 = Book("The Pragmatic Programmer", "Andy Hunt", "978-0135957059")

# Add books to library
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)


# Register members
member1 = Member("Alice Johnson", "M001")
member2 = Member("Bob Smith", "M002")

library.registerMember(member1)
library.registerMember(member2)

# Display available books
library.displayAvailableBooks()

# Member borrows a book
library.lendBook(member1, "978-0201633610")
library.lendBook(member2, "978-0201633610")

# Display available books again
library.displayAvailableBooks()

# Member returns a book
library.receiveBook(member1, "978-0201633610")