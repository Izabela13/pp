"""
3. Napisz klasę reprezentującą obiekty typu książka, w tym celu:
• stwórz klasę Book z odpowiednimi właściwościami i metodami,
• stwórz kilka przykładowych egzemplarzy tej klasy,
• zademonstruj działanie wybranych metod na przykładowych egzemplarzach
"""


class Book:

    def __init__(self, title, author, issue):
        self.__title = title
        self.__author = author
        self.__issue = issue

    def get_book_name(self):
        return self.__title

    def getfullname(self):
        return self.__author

    def getage(self):
        return self.__issue


book = []
book.append(Book("Bastion", "Stephen King", 1986))
book.append(Book("W górach szaleństwa", "Lovecraft", 1931))


