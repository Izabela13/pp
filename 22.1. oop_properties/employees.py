class Employee():
    def __init__(self, firstname, lastname, age, salary): # przypisanie pracownikowi właściwości
        self.__firstname = firstname  # pracownik będzie miał imię (klasa będzie hermetyczna)
        self.__lastname = lastname  # poszczególne właściwości będą przypisywane do konstruktora
        self.__age = age
        self.__salary = salary

    def getsalary(self):  # zachowanie klasy --> metoda zwróci zarobki
        return self.__salary

    def getfullname(self):  # zachowanie klasy --> metoda zwróci pełne imię
        return self.__firstname + " " + self.__lastname

    def getage(self):  # zachowanie klasy --> metoda zwróci wiek pracownika
        return self.__age


employee = []  # tworzenie listy pracowników. Do tej listy będą dodawani poszczególni pracownicy
employee.append(Employee("Jan", "Kowalski", 25, 3800))
employee.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employee.append(Employee("Natalia", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

for e in employee: # dla każdego pracownika w liście "employee" wyświetlimy kolejno informacje o nim
    print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja:", e.getsalary(), "zł")

"""
Konstruktor zainicjalizował zmienne instancji. Za pomocą odpowiednich metod, które w tym przypadku były "geterami",
pozwalającymi odczytać pola prywatne wyświetliliśmy informacje. 

Zabieg hermetyzacji (enkapsulacji) spowodował zabezpieczenie pól - możliwość odczytu bez nadpisania.
"""