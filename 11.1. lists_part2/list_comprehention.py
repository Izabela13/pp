# WYRAŻENIA LISTOWE


# # Definiowanie pustej listy.
numbers = [] # pusta lista

# # Generowanie list za pomocą pętli - wstawianie elementów.
# for i in range(1, 1001): # ładowanie elementów od 1 do 1000 (1001 już nie wchodzi do zakresu)
#     numbers.append(i)
#
# print(numbers)


# Za pomocą wyrażeń listowych - tę samą pętlę można wykonać w jednej linijce.
# Zamiast definicji pustej listy można od razu wprowadzić do nowej listy wartości.
numbers = [i for i in range(1, 1001)]  # "i" dla "i" w "range od 1 do 1000".
print(numbers)


# Co zrobić, jeśli chcemy, żeby wartości nie były szablonowe?
# Pod iterator można podstawić dowolną inną wartość. Jeżeli chcemy, żeby nasza lista miała 1000 elementów,
#  a wszystkie elementy ustawione na 99, pod "i" podstawiamy daną wartość, którą chcemy uzyskać.
numbers = [99 for i in range(1, 1001)]  # 1000 elementów o wartości 99
print(numbers)


# Można też wykonać jakieś działania:
numbers = [i ** 2 for i in range(1, 101)] # podnoszenie do potęgi wartości, np. od 1 do 100.
print(numbers) # w efekcie dostaniemy listę 100-elementową, gdzie każdy element został podniesiony do kwadratu.


# Dla mechanizmu wyrażeń listowych mamy instrukcje warunkowe, które można postawić na samym końcu.
numbers = [i ** 2 for i in range(1, 101) if i % 2 == 0]  # np. interesują nas liczby od 1 do 100, ale tylko parzyste
print(numbers) # w tym wypadku dostaniemy podzbiór 50 elementów podniesionych do kwadratu.


# Chcemy dowiedzieć się, ile liczb w przedziale od 1 do 300 dzieli się przez 3 i 7 (jednocześnie).
numbers_choosen = [i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]
print(len(numbers_choosen))

# Całe obliczenie w jednej linijce kodu:
# 1. Chcemy wyświetlić --> funkcja print()
# 2. Chcemy zbadać, ile elementów --> funkcja len()
# 3. Badamy listę elementów od 1 do 300 --> i for i in range(1, 301)
# 4. Warunki - mamy sprawdzać, czy i jest podzielne przez 3 i przez 7 jednocześnie
print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))  # 14