"""
1. Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
• każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
• zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
• ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
• każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.
"""


class Person:
    # def __init__(self, name, age):
    #     self.__name = name
    #     self.__age = age
    #     print("Inicjalizuję obiekt!")

    def __get_name(self, name):
        self.__name = name
        print("Jestem metodą") # TODO

    def __get_age(self, age):
        self.__age = age
        print("To jest metoda publiczna") # TODO