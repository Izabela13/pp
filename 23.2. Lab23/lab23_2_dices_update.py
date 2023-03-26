"""
2. Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).
"""

import random

class Dice: # obiekt
    def __init__(self): # konstruktor
        self.value = None # wartość kości

    def __throw(self):
        self.value = random.randint(1, 6)

    def __str__(self): #wyświetli obiekt
        return "[{}]".format(self.value)  # w nawiasach kwadratowych będzie pojawiać się wartość


# # sprawdzanie
# dice = Dice()
# print(dice) # [None] - kostka trzymana w kieszeni, nie ma wartości
# dice.throw()
# print(dice)


# Para kości
class DicePair:

    def __init__(self):
        self.pair = [Dice(), Dice()] # lista, która ma dwa obiekty kości

    def __throw(self):
        self.pair[0].throw()
        self.pair[1].throw()

# sprawdzenie, czy nie rzuciliśmy dwóch tych samych wartości. Rzucamy do momentu uzyskania dubletu

    def __is_double(self):
        return self.pair[0].value == self.pair[1].value

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])


dices = DicePair() #TODO
while True:
    dices._DicePair.__throw()
    print(dices)
    if dices._DicePair.__is_double():
        break