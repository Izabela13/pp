"""
Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
występuje 3 razy
"""

# zbiór oryginalny
numbers_org = [4, 1, 9, 2, 9, 1, 9, 4, 1, 4]

# zbiór, który zmieni kolejność elementów
numbers = [4, 1, 9, 2, 9, 1, 9, 4, 1, 4]

# sortowanie elementów listy
numbers.sort()
# print(numbers)

# zliczanie wystąpień
frequency = [] # lista podsumowująca ilość wystąpień tych samych elementów w posortowanej liście "numbers"

for number in numbers:
    frequency.append(numbers.count(number))
# print(frequency)


# wydobywanie unikatowych wartości z listy "numbers" i "frequency".

# Lista "frequency" zachowuje kolejność wystąpień poszczególnych elementów z listy "numbers".
# Kolejnym krokiem jest ograniczenie listy "numbers" tylko do unikatowych wartości.
# Lista "frequency" zachowa częstość wystąpień poszczególnych elementów listy "numbers".

numbers.append("end") # dodanie sztucznej wartości do listy, która to wartość nie będzie wchodziła do iteracji
# za każdą iteracją element bieżący będzie porównywany do elementu

# stworzenie list, do których będą zapisywane wartości
uniq_occur_numb = [] # lista unikatowych wartości
uniq_frequency_numb = [] # lista wystąpień poszczególnych elementów

i = 0
while i + 1 < len(numbers):
    if numbers[i] != numbers[i + 1]:
        uniq_occur_numb.append(numbers[i])
        uniq_frequency_numb.append(frequency[i])
    i += 1

# print(uniq_occur_numb)
# print(uniq_frequency_numb)

most_freq = max(uniq_frequency_numb) # zapisanie najwyższej wartości wystąpień do zmiennej
# print(most_freq)

ind = 0 # iterator przeznaczony do wyciągania tych indeksów z listy "uniq_frequency_numb", w które pojawiły się najczęściej
which_index = [] # do tej listy będą zapisywane indeksy tych liczb, które pojawiły się największą ilość razy

while ind < len(uniq_frequency_numb):
    if uniq_frequency_numb[ind] == most_freq:
        which_index.append(ind) # dodawanie do listy indeksów tych liczb, które najczęściej się pojawiały
    ind += 1

# print(which_index)

print("W zbiorze", numbers_org, "najczęściej występująca wartość to:")
for winner_ind in which_index:
    if uniq_occur_numb[winner_ind] and uniq_frequency_numb[winner_ind]:
        print(uniq_occur_numb[winner_ind], "występująca", uniq_frequency_numb[winner_ind], "razy.")