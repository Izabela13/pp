"""
Napisz skrypt, który oblicza ile warta byłaby inwestycja na kwotę
14 000 zł, gdyby jej wartość zwiększyła się w pierwszym roku o 40%, w
drugim roku zanotowała stratę w wysokości 1500 zł, a w trzecim roku
zwiększyła się o 12%
"""

print ("Liczenie krok po kroku")
print("Inwestycja")
print(14000)

print("")
print("Pierwszy rok")
print(14000 * 1.4)

print("")
print("Drugi rok")
print(14000 * 1.4 - 1500)

print("")
print("Trzeci rok")
print((14000 * 1.4 - 1500) * 1.12)


#Według zmiennych
print("Liczenie na podstawie zmiennych")
print("Inwestycja")
print(14000)

print("")
print("Pierwszy rok")
print(14000 * 1.4)
rok1 = (14000 * 1.4)

print("")
print("Drugi rok")
print(14000 * 1.4 - 1500)
rok2 = rok1 - 1500

print("")
print("Trzeci rok")
print(round(rok2 * 1.12))


#najlepsze rozwiązanie
print("")
print("")
print("Poprawne rozwiązanie")
print("")
print("Początkowa wartość inwestycji: ", 14_000., "zł")
print("Wartość inwestycji po pierwszym roku: ", 14_000. * 1.4, "zł")
print("Wartość inwestycji po drugim roku: ", (14_000. * 1.4) - 1_500, "zł")
print("Wartość inwestycji po trzecim roku: ", round((((14_000. * 1.4) - 1_500) * 1.12) ,2), "zł")