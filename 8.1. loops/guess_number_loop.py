# Gra toczy się, dopóki nie zostanie odgadnięta liczba

# na początku import biblioteki random do liczb pseudolosowych
import random

counter = 1 # w tej grze potrzebny będzie counter, czyli licznik
number = random.randint(1, 10) # wylosowana liczba z przedziału 1-10
guess = int(input("Zgadnij jaką liczbę mam na myśli (1, 10)? ")) # pobieranie liczby od użytkownika

while number != guess: # dopóki wylosowana liczba jest różna niż podana przez użytkownika, to wykonuj pętlę
    guess = int(input("Nie, to nie ta, spróbuj jeszcze raz: ")) # kolejny komentarz
    counter +=1 #nie sterujemy pętlą za pomocą counter'a. Do tego służy sprawdzenie, czy wartości są różne (!=)
# Counter posłuży do wyświetlenia użytkownikowi informacji, za którym razem odgadł liczbę. Można pominąć counter.
# Wyjście z pętli, gdy number == guess

print("Brawo! Udało Ci się za " + str(counter) + " razem.")

# counter jest powiększany, gdy wejdziemy do bloku. Zlicza, za którym razem gracz odgadł liczbę.
# ta pętla może się kręcić w nieskończoność.
# pętla while nie miała związku z żadnym licznikiem, tj. nie miała z góry założone, ile razy się obróci.
# pętla while za każdym razem sprawdzała, czy wylosowany number jest różny od wartości podanej przez użytkownika.