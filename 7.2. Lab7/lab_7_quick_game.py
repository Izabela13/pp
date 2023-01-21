"""
Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
o parzystości zgadywanej liczby itp.
"""

import random

number = random.randint(1, 10)

guess = int(input("Zgadnij jaką liczbę z przedziału od 1 do 10 mam na myśli!: "))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
elif guess != number:
    print("Niestety myślałem o innej liczbie. Spróbuj jeszcze raz. Podam Ci podpowiedź: ")
    if number % 2 == 0:
        print("Pomyślana przeze mnie liczba jest parzysta")
    else:
        print("Pomyślana przeze mnie liczba jest nieparzysta")