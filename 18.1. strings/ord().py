# # PUNKT KODOWY DLA ASCII UNICOD OD OKREŚLONEGO ZNAKU

char1 = "a"
char2 = " "

# Wyświetlanie punktów kodowych dla wartości w zmiennych "char1" i "char2"
print(ord(char1))  # 97
print(ord(char2))  # 32
print()


# Wyświetlenie informacji o punkcie kodowym litery "ę"
print(ord("ę"))  # 281 - wychodzi poza 256 możliwości kodowania

#######################################################################################################################

# Jak można dojść do tego, jaki to jest znak Unicode?
# Można pobrać wartość heksadecymalną - wystarczy podstawić wartość puntku kodowego (dziesiętnego) do funkcji hex().
print(hex(ord("ę")))  # 0x119
# Wartość heksadecymalna, w przykładzie wartość 0x119 to wartość, która zaprowadzi nas do kodu Unicode dla tego znaku.

# Wyświetlanie znaku Unicode o kodzie u0119:
print("\u0119") # ę --> Za pomocą "\" i "u" ("\u") generujemy kod znaku Unicode.
# W dwóch znakach zakodowany jest heksadecymalny jeden bajt (01) i drugi bajt (19).
# "\u" --> "Wyświetl mi znak Unicode o kodzie 01 19".
print()

#######################################################################################################################

# Jak działa kodowanie UTF-8 (sposób zapisania w pamięci komputera znaku o danym standardzie, np. ASCII lub Unicode).
"""
Wyświetlanie informacji o znakach "a" i "€":
1) znak 
2) punkt kodowy --> ord()
3) wartość hexa dla danego punktu kodowego --> hex(ord())
4) liczba bajtów, które zajmuje dany znak/ liczba bajtów potrzebna do zakodowania danego znaku --> encode()

encode() zwróci konkretne bajty, które będą potrzebne do zakodowania konkretnego znaku
"""

c = "a"  # "c" od "char"
print(c, ord(c), hex(ord(c)), c.encode())  # a 97 0x61 b'a' - znak "a" jest kodowany w jednym bajcie
"""
1) znak "a" 
2) punkt kodowy = 97
3) heksadecymalnie znak "a" to 61 (0x61)
4) jest zakodowany jako znak "a", czyli jako jeden bajt,

97 mieści się w zakresie od 0 do 127, więc do zakodowania tego znaku "a" wystarcza tylko jeden bajt.
"""

print()

c = "\u20AC" # nie ma znaczenia wielkość liter
print(c) # €
print(c, ord(c), hex(ord(c)), c.encode()) # € 8364 0x20ac b'\xe2\x82\xac'
"""
1) znak "€" 
2) punkt kodowy = 8364
3) heksadecymalnie znak "€" to 20AC (0x20ac)
4) jest zakodowany na 3 bajtach: 1 bajt = e2; 2 bajt = 82, 3 bajt = ac

Żeby zakodować i wyświetlić znak Euro, trzeba zająć w pamięci komputera 3 bajty (kodowanie za pomocą UTF8).
"""