"""
Wyświetl tylko liczby podzielne przez 3 ze zbioru liczb z zakresu określonego przez użytkownika.
Przykładowo dla zakresu od 1 do 10 będą to liczby 3, 6 i 9.
"""

print("Podaj zakres minimum i maksimum.")
user_min = int(input("Podaj liczbę stanowiącą minimum Twojego zbioru: "))
user_max = int(input("Podaj liczbę stanowiącą maksimum Twojego zbioru: "))

print("")

numbers_div_by3 = []

for i in range(user_min, user_max):
    if i % 3 == 0:
        numbers_div_by3.append(i)

print("Z podanego przez Ciebie zakresu następujące liczby są podzielne przez 3: " + str(numbers_div_by3))
