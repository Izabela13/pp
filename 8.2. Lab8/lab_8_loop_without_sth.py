"""
Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3.
"""

for x in range(1, 101):
    if x % 3 != 0:
        print(x)
