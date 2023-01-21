import random

number = random.randint(1, 3)

guess = int(input("Zgadnij jaką liczbę mam na myśli! (1, 2, lub 3): "))
if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
else:
    print("Niestety myślałem o liczbie: " + str(number) + ".")