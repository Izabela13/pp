"""
Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
pobranej od użytkownika jest także liczbą całkowitą.
"""

number = input("Podaj dowolną liczbę całkowitą: ")
print(input())

if  (int(number) ** 0.5) % 1 == 0:
    print("Pierwiastek kwadratowy z podanej przez Ciebie liczby całkowitej również jest liczbą całkowitą")
else:
    print("Pierwiastek kwadratowy z podanej przez Ciebie liczby zwróci liczbę zmiennoprzecinkową")