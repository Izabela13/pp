# Zadanie 1

class Person:
    def __init__(self, name, age):  # obiekty klasy "Person" będą to zmienne instancji - potrzebny będzie konstruktor
        self.__name = name  # zmienne "name" i "age" pobierane będą z konstruktora
        self.__age = age    # ustawienie na zmienne prywatne - zabezpieczenie przed przypadkowym nadpisaniem

    def introduce(self):  # konstruktor odpowiada za ustawienie właściwości obiektu podczas tworzenia tego obiektu.
        print("Cześć, jestem", self.__name, "i mam", self.__age, "lat/a.")  # akcja przedstawienia się.


persons = []  # lista i dodawnaie osób-obiektów
persons.append(Person("Janek", 20))  # imię-"nazwa" obiektu + atrybut "wiek" obiektu.
persons.append(Person("Agata", 34))
persons.append(Person("Tomek", 55))
persons.append(Person("Monika", 14))


for p in persons:  # pętla
    p.introduce()  # dla każdego obiektu metoda "introduce()".



# Zadanie 2 --> shift + F6 (refactoring)

import random

class Dice: # obiekt
    def __init__(self): # konstruktor
        self.__value = None # wartość kości

    def throw(self):
        self.__value = random.randint(1, 6)

    def get_value(self):
        return self.__value

    def __str__(self): #wyświetli obiekt
        return "[{}]".format(self.__value)  # w nawiasach kwadratowych będzie pojawiać się wartość


# # sprawdzanie
# dice = Dice()
# print(dice) # [None] - kostka trzymana w kieszeni, nie ma wartości
# dice.throw()
# print(dice)


# Para kości
class DicePair:

    def __init__(self):
        self.__pair = [Dice(), Dice()] # lista, która ma dwa obiekty kości

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

# sprawdzenie, czy nie rzuciliśmy dwóch tych samych wartości. Rzucamy do momentu uzyskania dubletu

    def is_double(self):
        return self.__pair[0].get_value() == self.__pair[1].get_value()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])


dices = DicePair()
while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break



# Zadanie 3

class Product:
    def __init__(self, name, category, price):  # parametry
        self.__name = name  # prywatne pole
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0  # to pole nie będzie ustawiane w tym miejscu

    def set_discount_in_percentage(self, discount_in_percent):  # możliwość ustawienia rabatu
        self.__discount_in_percent = discount_in_percent  # "__discount_in_percent" zostanie pobrany z parametru

    def get_current_price(self):
        result = self.__price * (1 - self.__discount_in_percent / 100)  # obniżanie ceny
        return round(result, 2)

    def is_category(self, category):  # metoda sprawdzająca kategorię - metoda będzie brała produkt i sprawdzała,
        return self.__category == category  # czy jest to produkt danej kategorii - porównanie do jakiejś kategorii
    """
    w metodzie "is_category" będzie sprawdzane wyrażenie logiczne, czy nasza kategoria "self._category" jest równe
    temu, co podalismy jako argument, czyli "category". Jeśli tak, metoda zwróci "True", jeśli nie, metoda zwróci "False".
    """

    def __str__(self):  # ładny ciąg znaków opisujący nasz produkt
        return "{} ({}) - {} zł".format(self.__name, self.__category, self.get_current_price())
    """
    używamy tu zbitki z formatowaniem, czyli zaczynamy od ciągu znaków "" i dodajemy funckję "format()" --> "".format()
    dodajemy informację o nazwie, kategorii i bieżącej cenie - dodajemy 3 takie elementy {} --> "{}{}{}".format()
    kolejne nawiasy klamrowe będą to: nazwa, kategoria i cena --> "{}{}{}".format(self.__name, self.__category, self.get_current_price())
    "{} ({}) - {} zł".format(self.__name, self.__category, self.get_current_price())
    """


def show_products(products):  # funkcja, która pozwoli wyświetlać produkty
    for p in products: # ta funkcja będzie wyświetlała listę produktów
        print(p)

def special_offer(products, category, discount_in_percent):  # rabat dla spożywczych
    for p in products:
        if p.is_category(category):  # sprawdzanie, czy produkt jest danej kategorii
            p.set_discount_in_percentage(discount_in_percent)


products = []
products.append(Product("mleko", "spożywcze", 3.99))
products.append(Product("masło", "spożywcze", 6.56))
products.append(Product("jogurt", "spożywcze", 0.99))
products.append(Product("płyn do naczyń", "chemia", 4.50))

show_products(products)
special_offer(products, "spożywcze", 30)
print("\nPromocja\n----------")
show_products(products)