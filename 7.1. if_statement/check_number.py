"""
Chcemy zapytać użytkownika o liczbę. Podaną liczbę chcemy sprawdzić, czy jest podzielna przez 5 i 7
"""

number = int(input("Podaj liczbę: "))

print("Liczba jest: " )

#Czy liczba jest parzysta?
if number % 2 == 0: # Jeżeli wynik jest 0, to jest to liczba parzysta
    print("- parzysta")
else:
    print("- nieparzysta")


#Weryfikacja, czy liczba jest podzielna przez 5 i 7
if number % 5 == 0:  # czy liczba jest podzielna przez 5
    print("- podzielna przez 5")
else:
    print("- niepodzielna przez 5")

if number % 7 == 0:  # czy liczba jest podzielna przez 5
    print("- podzielna przez 7")
else:
    print("- niepodzielna przez 7")
