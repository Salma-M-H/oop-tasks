class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__isAvailable = True

    @property
    def isAvailable(self):
        return self.__isAvailable

    @isAvailable.setter
    def isAvailable(self, value):
        self.__isAvailable = value

    @property
    def isbn(self):
        return self.__isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author


    def getInfo(self):
        return f"- {self.title} by {self.author} (ISBN: {self.isbn})"

    def borrow(self):
        self.isAvailable = False

    def returnBook(self):
        self.isAvailable = True