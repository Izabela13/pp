# # ŁAŃCUCHY ZNAKÓW

#######################################################################################################################

# # OPERACJE NA ŁAŃCUCHACH ZNAKÓW

txt = "Ala ma kota."  # nie ma znaczenia, czy łańcuch znaków ujęty jest w cudzysłowy "" czy w apostrofy ''.

# Wyświetlenie zawartości zmiennej "txt":
print(txt)       # Ala ma kota.

# # Sprawdzanie, jaki jest rozmiar - ilość znaków w łańcuchu znaków.
print(len(txt))  # 12

# # Co kryje się w zmiennej "txt" o indeksie -1
print(txt[-1])   # . --> jest to kropka.

# # Jakąś długość będzie miał pusty ciąg znaków:
print(len(""))  # 0 --> pusty ciąg znaków będzie miał zerową ilość elemnentów (zerową długość).

print()

#######################################################################################################################

# # ZNAKI SPECJALNE

# # Mimo tego, że zakodujemy więcej znaków, znaki specjalne również mają swoją długość
print(len("\t\n\\"))  # 3 --> ciąg znaków o długości 3: tabulator + znak nowej linii + backslash

print()

#######################################################################################################################

# # WIELOLINIOWE ŁAŃCUCHY ZNAKÓW

txt = "To jest tekst."\
      "To dalszy ciąg."
print(txt)  # To jest tekst.To dalszy ciąg.

# # Użycie trzech apostrofów albo trzech cudzysłowów spowoduje, że dostaniemy tekst ze złamaną linią
# # oraz z uwględnionym wcięciem.
txt = """To jest tekst.
       To dalszy ciąg."""
print(txt)
# To jest tekst.
#        To dalszy ciąg.


# # Jeżeli chcielibyśmy sprawdzić długość naszego tekstu, a nasz tekst były w postaci:
txt = """a
b
c"""
# # to dostaniemy informację, że na nasz tekst składa się 5 znaków.
print(len(txt))  # 5 --> 3 znaki (a, b, c) + 2 znaki nowej linii.

# # Zamiennie można byłoby zapisać tę formę w następujący sposób:
txt2 = "a\nb\bc"

print(len(txt))   # 5
print(len(txt2))  # 5

print()

#######################################################################################################################

# # KONKATENACJA I REPLIKACJA

str1 = "a"
str2 = "b"

# Łączenie stringów:
print(str1 + str2)  # ab
print(str2 + str1)  # ba
print()

# Replikowanie stringów:
print(str1 * 3)  # aaa
print(5 * str2)  # bbbbb
print()

# Można stosować operatory skrótów:
str1 += str2
print(str1)  # ab

str1 *= 10
print(str1)  # abababababababababab

print()

#######################################################################################################################

# # Przejście do plików ord() i chr()

#######################################################################################################################

# # STRING JAKO ŁAŃCUCH ZNAKÓW (SEKWENCJA):

txt = "Ala ma kota."
# Tekst jest indeksowany
print(txt[2])   # a
print(txt[-4])  # o
print()


# # Wyświetlanie wszystkich znaków za pomocą indeksów - użycie pętli

for i in range(len(txt)):
      print(txt[i], end="-")  # A -l -a -  -m -a -  -k -o -t -a -. -
print("\n")

for c in txt:
      print(c)  # Wyświetli się jeden znak pod drugim
print()

#######################################################################################################################

# # WYCINKI

print(txt[4:6])   # wycinanie "ma"
print(txt[7:])    # wycinanie "kota"
print(txt[-1:])   # .
print(txt[2::3])  # aao --> wyświetlanie od drugiego znaku co trzeci znak
print()

#######################################################################################################################

# # GENEROWANIE ALFABETU

# Wypisujemy, od jakiego punktu kodowego alfabet się zaczyna i na jakim punkcie kodowym sie kończy
print(ord("a"))  # 97
print(ord("z"))  # 121

alphabet = ""

for i in range(ord("a"), ord("z") + 1):  # zakres od "a" (97) do "z" (121) + 1, żeby nie zakończyć na "y"
      #print(chr(i), end="") # abcdefghijklmnopqrstuvwxyz  # Alfabet bez polskich znaków
      alphabet += chr(i)  # dodawanie liter do zmiennej "alphabet"

print(alphabet)

print("a" in alphabet)     # True
print("abce" in alphabet)  # False
print()

#######################################################################################################################

# # NIEMUTOWALNOŚĆ CIĄGÓW ZNAKÓW

# # USUWANIE
# # del alphabet[0]  # TypeError --> Nie można usuwać pojedynczych elementów łańcucha znaków

# # Nie można usuwać pojedynczego znaku, ale można uzunąć cały string (wszystkie znaki)
# # del alphabet    # można usuwać stringi za pomocą metody del
# # print(alphabet) # pojawi się NameError - nie można odwołać się do nazwy, która została usunięta.


# # DODAWANIE
# # alphabet.append("asbss") # string nie posiada metody append(), update(), insert()

# # Do stringów można dodawać pojedyncze znaki - za każdym razem tworzymy nowy obiekt w pamięci komputera
# alphabet += "AAAA"
# print(alphabet) # abcdefghijklmnopqrstuvwxyzAAAA

#######################################################################################################################

# # WYKORZYSTANIE FUNKCJI MIN() I MAX()

# Funkcje MIN i MAX
print(min([1, 2, 3]))  # 1
print(max([1, 2, 3]))  # 3
print()
print(min("abcABC"))  # A - wartość punktu kodowego - duże "A" ma mniejszą wartość niż małe "a"
print(max("abcABC"))  # c - wartość punktu kodowego - małe "c" ma największą wartość kodową
print()
print(max("Ala ma kota."))  # t - wartość punktu kodowego = 116 (największa)
print()

#######################################################################################################################

# # WYKORZYSANIE FUNKCJI index(), list() i METODY count()

# Funkcja index() - zwraca indeks pierwszego wystąpienia danego argumentu (może to być znak lub podciąg)
print(alphabet.index("w"))  # literka "w" ma indeks 22
print("aAbByYzZAa".index("A"))  # 1 - funkcja indeks zwraca indeks pierwszego wystąpienia argumentu (zaczynamy od 0)
print("aAbByYzZAa".index("ZA"))  # 7 - indeks dla "Z" = 7.
print()

# Jest to bardzo podobne do działań na listach
print([1, 2, 3].index(3))  # 2 --> index dla 3 to wartość 2
print()


# Funkcja list() - za pomocą funkcji list() możemy w łatwy sposób zamienić ciąg znaków na listę.
print(list(alphabet))


# Zliczanie wystąpień danego znaku:
print(alphabet.count("a"))        # 1
print("Ala ma kota.".count("a"))  # 3
print([1, 1, 2, 2, 4].count(1))   # 2