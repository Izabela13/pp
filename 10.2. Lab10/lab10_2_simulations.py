"""
Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
wyświetli poniższe informacje:
• zestaw wylosowanych wyników,
• wyrzucaną wartość za 8 razem,
• liczbę wyrzuconych szóstek,
• maksymalną liczbę wyrzuconych tych samych wartości pod rząd.
"""

import random

numbers = []
numb6 = []

for i in range(16):
    number = random.randint(1, 6)
    numbers.append(number)
    if i == 9:
        print(number)
    elif number == 6:
        numb6.append(6)
        print(len(numb6))
print(numbers)