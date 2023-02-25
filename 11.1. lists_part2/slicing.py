# slicing ma być remedium na charakterystyczny typ list

list_1 = [9]
list_2 = list_1[:] # robienie kopii od początku do końca listy
# lista_2 = [list_1]

# operacja z podmianą elementów dla listy 2
list_2[0] = 13
print(list_2)
print(list_1) # zabieg wycinania listy, który tworzy oddzielną listę, przechowywany jest w innym obszarze pamięci komputera


numbers = [10, 8, 6, 4, 2]

#jak to tnie
# dla listy numbers chcemy stworzyć całkiem nową listę
new_numbers = numbers[1:3] # chcemy wziąć 8 i 6
print(new_numbers)

# lista new_numbers to teraz oddzielny obiekt, który nie wływa na listę numbers

#           -5  -4 -3 -2 -1
# numbers = [10, 8, 6, 4, 2]

new_numbers = numbers[-4: -2]
print(new_numbers)

# kopiowanie całej listy [:] lub [0: len(numbers)]



# Usuwanie wycinków
numbers = [10, 8, 6, 4, 2]

del numbers[1:3] # del to instrukcja

print(numbers)
# [10, 4, 2]

# instrukcją del można również usunąć całą listę. Wówczas dostaniemy wyjątek, bo lista zniknie