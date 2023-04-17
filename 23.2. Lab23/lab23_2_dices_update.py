"""
2. Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).
"""

import random

# Jednak kość
class Dice:
    def __init__(self):
        self.__value = None

    def throw(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return "[{}]".format(self.__value)

    def get__value(self):
        return self.__value


# # sprawdzanie
# dice = Dice()
# print(dice)  # [None] - kostka trzymana w kieszeni, nie ma wartości
# dice.throw() # po rzucie kością wyświetli się wartość od 1 do 6
# print(dice)


# Para kości
class DicePair:

    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

# Rzucamy do momentu uzyskania dubletu.
    def is_double(self):
        return self.__pair[0].get__value() == self.__pair[1].get__value()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])


dices = DicePair()
while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break