class Member:

    def __init__(self, name, memberId):
        self.__name = name
        self.__memberId = memberId
        self.__borrowBooks = []
        self.__borrowLimit = 3


    @property
    def name(self):
        return self.__name

    @property
    def memberId(self):
        return self.__memberId

    @property
    def borrowBooks(self):
        return self.__borrowBooks

    @property
    def borrowLimit(self):
        return self.__borrowLimit


    def __extractBooksTiltle(self):
        booksTitles = ''
        for book in self.borrowBooks:
            booksTitles +=" " + book.title
        return booksTitles

    def getInfo(self):
        return f"{self.name} with Id {self.memberId} borrowed {self.__extractBooksTiltle()}"


    def borrowBook(self, book):
        if 0 < self.__borrowLimit:
            self.borrowBooks.append(book)
            self.__borrowLimit -= 1

        else: 
            print("You hit the limit of borrowing books")


    def returnBook(self, book):
        self.borrowBooks.remove(book)
        self.__borrowLimit += 1