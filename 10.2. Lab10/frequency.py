"""
Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
występuje 3 razy.
"""
# hardcodowanie cyfr
ditgits = [1, 2, 4, 6, 6, 2, 6, 6] # zbiór cyfr

# w pętli zostaną zapisane częstotliwości wystąpień - zapisanie do listy frequency
# zmienna pomocnicza "frequency"
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# pierwszy element będzie określał ilość występowania 0, drugi 1, trzeci 2, itd. ile cyfr, tyle pozycji

# algorytm będzie sprawdzał, czy dana cyfra występuje, i nadpisywał ich ilość do odpowiednich pozycji (0-10)
for digit in ditgits: #pętla będzie musiała przejść po wszystkich cyfrach w liście "digits". Z listy "digits" będą wyciągane po kolei cyfry ("digit")
    frequency[digit] += 1 # częstotliwość - zwiększ "digit" o 1, np. digit = 1, zwiększ wystąpienie wartości 1 o 1.

print(frequency)
# tworzenie zmiennej pomocniczej - liczba najczęściej występująca
most_common = -1 # bo indeksuje się od 0
# musimy przejść po zbiorze "frequency"
for i in range(len(frequency)):
    if frequency[i] > most_common: # jeżeli element "frequency" o indeksie i jest większy od "most_common", to
        most_common = i # most common = i

print("Najczęściej występującą cyfrą jest " + str(most_common) + ",", "występuje", frequency[most_common], "razy.")
# w str(most_common) zawarty jest indeks najczęściej występującej cyfry - indeks = cyfra. W tym wypadku jest to i = 6.
# w "frequency[most_common] zawarta jest ilość wystąpień, czyli co kryje się pod indeksem i. W tym wypadku jest to 4.
# Odpowiedź: Najczęściej występującą cyfrą jest 6, występuje 4 razy.

# Podsumowując:
# [0, 1, 2, 0, 1, 0, 4, 0, 0, 0]
# do policzenia częstości wystąpień poszczególnych cyfr wykorzystano pomocniczną listę "frequency", w której
# poszczególne elementy listy (indeksy) reprezentowały poszczególne cyfry.
# Wartości cyfr (indeksów) reprezentowane są przez częstość wystąpień danej cyfry.

##################################################
print("")
#Wyjaśnienie

# mamy zakres liczb. Uźywamy listy dla tego zbioru.
digits_test = [1, 2, 1, 5] #zakładamy, że są to cyfry (czyli max może być 10 - od 0 do 9)

# predmiotem zadania było policzenie, 1) która cyfra występuje najwięcej razy i 2) ile razy występuje

# stworzenie listy pomocniczej, w której będzie zapisywana częstość występowania elementów
# początkowa wartość to same zera
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# jest to taki tymczasowy pojemniczek na informacje:
# |_|  |_|  |_|  |_|  |_|  |_|  |_|  |_|  |_|  |_|  - 10 przegródek
#  0    1    2    3    4    5    6    7    8    9   - przegródki mają roboczą nazwę "frequency", ale jest to indeksowanie

# przegródek używamy do tego, żeby niezależnie jak duża będzie wejściowa lista, wpisywać, która liczba i jakiej ilości występowała
# cyfry, które są liście poczatkowej można uznać za indeksy. Zliczane są wystąpienia danego indeksu.
# algorytm: indeks 0 reprezentuje 0-ra, indeks 1 reprezentuje 1-ynki, indeks 2 reprezentuje 2-ójki, itd.

# jak to się prezentuje dla testowego zbioru [1, 2, 1, 5]
# # |0|  |2|  |1|  |0|  |0|  |1|  |0|  |0|  |0|  |0|
# #  0    1    2    3    4    5    6    7    8    9

# pierwsza część programu przechodzi po wszystkich elementach i podnosi wartość komórki o danym indeksie (na początku z 0 do 1).
# dla tablicy "frequency" tam, gdzie jest indeks, np. 1 program robi "frequency += 1":
# frequnency[1] = frequency[1] + 1
# frequnency[2] = frequency[2] + 1
# frequnency[1] = frequency[1] + 1
# frequnency[5] = frequency[5] + 1

print(digits_test)
for digit in digits_test:
    frequency[digit] += 1

print(frequency) # [0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0]

# Matryca [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] to umowny zapis.
