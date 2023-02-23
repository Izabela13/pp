"""
Chcemy zapytać użytkownika o liczbę. Podaną liczbę chcemy sprawdzić, czy jest parzysta
i czy jest podzielna przez 5 i 7 (czy jest podzielna bez reszty).
"""

number = int(input("Podaj liczbę: "))
# konwersja do liczby całkowitej (int) + instrukcja input pobierająca od użytkownika jakąś wartość + prompt w instrukcji intput()

print("Liczba jest: " )

#Czy liczba jest parzysta (nieparzysta)?
if number % 2 == 0: # Jeżeli wynik jest 0, to jest to liczba parzysta
    print("- parzysta")
else:
    print("- nieparzysta")


#Weryfikacja, czy liczba jest podzielna przez 5 i 7
if number % 5 == 0:  # czy liczba jest podzielna przez 5
    print("- podzielna przez 5")
else:
    print("- niepodzielna przez 5")

if number % 7 == 0:  # czy liczba jest podzielna przez 7
    print("- podzielna przez 7")
else:
    print("- niepodzielna przez 7")
