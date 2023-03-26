"""
2. Napisz klasę zliczającą wszystkie powstałe swoje instancje.
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

    def risesalary(self, pct=1.10):
        return self.__salary * pct


def CounterClass():
    counter = 0
    if Employee:
        counter += 1
    return counter


employee = []
employee.append(Employee("Jan", "Kowalski", 25, 3800))
employee.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employee.append(Employee("Natalia", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

for e in employee:
    print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja:", e.getsalary(), "zł")


print("\n")
print("Lista płac po podwyżce o 10%")
print("-" * 50)

for e in employee:
    print(e.getfullname(), "wiek:", e.getage(), "lat,", "pensja po podwyżce:", round(e.risesalary()), "zł")


print()
counting = CounterClass()
print(counting)