"""
Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje:
dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo.
Wyświetl rezultat na ekranie.
"""

from time import sleep

print("Zostaniesz poproszony o podanie dwóch liczb całkowitych."), sleep(2)
print(
"Na podanych liczbach zostaną wykonane operacje: \n",
"- dodawania \n",
"- odejmowania \n",
"- mnożenia \n",
"- dzielenia \n",
"- modulo \n"), sleep(3)

user_number1 = input("Podaj pierwszą liczbę: ")
user_number2 = input("Podaj drugą liczbę: ")

print("\n")

print("Dodawanie: " + "\t "  + user_number1 + " + " + user_number2 + " = " + str(int(user_number1) + int(user_number2)))
print("Odejmowanie: "        + user_number1 + " - " + user_number2 + " = " + str(int(user_number1) - int(user_number2)))
print("Mnożenie: "  + "\t "  + user_number1 + " * " + user_number2 + " = " + str(int(user_number1) * int(user_number2)))
print("Dzielenie: " + "\t "  + user_number1 + " / " + user_number2 + " = " + str(int(user_number1) / int(user_number2)))
print("Modulo: "    + "\t "  + user_number1 + " % " + user_number2 + " = " + str(int(user_number1) % int(user_number2)))