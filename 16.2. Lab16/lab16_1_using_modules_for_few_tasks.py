"""
1. Korzystając z odpowiednich modułów napisz skrypt realizujący następujące zadania:
• wyświetl informacje o procesorze komputera,
• wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
• wyznacz sinus 90 stopni.
"""


import platform
from random import sample
from math import sin, radians


# Zadanie 1: Wyświetl informacje o procesorze komputera
print("Informacje o procesorze komputera: ")
print(platform.processor())  # Komputer uczelniany: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
print("\n")


# Zadanie 2: wylosuj 3 niepowtarzalne liczby ze zbioru 1-10
print("Losowanie 3 niepowtarzalnych liczb ze zbioru 1-10.")
range_list = [i for i in range(1, 11)]

print("Wylosowane liczby:", sample(range_list, 3))
print("\n")


# Zadanie 3: wyznacz sinus 90 stopni
print("Wyznaczanie sinusa 90 stopni")
print("Sinus 90 stopni to", sin(radians(90)))