# # Zadanie 1: lotek

# import random # moduł random do generowania liczb pseudolosowych
#
# user_numbers = []   # seria liczb od użytkownika
# random_numbers = [] # wylosowane przez komputer liczby
# hit_total = 0       # licznik do weryfikowania i porównywania trafień
#
# # Zaczynamy od prostego kodu - dekompozycja na mniejsze podproblemy do rozwiązania
#
#
# # Pobranie od użytkownika 6 liczb i zapisanie jej do listy "user_numbers"
# # Wiemy, że ma wykonać się 6 iteracji
# for i in range(6):
#     user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę od 1 do 49: "))) # indeks i powiększony o 1, bo zaczynamy liczenie od 0
#
# print(user_numbers) # musimy wyświetlić liczby pobrane od użytkownika
#
#
# # Wylosowanie 6-ciu liczb przez program.
# # do listy "random_numbers" będziemy dodawać wylosowane liczby
#
# # # W pętli będzie to:
# # for i in range(6):
# #     random_numbers = random.sample(range(1, 50), 6)
# # # 6 razy losowano. Tą pętlą nadpisujemy liczby. Najprościej zrobić to po prostu w jednej linijce kodu.
#
# random_numbers = random.sample(range(1, 50), 6)
#
#
# # Użytkownik dostaje informację o ilości trafień
# for number in user_numbers: # iterowanie po liście z liczbami użytkownika (pod zmienną "number" będzie kolejna liczba użytkownika)
#     if number in random_numbers: # jeżeli liczba podana przez użytkownika znajduje się w zbiorze liczb wylosowanych przez komputer, to...
#         hit_total += 1 # ... listę "hit_total" zwiększ o 1.
#
# user_numbers.sort()
# random_numbers.sort()
#
# print("Wylosowane liczby:", random_numbers)
# print("Obstawione liczby:", user_numbers)
# print("Trafiono:", hit_total, "liczb.")



# # Zadanie 2: sorted_numbers

# numbers = []
# numbers_total = int(input("Podaj liczbę elementów zbioru: ")) # ile liczb użytkownik będzie podawał
#
# for i in range(numbers_total): # uruchomienie pętli dla "i" w zakresie "range", która będzie zakresem użytkownika.
#     number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
#     numbers.append(number)
#
# numbers.sort(reverse=True) # dokonaj sortowania odwrotnego
#
# numbers_without_duplicates = []
# for number in numbers: # wybieranie ze zbioru liczb "numbers"
#     if number not in numbers_without_duplicates: # jeżeli liczba "number" nie znajduje się już w zbiorze bez duplikatów...
#         numbers_without_duplicates.append(number) # dodaj liczbę do zbioru
#
# print(numbers_without_duplicates)



# # Zadanie 3: chess_random

import random # moduł random do losowania

# Określenie, jak będziemy wizualnie określać puste pole szachowe
# Oznaczanie pustego pola szachowego
BLANK_SQUARE = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"] # lista figur do losowego rozmieszczenia

# Szachownica - tworzenie przez wyrażenie listowe zagnieżdżone, które uwolni nas od nadpisywania (referencji)
chessboard = [[BLANK_SQUARE for i in range(8)] for i in range(8)] # pętla w pętli
# [BLANK_SQUARE for i in range(8)] - 8 elementów w wpierszu
# for i in range(8) - powtórzenie wierszy 8 razy
# 8 wierszy, z których każdy ma 8 elementów tekstowych

# LOSOWANIE
counter = 0

# żeby uniknąć nadpisywania sobie tych samych pól:
while counter < 5: # mamy 5 elementów, z tego "countera" będziemy odejmować każdy postawiony na szachownicy element
    row = random.randint(0, 7) # zależy nam na indeksach.
    column = random.randint(0, 7)
    # jeżeli wylosujemy te same wartości, nie podniesie się counter (pętla nie wejdzie do bloku if)
    if chessboard[row][column] == BLANK_SQUARE: # sprawdzenie, czy na planszy jest puste pole
        chessboard[row][column] = pieces[counter] # jeżeli pole jest puste, możemy na nim postawić element z listy (pieces)
        counter += 1
# Stosujemy pętlę while dlatego, że możemy natrafić na już zajęte pole. Wówczas counter ma się nie zmienić.

# Wyświetlenie szachownicy:
for row in range(len(chessboard)): # pętla będzie się obracać tyle razy, ile jest elementów w wierszu
    if row == 0: # jeżeli wiersz będzie miał indeks 0, wyświetlimy etykiety
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="  ")
    print(row + 1, end=" ") # liczba wiersza
    for column in range(len(chessboard[row])): # pętla będzie się obracać tyle razy, ile jest elementów kolumn
        print(chessboard[row][column], end=" ")
    print()