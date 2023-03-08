# GRA LOSUJĄCA
# Wylosuj 3 liczby od 1 do 10, przy czym nie chcemy, aby te liczby się powtarzały.
# Mają być posortowane w kolejności rosnącej.

import random

random_numbers = []  # umieszczanie wylosowanych liczb w liście



# # I rozwiązanie, ale nie spełniające warunku losowania tylko niepotwarzających się liczb
# Iterowanie tyle razy, ile mamy wylosować liczb.
for i in range(3):
    random_numbers.append(random.randint(1, 10)) # do listy zostaną dodane wylosowane liczby od 1 do 10
random_numbers.sort()
print(random_numbers)
# Randint nie zapewnia losowania niepowtarzających się wartości.



# # II rozwiązanie, ale mogące spowodować problemy z wydajnością przy większych zbiorach
# Trzeba zmienić pętlę na while - losuj dopóki liczby nie będą się powtarzać

counter = 3 # potrzebna jest zmienna pomocnicza. Będzie ona zliczała liczbę losowań
random_numbers = []
while counter:  # LOSUJ DOPÓKI COUNTER. Co to znaczy? Pętla będzie działać, dopóki "counter" będzie mieć wartość <> 0
    number = random.randint(1, 10)  # oddzielne losowanie liczb i wstawianie jej do zmiennej "number"
    if number not in random_numbers: # sprawdzenie za pomocą instrukcji warunkowej, czy wylosowana liczba nie znajduje się w zbiorze wylosowanych liczb
        random_numbers.append(number) # liczba zostanie dodana, jeżeli nie ma jej jeszcze w zbiorze
        counter -= 1 # jeżeli liczba się nie powtarza i została dodana do zbioru, można zmniejszyć counter

random_numbers.sort()
print(random_numbers)
# Co jest słabością tego rozwiązania?
# Problem jest z wydajnością - może się okazać, że program będzie w koło losował tę samą liczbę.



# # III rozwiązanie za pomocą funkcji sample
# sample - losowanie dowolnej ilości liczb z podanego zbioru, bez powtórzeń
# na początku trzeba stworzyć zbiór, z którego będziemy losować
numbers = [i for i in range(1, 11)] # wyrażenie listowe
random_numbers = random.sample(numbers, 3) # zbiór nie będzie pustą listą.
# W module random jest funkcja sample(). Funkcja przyjmuje dwa parametery:
# 1. zbiór, z którego nastąpi losowanie
# 2. ile elementów ma zostać wylosowanych

random_numbers.sort() # na samym końcu nastąpi sortowanie

print(random_numbers)