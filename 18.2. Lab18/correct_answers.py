# Zadanie 1: alphabet

# Nie próbować generować alfabetu z polskimi znakami

# alphabet = "aąbcćdeęfghijklłmnńoópqrstuvwxyzźż"
#
# for c in alphabet:
#     print(c, ord(c))



# Zadanie 2: string_statistics funkcja generująca ciąg znaków
# Istotne jest - implementacja funkcji, funkcja jest skrzynką --> wejście - przekazanie jako argument ciągu znaków
# wyjście --> zwrócić obiekt typu słownik

"""
lista [1, 2, 3]
- odwołanie po indeksach (lista[0])
- kolejność jest zachowana
- elementy można usuwać i dodawać

krotka (1, 2, 3)
- bardzo podobna do listy
- kolejność jest zachowana
- nie jest mutowalna

słownik {}
- wartość klucz:wartość
- nie jest sekwencją, bezpośrednio nie można po nim iterować
- element są uporządkowane
- klucze wstawione do słownika nie mogą się powtarzać
- klucz jednoznacznie identyfikuje daną wartość w słoniku

ciąg znaków
- sekwencja
- podobny do krotki - niezmienny
"""

# ciąg znaków i słownik
# w pierwszej kolejnosći przejść po ciągu znaków

# string = "abracadabra"
#
# def count_letters(string):
#     stats = {}
#
#     for char in string: # c to zmienna
#         if char in stats: # stats.keys():  przypadek, gdy literka jest już w słowniku
#             stats[char] += 1
#         else:
#             stats[char] = 1
#
#     return stats  # zwracanie słownika "stats".
#
#
# print(count_letters(string))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
# print(count_letters("abcabc"))
# print(count_letters("Ala ma kota, a kot ma Alę."))



# Zadanie 3: caesar_code
"""
Alfabet: AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ
  Szyfr: CĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻAĄB
"""

delta = 3 # do zmiennej przypisujemy parametr przesunięcia
# wersja bez polskich znaków

# print(ord("A")) # 65 - punkt startowy
# print(ord("Z")) # 90 - punkt końcowy

for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end="")
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# print()

# # Pętla dla zmiany znaku kodowego
# for i in range(ord("A") + delta, ord("Z") + 1 + delta):
#     print(chr(i), end="")
# # DEFGHIJKLMNOPQRSTUVWXYZ[\] - przy XYZ trzeba zawinąć do ABC

print()

for i in range(ord("A") + delta, ord("Z") + 1 + delta):
    if i > ord("Z"):
        i -= ord("Z") - ord("A") + 1
    print(chr(i), end="")
# DEFGHIJKLMNOPQRSTUVWXYZABC

print()


# Deszyfrowanie - zapisać funkcję do deszyfrowania

# Funkcja rozkodowująca jedną literę
def decode_letter(letter, delta): # jaka litera i o ile przesunąć
    if letter < "A" or letter > "Z": # jeżeli w kodowaniu trafi się spacja lub przecinek, to chcemy, żeby wróciły te same znaki
        return letter
    n = ord(letter) - delta # punkt kodowy zmiennej
    # zawijanie liter
    if n < ord("A"):
        n += ord("Z") - ord("A") + 1
    return chr(n)
# Funkcja do rozszyfrowania jednej litery

# print(decode_letter("J", delta) == "G") # True
# print(decode_letter("B", delta)) # Y - przy przesunięciu punktu kodowego o 3

print()

# Funkcja rozszyfrowująca
def decode(string, delta): # punktem wejściowym będzie string, który będzie przesuwany o deltę (która może się zmienić)
    decoded = ""
    for char in string:
        decoded += decode_letter(char, delta)
    return decoded

print(decode("VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ", delta))
# STUDIA PODYPLOMOWE - PROGRAMISTA PYTHON