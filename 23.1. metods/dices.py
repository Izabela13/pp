# PROGRAM SYMULUJĄCY RZUT DWIEMA KOSTKAMI DO GRY W PODEJŚCIU OBIEKTOWYM

import random

class Dice:  # kostka to obiekt
    def __init__(self):  # konstruktor - w tym konstruktorze będziemy inicjalizować obiekt
        self.value = None  # właściwością będzie wartość kości (na początku ustawiona na wartość nieokreśloną "None")
    # Dopóki nie rzucimy kości, każda kostka trzymana w ręce ma nieokreśloną wartość
    def throw(self): # kostka będzie miała zachowanie "losuj"
        self.value = random.randint(1, 6)  # podczas rzutu kostka będzie losować randomową wartość od 1 do 6.
    # Zamiast funkcji print() można użyć funkcji "__str__", która zwróci ciąg znaków.
    def __str__(self):  # wyświetli obiekt
        return "[{}]".format(self.value)  # w nawiasach kwadratowych będzie pojawiać się wartość


# # sprawdzanie
# dice = Dice()
# print(dice)  # [None] - kostka trzymana w kieszeni, nie ma wartości
# dice.throw() # po rzucie kością wyświetli się wartość od 1 do 6
# print(dice)


# Para kości
class DicePair:

    def __init__(self):  # konstruktor
        self.pair = [Dice(), Dice()]  # zdefiniowanie właściwości "para" - lista, która ma dwa obiekty kości

    def throw(self):  # metoda "rzucaj"
        self.pair[0].throw()  # najpierw losowanie na jednej kości (odwołanie do kości o indeksie 0)
        self.pair[1].throw()  # odwołanie do kości o indeksie 1.

# Rzucamy do momentu uzyskania dubletu.

    def is_double(self): # sprawdzenie, czy nie rzuciliśmy dwóch tych samych wartości.
        return self.pair[0].value == self.pair[1].value  # zwróć "True" jeżeli wartość na kości 1 = wartość na kości 2.

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])  # string reprezentujący kości


dices = DicePair()  # para kości
while True:  # rzucamy do momentu wyrzucenia dubletu
    dices.throw() # rzucamy
    print(dices)  # drukujemy to, co się wyrzuciło
    if dices.is_double():  # jeśli wypadł dublet...
        break  # ... wyjdź z pętli

"""
Podsumowanie: 

Za pomocą klasy "Dice" zamodelowano właściwości i zachowanie jednej kostki do gry. 

Za pomocą klasy "DicePair" zagregowano obiekty klasy "Dice". Para kości jest przechowywana w słowniku. W rzucie 
(metoda "throw") najpierw toczy się jedna kostka, potem toczy się druga kostka. Obie kości losują jakieś właściwości. 

Za pomocą metody "is_duble" następuje porównanie właściwości dwóch kostek. 

Na końcu - wyświetlenie wyniku użytkownikowi. W przypadku dubletu następuje przerwanie zabawy.
"""