#Jordan Pulaski
#jordan.pulaski001@albright.edu
#AW 2
class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def setTitle(self, title):
        self.__title = title

    def setAuthor(self, author):
        self.__author = author

    def setPublisher(self, publisher):
        self.__publisher = publisher

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getPublisher(self):
        return self.__publisher

    def __str__(self):
        return "Book Title: " + self.__title + \
               "\nAuthor's Name: " + self.__author + \
               "\nPublisher's Name: " + self.__publisher

    
