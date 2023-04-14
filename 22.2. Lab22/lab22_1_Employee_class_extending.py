"""
1. Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
• dodaj metodę risesalary(),
• metoda powinna zwiększać zarobki o podaną wartość procentową,
• domyślnie metoda powinną zwiększać zarobkio 10%.
"""

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

    def risesalary(self, pct=10):
        percent = (pct / 100) + 1
        return self.__salary * percent


def rise(pct=10):
    return pct


def gap(n):
    return "\t" * n

#######################################################################################################################

employee = []

# Płace początkowe
employee.append(Employee("Jan",     "Kowalski   \t\t\t", "25",   3800))
employee.append(Employee("Edmund",  "Kaczmarczyk\t\t",  "45",   7000))
employee.append(Employee("Natalia", "Nowak      \t\t",  "60",   15200))

print("Lista płac")
print("-" * 50)
print("IMIĘ I NAZWISKO", gap(2), "WIEK", gap(2), "PENSJA")
print("-" * 50)
for e in employee:
    print(e.getfullname(), e.getage(), "lat", gap(1), e.getsalary(), "zł")


print("\n")


# Płace po generalnej podwyżce o 10%
print("Lista płac po podwyżce o", str(rise()) + "%")
print("-" * 50)
print("IMIĘ I NAZWISKO", gap(2), "WIEK", gap(2), "PENSJA")
print("-" * 50)
for e in employee:
    print(e.getfullname(), e.getage(), "lat", gap(1), round(e.risesalary()), "zł")


print("\n")


# Płace po indywidualnych podwyżkach
print("Lista płac po indywidualnych podwyżkach")
print("-" * 60)
print("IMIĘ I NAZWISKO", gap(2), "WIEK", gap(2), "PODWYŻKA", gap(2), "PENSJA")
print("-" * 60)
print(employee[0].getfullname(), employee[0].getage(), "lat", gap(1), rise(), "%", gap(3), round(employee[0].risesalary()), "zł")
print(employee[1].getfullname(), employee[1].getage(), "lat", gap(1), rise(5), "%", gap(3), round(employee[1].risesalary(5)), "zł")
print(employee[2].getfullname(), employee[2].getage(), "lat", gap(1), rise(2), "%", gap(3), round(employee[2].risesalary(2)), "zł")