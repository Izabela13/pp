# TWORZENIE I ULEPSZANIE FUNKCJI
# Pobieramy od użytkownika 3 liczby i wyświetlamy


# # Rozbicie elementów pobierania
# print("Podaj liczbę: ")
# a = int(input())
# print("Podaj liczbę: ")
# b = int(input())
# print("Podaj liczbę: ")
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

# # Powtarzającą się część kodu można wydzielić do funkcji.


# # I UPDATE - stworzenie funkcji
# def show_message():
#     print("Podaj liczbę: ") # Funkcję będzie wyświetlała komunikat

# show_message() # wywołanie funkcji = wyświetlenie komunikatu funkcji
# a = int(input())
# show_message()
# b = int(input())
# show_message()
# c = int(input())

# print("Pobrano liczby:", a, b, c)

# # Co nam to dało? Jakie to daje korzyści?
# # 1. Zmiana formy komunikatu nastąpi tylko w jednym miejscu. Np. z "Podaj liczbę" na "Proszę, podaj liczbę: "
# # 2. Modyfikacja całej funkcji, np. podawanie liczb będzie następować w tej samej linijce


# # II UPDATE - zmiana komunikatu funkcji i sposobu wyświetlania informacji.
# def show_message():
#     print("Proszę, podaj liczbę: ", end="") # modyfikacji dokonujemy tylko w jednym miejscu

# show_message()
# a = int(input())
# show_message()
# b = int(input())
# show_message()
# c = int(input())

# print("Pobrano liczby:", a, b, c)


# # PRZEJŚCIE DO PLIKU ŹRÓDŁOWEGO asterisks


# III UPDATE - parametryzowanie funkcji:
# def show_message(number_no): # wprowadzenie parametru "number_no"
#     print("Proszę, podaj " + str(number_no) + " liczbę: ", end="") # Proszę, podaj + "którą?" + liczbę

# show_message(1)
# a = int(input())
# show_message(2)
# b = int(input())
# show_message(3)
# c = int(input())

# print("Pobrano liczby:", a, b, c)



# # POWRÓT DO PLIKU ŹRÓDŁOWEGO function_demo



# # IV UPDATE - eliminacja powtarzających się instrukcji input()
# # Możemy zrefaktorować skrypt. Zamiast metody "show_message", możemy zmienić na "get_number".
# def get_number(number_no):
#     print("Proszę, podaj", number_no, "liczbę:", end=" ")
#     return int(input()) # co ma zwrócić funkcja

# a = get_number(1)
# b = get_number(2)
# c = get_number(3)

#print("Pobrano liczby: ", a, b, c)

# # Funkcja "get_number" realizuje dwie rzeczy:
# # 1. Wyświetla etykietę korzystając z argumentu, który przekazujemy (po to, żeby określić, którą liczbę pobieramy).
# # 2. Pobiera liczbę od użytkownika, konwertuje na liczbę całkowitą i zwraca ją za pomocą instrukcji "return".
"""
Wynik:
Proszę, podaj 1 liczbę: 1
Proszę, podaj 2 liczbę: 2
Proszę, podaj 3 liczbę: 3
Pobrano liczby:  1 2 3
"""



# # V UPDATE: Można jeszcze skrócić zapis:
# def get_number(number_no):
#     return int(input("Proszę, podaj " + str(number_no) + " liczbę: "))
#
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)
#
# print("Pobrano liczby:", a, b, c)



# # VI UPDATE: Poprawa zapisu - ostatnie uproszczenie
def get_number(number_no):
    return int(input("Proszę, podaj " + str(number_no) + " liczbę: "))

print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))