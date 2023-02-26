# numbers = (1, 2, 3)  # to jest krotka
# numbers = 1, 2, 3 # tak też można zapisać
# numbers = () # pusta krotka

# Jeżeli chcemy zapisać jedną wartość, to trzeba dodać przecinek na końcu:
# numbers = (1, ) # bez tego przecinka interpreter odczyta to jako liczbę w nawiasach

#numbers = (1, 2, 3)

# for i in numbers:
#     print(i)
# działa dokładnie jak lista

# print(numbers[1:2]) # Kopia krokti: (2,)


# Wyrażenia listowe
numbers = tuple(x for x in range(10))
print(numbers)
# Wynik: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Krotki są niemutowalne, np.
# numbers[0] = 999 #Pojawi się wyjątek Type Error

# Nie możemy usunąć żadnego elementu
# del numbers[0] # Type Error - nie da się usuwać elementów w tupli
# Można jedynie usunąć CAŁĄ kroktę
# del numbers



# OPERACIE NA KROTKACH:
# sprawdzanie, ile ma elementów

# można używać operatora mnożenia - pomnoży całą krotkę, np.
# print(numbers * 2) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# Na zasadzie odczytu, a nie modyfikacji.

# można dodawać krotki
# print(numbers + numbers)


numbers = [1, 2, 3]
numbers = tuple(numbers)

print(numbers) # (1, 2, 3)

napis = "Ala ma kota"
napis = tuple(napis)

print(napis) # ('A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a')