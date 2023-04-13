# # Zadanie 1: alphabet

# # Nie próbować generować alfabetu z polskimi znakami

# alphabet = "aąbcćdeęfghijklłmnńoópqrstuvwxyzźż"

# # Korzystamy z właściwości typu string - po stringu można iterować, ponieważ jest to sekwencja

# for c in alphabet:
#     print(c, ord(c))



# Zadanie 2: string_statistics funkcja generująca ciąg znaków
"""
PRZYPOMNIENIE

lista [1, 2, 3]
- odwołanie po indeksach (np. lista[0])
- uporządkowany zbiór elementów. Kolejność wyciągania elementów jest zachowana
- modyfikowalna sekwencja - elementy można usuwać i dodawać

krotka (1, 2, 3)
- bardzo podobna do listy
- można odwoływać się do elementów po indeksach
- uporządkowany zbiór elementów. Kolejność wyciągania elementów jest zachowana
- nie jest mutowalna - nie można usuwać i dodawać elementów. Żeby dodawać lub usuwać elementy trzeba stworzyć nowy
obiekt i przepisać wszystkie elementy, które mają się w nim znaleźć (powiększone lub pomniejszone w stosunku do
oryginalnej, pierwotnej krotki).

słownik {"a": 1, "b": 2}
- wartość klucz:wartość
- nie jest sekwencją, bezpośrednio nie można po nim iterować. Pętlą można przejść po elementach słownika - po kluczach,
wartościach albo po całych zestawach (itemach)
- element są uporządkowane (od pewnej wersji Pythona)
- klucze wstawione do słownika nie mogą się powtarzać - klucz jednoznacznie identyfikuje daną wartość w słowniku

ciąg znaków string ="abcde"
- sekwencja
- podobny do krotki - niezmienny
"""


"""
Istotne jest - implementacja funkcji, funkcja jest skrzynką, do której wrzucamy jakieś dane i te dane później wyciągamy.
Tak więc z jednej strony mamy jakieś wejście, z drugiej strony mamy jakieś wyjście.
--> wejście - przekazanie jako argument ciągu znaków
--> wyjście - zwrócić obiekt typu słownik

Jeżeli chcieć stworzyć zaślepkę, to funkcja posiadać będzie na wstępie takową formę:

    def count_letters(string):
        return {}

Skrypt z użyciem tej funkcji powinien zadziałać, mimo że na tym etapie zwróci {}.
"""

string = "abracadabra"

def count_letters(string): # ciag znaków jest naszym parameterem wejściowym
    stats = {}  # wiemy z zadania, że funkcja ma zwrócić obiekt typu słownik. Możemy zdefiniować słownik na początku.
    # Musimy przejść po każdym znaku ciągu i sprawdzić, czy mamy go zliczyć. Iterowanie po ciągu znaków
    for char in string:  # wyciągamy każdy znak do zmiennej "char"
        if char in stats:  # stats.keys(): przypadek, gdy literka jest już w słowniku (element o danym kluczu)
            stats[char] += 1  # już jakaś literka jest w słowniku, zwiększamy wartość dla klucza (dla tej literki)
        else:
            stats[char] = 1  # dla tego klucza przypisujemy wartość 1 (literki jeszcze nie ma i trzeba ją dodać)

    return stats  # zwracanie słownika "stats" - element wyjściowy


print(count_letters(string))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
print(count_letters("abcabc"))
print(count_letters("Ala ma kota, a kot ma Alę."))



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