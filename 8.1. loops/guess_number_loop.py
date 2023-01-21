import random

counter = 1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1, 10)? "))

while number != guess:
    guess = int(input("Nie, to nie ta, spróbuj jeszcze raz: "))
    counter +=1 #nie sterujemy pętlą counterem. Do tego służy sprawdzenie, czy wartości są różne

print("Brawo! Udało Ci się za " + str(counter) + " razem.")

#counter jest powiększany, gdy wejdziemy do bloku