class Library:
    def __init__(self, name):
        self.__name = name
        self.books = []
        self.members = []

    @property
    def name(self):
        return self.__name


    def addBook(self, book):
        self.books.append(book)


    def lendBook(self, member, isbn):
          for book in self.books:
            if book.isbn == isbn:
                if book.isAvailable:
                    member.borrowBook(book)
                    book.borrow()
                    print(f'{member.name} borrowed {book.title}\n')
                    break
                else:
                    print('Book is not available')
                 
    def receiveBook(self, member, isbn):
        for book in member.borrowBooks:
            if book.isbn == isbn:
                member.returnBook(book)
                book.returnBook()
                print(f"{member.name} returned {book.title}")

                break

    def displayAvailableBooks(self):
        availableBooks = [book.getInfo() for book in self.books if book.isAvailable]
    
        print(f"Available books in {self.name}:")
        print(print("\n".join(availableBooks)))

    def registerMember(self, member):
        self.members.append(member)


    def __searchByTitle(self, title):
        foundBooks = [book for book in self.books if  title.lower() in book.title.lower()]
        return foundBooks


    def __searchByAuthor(self, author):
        foundBooks = [book for book in self.books if author.lower() in book.author.lower()]
        return foundBooks


    def searchByAuthorOrTitle(self, title="", author=""):
        foundBooks = []

        if title and author:
            foundByTitle = self.__searchByTitle(title)
            foundBooks = [book for book in foundByTitle if book.author.lower() in author.lower()]

        elif title:
            foundBooks = self.__searchByTitle(title)

        elif author:
            foundBooks = self.__searchByAuthor(author)

        return [book.getInfo() for book in foundBooks]