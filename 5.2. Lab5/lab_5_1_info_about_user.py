"""
Napisz skrypt wyświetlający na ekranie informacje o użytkowniku takie
jak: imię, wiek oraz miasto. Dane przechowuj w odpowiednio nazwanych
zmiennych.
"""

name = "Iza"
age = 30
city = "Kraków"


# Sposób 1: Zapis w jednej linijce:
print(
"Infromacje o użytkowniku:", "\n",
"name:", name, "\n", "age:", age, "\n", "city:", city, "\n")


#Sposób 1: Zapis z uporządkowaną strukturą:
print(
"Informacje o użytkowniku: ", "\n",
"name:", name, "\n",
"age:", age, "\n",
"city:", city, "\n")


#Sposób 2: Zapis wyświetlający informacje o użytkowniku wewnątrz zdań:
print("Mam na imię " + name + ". " + "Liczę " + str(age) + " lat" + ". " + "Zamieszkuję " + city + ".")
