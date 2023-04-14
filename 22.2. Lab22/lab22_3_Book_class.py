"""
3. Napisz klasę reprezentującą obiekty typu książka, w tym celu:
• stwórz klasę Book z odpowiednimi właściwościami i metodami,
• stwórz kilka przykładowych egzemplarzy tej klasy,
• zademonstruj działanie wybranych metod na przykładowych egzemplarzach
"""


class Book:

    def __init__(self, title, author, issue, publisher):
        self.__title = title
        self.__author = author
        self.__issue = issue
        self.__publisher = publisher

    def show_short_book_info(self):
        print(self.__title, "\t", self.__author)

    def show_all_book_info(self):
        print(self.__title, "\t", self.__author, "\t", self.__issue, "\t" * 4, self.__publisher)

#######################################################################################################################

def gap(n):
    return "\t" * n


books = []
books.append(Book("Bastion \t\t\t\t",         "Stephen King \t\t\t",       1986,   "Albatros"))
books.append(Book("W górach szaleństwa \t",   "Howard Phillips Lovecraft", 1931,   "C&T Crime & Thriller"))
books.append(Book("Ania z Zielonego Wzgórza", "Lucy Maud Montgomery \t",   2009,   "Wydawnictwo Literackie"))

print()

print("Książki. Krótka informacja.")
print("-" * 60)
print("TYTUŁ", gap(6), "AUTOR")
print("-" * 60)
for b in books:
    b.show_short_book_info()

print("\n")

print("Książki. Szczegółowe informacje.")
print("-" * 100)
print("TYTUŁ", gap(6), "AUTOR", gap(6), "ROK WYDANIA", gap(2), "WYDAWNICTWO")
print("-" * 100)
for b in books:
    b.show_all_book_info()