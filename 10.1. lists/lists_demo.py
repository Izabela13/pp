# jak przechowywć 5 liczb całkowitych
# a = 3
# b = 4
# c = 6
# d = 11
# e = 99
#
# print(a, b, c, d, e)

numbers = [3, 4, 6, 11, 99, 10, 10]
print(numbers)

fruits = ["banan", "jabłko", "czereśnia"]
print(fruits)

#Lista pozwala na dodawanie i usuwanie elementów.
#Lista może przechowywać duplikaty

numbers = [1, 1, 1, 1, 1, 1, 1] # to jest ok

#Lista może przechowywać różne wartości
fruits = ["banan", "jabłko", "czereśnia", 99, True] # mogą tu wpadać również typy bool

#Lista jest indeksowana od 0 od lewej i od -1 od prawej
print(fruits[2])

"""
indeks       0         1         2
fruits = ["apple", "banana", "cherry"]
indeks      -3        -2        -1
"""

#Jeżeli weźmiemy indeks większy niż zakres elementów, to wyskoczy błąd - błąd zakresu



# USUWANIE ELEMENTÓW Z LISTY
print(fruits)
del fruits[-1] # jeżeli przy del nie wstawimy indeksu, czy zakresu indeksów, to instrukcja del usunie całą listę
print(fruits)


# ROZRÓŻNIENIE FUNKCJI I INSTRUKCJI
l = len(fruits) #funkcja - nie operuje na konkretnym obiekcie - operuje globalnie
fruits.append("kiwi")# metoda operuje na danych - na konkretnym obiekcie


# DODAWANIE OBIEKTÓW
# append to jedna metoda
# metoda insert
fruits.insert(0, "gruszka")
print(fruits)