# # Zadanie 1:

class Employee():
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age

    def risesalary(self, percent=10):  # domyślnie 10%
        self.__salary *= percent / 100 + 1  # przemnażanie właściwości przez wartość procentową


def payroll(employee):  # dodawanie ulepszenia (w funkcji poza klasą)
    print("Lista płac")
    print("-" * 50)

    for e in employee:
        print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja:", e.getsalary(), "zł")


employee = []
employee.append(Employee("Jan", "Kowalski", 25, 3800))
employee.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employee.append(Employee("Natalia", "Nowak", 60, 15200))

payroll(employee)
employee[0].risesalary()
employee[2].risesalary(30)
payroll(employee)


# # Zadanie 2: instance_counter

class C:
    counter = 0  # zmienna klasowa. Klasa nie będzie miała innych właściwości, poza konstruktorem

    def __init__(self):
        C.counter += 1  # zwiększanie countera o 1 kiedy powstaje nowy obiekt

    def get_counter(self):
        return C.counter

for i in range(100):
    obj = C()  # nie musimy do niczego przypisywać tych obiektów

print("Utworzono obiektów:", obj.get_counter())



# # Zadanie 3

class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

        #METODY

    def show_short_info(self):
        print("tytuł:", self.__title, " autor", self.__author)

    def show_full_info(self):
        print("tytuł:", self.__title, " autor:", self.__author, " wydawca:", self.__publisher, " rok wydania:", self.__year)

books = []
books.append(Book("Dzieci z Bullerbyn", "Astrid Lindgren", "Nasza Księgarnia", 2014))
books.append(Book("Moby Dick", "Herman Marvill", "Amercom", 2009))
books.append(Book("Python. Wprowadzenie", "Mark Lutz", "Helion", 2022))

for b in books:
    b.show_full_info()
