# Gra w odgadnij liczbę

import random # biblioteka w pythonie, która pozwala na symulację losowania liczb

number = random.randint(1, 3) # losowa wartość + funkcja z modułu random + zakres

guess = int(input("Zgadnij jaką liczbę mam na myśli! (1, 2, lub 3): "))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
else:
    print("Niestety myślałem o liczbie: " + str(number) + ".")