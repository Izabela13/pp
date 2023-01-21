"""
Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
znak z jakiej będzie zbudowana powinien określić użytkownik
"""

matrix_size = int(input("Podaj rozmiar macierzy: "))
matrix_sign = int(input("Podaj znak dla macierzy: "))

for x in matrix_size:
    print(matrix_sign * str(matrix_size))