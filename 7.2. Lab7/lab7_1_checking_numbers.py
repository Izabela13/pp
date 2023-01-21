"""
Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
pobranej od użytkownika jest także liczbą całkowitą.
"""

number = input("Podaj dowolną liczbę całkowitą: ")

if  (int(number) ** 0.5) % 1 == 0:
    print("Pierwiastek kwadratowy z podanej przez Ciebie liczby jest liczbą całkowitą.")
else:
    print("Pierwiastek kwadratowy z podanej przez Ciebie liczby nie jest liczbą całkowitą.")