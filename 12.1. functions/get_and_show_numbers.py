# Pobieramy od użytkownika 3 liczby i wyświetlamy

# print("Podaj liczbę: ")
# a = int(input())
# print("Podaj liczbę: ")
# b = int(input())
# print("Podaj liczbę: ")
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)


# Powtarzającą się część można wydzielić do funkcji.
# def show_message():
#     print("Podaj liczbę: ")
#
# show_message()
# a = int(input())
# show_message()
# b = int(input())
# show_message()
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

# Co nam to dało?
# 1. Zmiana komunikatu nastąpi tylko w jednym miejscu. Np. "Proszę, podaj liczbę: "
# 2. Modyfikacja całej funkcji, np. podawanie liczb będzie następować w tej samej linijce

# def show_message():
#     print("Proszę, podaj liczbę: ", end="")
#
# show_message()
# a = int(input())
# show_message()
# b = int(input())
# show_message()
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)


# Parametryzowanie:
# def show_message(number_no):
#     print("Proszę, podaj " + str(number_no) + " liczbę: ", end="")
#
# show_message(1)
# a = int(input())
# show_message(2)
# b = int(input())
# show_message(3)
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)


# Poprawianie inputów - żeby nie było ich tak dużo

# def get_number(number_no):
#     print("Proszę, podaj", number_no, "liczbę:", end=" ")
#     return int(input())
#
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)
#
# print("Pobrano liczby: ", a, b, c)
"""
Wynik:
Proszę, podaj 1 liczbę: 1
Proszę, podaj 2 liczbę: 2
Proszę, podaj 3 liczbę: 3
Pobrano liczby:  1 2 3
"""

# Można jeszcze skrócić zapis:
def get_number(number_no):
    return int(input("Proszę, podaj " + str(number_no) + " liczbę: "))

a = get_number(1)
b = get_number(2)
c = get_number(3)

print("Pobrano liczby:", a, b, c)