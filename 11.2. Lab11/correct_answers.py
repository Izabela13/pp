# # Zadanie 1
#
# import random
#
# user_numbers = []
# random_numbers = []
# hit_total = 0
#
# for i in range(6):
#     user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę od 1 do 49: ")))
#
# print(user_numbers) # musimy wyświetlić liczby pobrane od użytkownika
#
#
# # do random numbers będziemy dodawać wylosowane liczby
#
# # W pętlli będzie to:
# # for i in range(6):
# #     random_numbers = random.sample(range(1, 50), 6)
# # pętlą nadpisujemy liczby. Najprościej zrobić to po prostu w jednej linijce kodu.
#
# random_numbers = random.sample(range(1, 50), 6)
#
# for number in user_numbers:
#     if number in random_numbers:
#         hit_total += 1
#
# user_numbers.sort()
# random_numbers.sort()
#
# print("Wylosowane liczby:", random_numbers)
# print("Obstawione liczby:", user_numbers)
# print("Trafiono:", hit_total, "liczb.")



# # Zadanie 2
#
# numbers = []
# numbers_total = int(input("Podaj liczbę elementów zbioru: "))
#
# for i in range(numbers_total):
#     number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
#     numbers.append(number)
#
# numbers.sort(reverse=True) # dokonaj sortowania odwrotnego
#
# numbers_without_duplicate = []
# for number in numbers:
#     if number not in numbers_without_duplicate:
#         numbers_without_duplicate.append(number)
#
# print(numbers_without_duplicate)



# Zadanie 3

import random

# Oznaczanie pustego pola szachowego
BLANK_SQUARE = "-- "
pieces = ["WP", "BP", "BP", "BT", "WQ"]

chessboard = [[BLANK_SQUARE for i in range(8)] for i in range(8)]

counter = 0

# nie nadpisywać sobie tych samych pól

while counter < 5:
    row = random.randint(0, 7) # zależy nam na indeksach.
    column = random.randint(0, 7)
    # jeżeli wylosujemy te same wartości, nie podniesie się counter (pętla nie wejdzie do bloku if)
    if chessboard[row][column] == BLANK_SQUARE:
        chessboard[row][column] = pieces[counter]
        counter += 1

for row in range(len(chessboard)): # pętla będzie się obracać tyle razy, ile jest elementów w wierszu
    if row == 0:
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="  ")
    print(row + 1, end=" ")
    for column in range(len(chessboard)): # pętla będzie się obracać tyle razy, ile jest elementów kolumn
        print(chessboard[row][column], end="")
    print()