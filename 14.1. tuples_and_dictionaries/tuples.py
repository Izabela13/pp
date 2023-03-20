# # KROTKI

# # JAK ZAPISAĆ KROTKĘ
# numbers = (1, 2, 3)  # to jest krotka
# numbers = 1, 2, 3 # taką samą krotkę jak wyżej można zapisać też bez nawiasów
# numbers = () # pusta krotka

# # Jeżeli chcemy zapisać jedną wartość do krotki, trzeba dodać przecinek na końcu:
# numbers = (1, ) # bez tego przecinka interpreter odczyta taki zapis jako liczbę w nawiasach
# # Po użyciu funkcji print() na konsoli również wyświetli się krotka z przecinkiem: (1,)



# # STOSOWANIE INDEKSÓW W KROTKACH
# # Przy krotkach działają te same mechanizmy co przy listach, np. można stosować nawiasy kwadratowe, żeby dostać się
# # przez indeksy do odpowiednich elementów. Działają indeksy ujemne.
# numbers = (1, 2, 3)
# print(numbers[0])
# print(numbers[-2])


# # Przy krotkach iteruje się dokładnie tak samo jak przy listach.
# for i in numbers:
#     print(i)
# # działa dokładnie jak lista


# # Można stosować wycinki
# print(numbers[1:2]) # Kopia krotki: (2,)
# print(numbers[:]) # Cała kopia krotki: (1, 2, 3)



# # WYRAŻENIA LISTOWE - mała róźnica - nawiasy kwadratowe są zarezerwowane dla listy.
numbers = tuple(x for x in range(10)) # GENERATOR WYRAŻEŃ (GENERATOR EXPRESION) - zamiast nawiasów kwadratowych...
print(numbers) # ... stosuje się słowo kluczowe "tuple" i nawiasy okrągłe ().
# # Wynik: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# # Zamiast słowa kluczowego "tuple" można użyć słowa kluczowego "list". Wówczas generator wyrażeń wygeneruje listę:
# numbers = list(x for x in range(10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]



# # RÓŻNICE KROTEK W STOSUNKU DO LIST

# # NIEZMIENNOŚĆ (IMMUTABLENESS) 1
# # Krotki są niemutowalne (jak stringi czy jak liczby całkowite). Podmiana elementu o indeksie 0 na np. 9999 ...
# numbers[0] = 9999  # ... spowoduje pojawienie się wyjąteku Type Error
# # Składniowo wszystko jest poprawnie, nic nie budzi watpliwości, natomiast semantycznie nie można zmieniać obiektu,
# # nie można przypisać wartości do już istniejącego obiektu.

# # NIEZMIENNOŚĆ (IMMUTABLENESS) 2
# # Nie możemy usunąć żadnego elementu z krotki, np.
# del numbers[0]  # ten zapis zareaguje błędem Type Error - "Obiekt krotki nie wspiera usuwania elementów"
# # Nie da się usuwać elementów w tupli. Można jedynie USUNĄĆ CAŁĄ KROTKĘ.
# del numbers  # Po usunięciu krotki nie będzie już można odwołać się do niej i przy próbie wykonania print()
# # użytkownik dostanie błąd "NameError", ponieważ takiej krotki już nie będzie.



# # OPERACIE NA KROTKACH:
# # 1. Sprawdzanie, ile krotka ma elementów (wykorzystanie funkcji len() jak w przypadku list).
print(len(numbers))  # 10 (wcześniej użyto wyrażenia listowego "numbers = tuple(x for x in range(10))"

# # 2. Można używać OPERATORA MNOŻENIA, natomiast operator mnożenia NIE POMNOŻY WSZYSTKICH ELEMENTÓW KROTKI razy ileś,
# #    ale POMNOŻY CAŁĄ KROTKĘ (ZMULTIPLIKUJE, POWIELI CAŁĄ KROTKĘ) wskazaną ilość razy.
print(numbers * 2)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# # 3. Można używać OPERATORA DODAWANIA - dodawać krotki na zasadzie "sklejania"
print(numbers + numbers)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Operacje mnożenia (multiplikacji) i dodawania (łączenia) tylko na zasadzie odczytu, a nie modyfikacji.
# # Gydby chcieć coś zmieniać w tupli, nawet nie będzie na to stosownej metody, np.
# # numbers.append(111) # dodanie na siłę metody append() spowoduje zwrócenie wyjątku AttributeError (brak metody)

# # 4. KONWERSJA
# # Często zachodzi potrzeba poruszania się między listami a krotkami.
numbers = [1, 2, 3]  # Jeżeli listę chcemy zmienić na krotkę, wystarczy dla tej listy użyć "tuple"
numbers = tuple(numbers) # działa to podobnie jak zamiana liczby na stringa i na odwrót
print(numbers) # (1, 2, 3)

# # Konwersja działa również z ciągami znaków.
napis = "Ala ma kota"
napis = tuple(napis) # cały ciąg znaków zostaje przekonwertowany na krotkę
print(napis) # ('A', 'l', 'a', ' ', 'm', 'a', ' ', 'k', 'o', 't', 'a')