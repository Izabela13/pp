"""
1. Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
• każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
• zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
• ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
• każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def presentation(self):
        print("Jestem " + self.__name + ". Mam lat " + str(self.__age) + ".")


people = []

people.append(Person("Ellie", 14))
people.append(Person("Joel", 52))
people.append(Person("Ethan", 35))
people.append(Person("Jill", 30))
people.append(Person("Leon", 21))


print("\nAkcja przedstawiania się każdego obiektu klasy Person.")
for person in people:
    person.presentation()