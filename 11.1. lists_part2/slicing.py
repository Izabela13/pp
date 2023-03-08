# # WYCINANIE - SLICING

# slicing ma być remedium na charakterystyczny typ list

list_1 = [9]
list_2 = list_1[:] # robienie kopii całej listy - od początku do końca listy (sam dwukropek [:])
# Pojawi się teraz kopia listy "list_1" w liście "list_2". Od tego momentu w pamięciu komputera będą funkcjonowąły
# dwie niezależne listy oraz dwie niezależne nazwy, które będą wskazywąły na dwie niezależne listy.
# lista_2 = [list_1]

# operacja z podmianą elementów dla listy "list_2"
list_2[0] = 13
print(list_2) #[13] - zmieniona została tylko lista "list_2".
print(list_1) #[9] - lista "list_1" nie uległa zmianie.
# NIE UŻYTO METODY PRZYPISANIA, ALE KOPIOWANIA --> w pamięci komputera istnieją dwie niezależne listy.
# zabieg wycinania listy, który tworzy oddzielną listę, przechowywany jest w innym obszarze pamięci komputera



# jak to tnie?

# mamy listę "numbers"
numbers = [10, 8, 6, 4, 2]

# dla listy numbers chcemy stworzyć całkiem nową listę
new_numbers = numbers[1:3] # chcemy wziąć 8 i 6 (wycinek - jakaś część listy numbers)
print(new_numbers) # Wynik: [8, 6]

# INDEKSY   0   1   2   3   4
# NUMBERS: 10,  8,  6,  4,  2
# Jeżeli do nowej listy mają trafić elemenetny [1:3], oznacza to, że brane będą elementy od drugiej pozycji (indeks 1)
# do pozycji 2, bez 3 (indeks 3 to koniec zakresu, który zostaje pominięty).


# Lista "new_numbers" to teraz oddzielny obiekt (oddzielne miejsce w pamięci komputera), który nie wpływa na listę "numbers".


# Do list można odwoływać się przez indeksy ujemne
# INDEKSY   -5  -4  -3  -2  -1
# numbers = [10, 8,  6,  4,  2]

new_numbers = numbers[-4: -2] # dokładnie ten sam efekt, co przy indeksach [1:3]
print(new_numbers) # Wynik: [8, 6]


# Może wystąpić również kombinacja indeksów ujemnych i dodatnich, np.
new_numbers = numbers[-4:3]
print(new_numbers) # Wynik: [8, 6]

# INDEKSY +  0   1   2   3   4
# INDEKSY - -5  -4  -3  -2  -1
# numbers = [10, 8,  6,  4,  2]

# Trzeba uważać na logiczne stosowanie indeksów, np. new_numbers = numbers[4:3] spowoduje powstanie pustej listy.




# KOPIOWANIE CAŁEJ LISTY: [:] lub [0: len(numbers)]
new_numbers = numbers[:]
print(new_numbers) # Wynik: [10, 8, 6, 4, 2]

new_numbers = numbers[0:len(numbers)]
print(new_numbers) # Wynik: [10, 8, 6, 4, 2]




# USUWANIE WYCINKÓW
# Listy można modyfikować przez stosowanie wycinków
numbers = [10, 8, 6, 4, 2]

# Zadanie: wyciąć element 8 i 6
del numbers[1:3] # del to instrukcja. Funkcja ma nawiasy okrągłe.

print(numbers)
# [10, 4, 2]

# instrukcją del można również usunąć całą listę.
del numbers[:] # wszystkie elementy z listy zostaną wycięte
print(numbers) # []
# W efekcie powstanie pusta lista


# Aby usunąć całą listę, po instrukcji "del" należy wpisać listę do usunięcia
# del numbers
# Wówczas dostaniemy wyjątek dotyczący tego, że nie ma danej nazwy, ponieważ lista zniknie