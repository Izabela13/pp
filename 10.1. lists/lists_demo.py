# Przykład: jak przechhowywać wiele wartości

# jak przechowywć 5 liczb całkowitych
# a = 3
# b = 4
# c = 6
# d = 11
# e = 99
#
# print(a, b, c, d, e)

# Zamiast zapisu z użyciem pojedynczych zmiennych można wykorzystać listę
# Nie ma tutaj ograniczenia co do zakresu.
numbers = [3, 4, 6, 11, 99, 10, 10]
print(numbers)

# Nie ma ograniczenia tylko do liczb.
fruits = ["banan", "jabłko", "czereśnia"]
print(fruits)

# Listy są uporządkowane.
numbers = [1, 2, 3, 4, 5]
# jeżeli odwołamy się do listy, to elementy pojawią się w takiej kolejności, w jakiej zostały wprowadzone.

# Lista pozwala na dodawanie i usuwanie elementów.

# Lista może przechowywać duplikaty
# Jeżeli do listy wstawimy takie same elementy, lista będzie złożona z tych samych elementów.
numbers = [1, 1, 1, 1, 1, 1, 1] # to jest ok

# Lista może przechowywać różne wartości
fruits = ["banan", "jabłko", "czereśnia", 99, True] # mogą tu wpadać również typy bool

# Lista jest indeksowana od 0 od lewej i od -1 od prawej
print(fruits[0]) # banan
print(fruits[2]) # czereśnia

# Jeżeli odwołamy się do indeksu, który nie istnieje, otrzymamy wyjątek: "IndexError: list index out of range"

"""
indeks       0         1        2        3       4
fruits = ["apple", "banana", "cherry",  99,     True]
indeks      -5        -4       -3       -2      -1
"""

# Jeżeli weźmiemy indeks większy niż zakres elementów, to wyskoczy błąd - błąd zakresu
# Można sprawdzić zakres indeksów za pomocą funkcji len()
print(len(fruits)) # 5 (bo do lsity została dopisana liczba 99 i wartość "True").



# USUWANIE ELEMENTÓW Z LISTY
# jeżeli chcemy usunąć jakieś elementy, najprościej zastosować instrukcję del
print(fruits)
del fruits[-1] # jeżeli przy del nie wstawimy indeksu, czy zakresu indeksów, to instrukcja del usunie całą listę
print(fruits) # wynik: ['banan', 'jabłko', 'czereśnia', 99]



# ROZRÓŻNIENIE FUNKCJI I INSTRUKCJI
l = len(fruits) #funkcja - nie operuje na konkretnym obiekcie - operuje globalnie, zwraca wynik do zmiennej.
fruits.append("kiwi") # metoda operuje na danych - na konkretnym obiekcie, np. na liście. Nie musi zwracać wartości.
print(fruits) # Wynik: ['banan', 'jabłko', 'czereśnia', 99, 'kiwi']



# DODAWANIE OBIEKTÓW
# append to jedna z metod dodawania obiektów
# metoda insert
fruits.insert(0, "gruszka")
print(fruits)
# metodę insert stosuje się wtedy, kiedy obiekt ma zostać umieszczony w konkretnym miejscu, np. na samym początku.
# przy metodzie insert na samym początku używamy argumentu z indeksem, w który chcemy wstawić obiekt.
# wynik: ['gruszka', 'banan', 'jabłko', 'czereśnia', 99, 'kiwi'] - "gruszka" znajduje się na pozycji pierwszej (indeks 0)
