"""
Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje:
dodawania, odejmowania, mnożenia, dzielenia oraz operację modulo.
Wyświetl rezultat na ekranie.
"""

print("Zostaniesz poproszony o podanie dwóch liczb całkowitych")
print(
"Na podanych liczbach zostaną wykonane operacje: \n",
"- dodawania \n",
"- odejmowania \n",
"- mnożenia \n",
"- dzielenia \n",
"- modulo \n")

user_number1 = input("Podaj pierwszą liczbę: ")
user_number2 = input("Podaj drugą liczbę: ")

print("\n")

print("Dodawanie: "   + str(user_number1) + " + " + str(user_number2) + " = " + (str(int(user_number1) + int(user_number2))) + "." )
print("Odejmowanie: " + str(user_number1) + " - " + str(user_number2) + " = " + (str(int(user_number1) - int(user_number2))) + "." )
print("Mnożenie: "    + str(user_number1) + " * " + str(user_number2) + " = " + (str(int(user_number1) * int(user_number2))) + "." )
print("Dzielenie: "   + str(user_number1) + " / " + str(user_number2) + " = " + (str(int(user_number1) / int(user_number2))) + "." )
print("Modulo: "      + str(user_number1) + " % " + str(user_number2) + " = " + (str(int(user_number1) % int(user_number2))) + "." )