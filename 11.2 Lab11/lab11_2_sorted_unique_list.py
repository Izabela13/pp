"""
2. Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
duplikatów.
"""

# Pobieranie od użytkownika serii liczb całkowitych.

user_numbers = []

user_range = int(input("Podaj, jaki zakres liczb całkowitych chcesz wprowadzić: "))
print("")
print("Wprowadź po kolei liczby.")

counter = 1 # licznik kolejnych pozycji

for number in range(user_range):
    user_number = int(input("Podaj " + str(counter) + " liczbę: "))
    user_numbers.append(user_number)
    counter += 1



# Sortowanie malejące listy użytkownika i pozbywanie się duplikatów

user_numbers.sort(reverse=True)
user_unique_numbers = []

i = 0 # indeks

while i + 1 <= len(user_numbers):
    if i + 1 < len(user_numbers) and user_numbers[i] != user_numbers[i + 1]:
        user_unique_numbers.append(user_numbers[i])
    elif i + 1 == len(user_numbers) and (user_numbers[-1] != user_numbers[-2] or user_numbers[-1] == user_numbers[-2]):
        user_unique_numbers.append(user_numbers[-1])
    i += 1

user_unique_numbers.sort(reverse=True)

print("")
print("Oto lista wprowadzonych przez Ciebie liczb całkowitych, posortowanych malejąco: " + str(user_numbers) + ".")
print("Oto lista wprowadzonych przez Ciebie liczb całkowitych, posortowanych malejąco oraz bez duplikatów: " +
      str(user_unique_numbers) + ".")