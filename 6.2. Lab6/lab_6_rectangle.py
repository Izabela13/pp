"""
1. Napisz skrypt rysujący na ekranie prostokąt
zbudowany ze znaku jak i wymiarów określonych
przez użytkownika, np..:
"""
from time import sleep

print("Podaj informacje: "), sleep(2)
sign = input("Podaj dowolny znak, jakim chcesz narysować i wypełnić prostokąt: ")
columns = input("Podaj liczbę (całkowitą) kolumn, jaką ma mieć Twój prostokąt : ")
rows = input("Podaj liczbę (całkowitą) wierszy, jaką ma mieć Twój prostokąt: ")

print((str(sign) * int(columns) + "\n") * (int(rows)), end = "")

