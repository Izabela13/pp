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



# Pozbywanie się duplikatów

user_unique_numbers = []  # pusta lista, do której będą wprowadzane unikatowe wartości

for element in user_numbers:
    if element not in user_unique_numbers:
        user_unique_numbers.append(element)



# Sortowanie w kolejności malejącej

#user_numbers.sort(reverse=True)
user_unique_numbers.sort(reverse=True)

print("")
#print("Oto lista wprowadzonych przez Ciebie liczb całkowitych, posortowanych malejąco: " + str(user_numbers) + ".")
print("Oto lista wprowadzonych przez Ciebie liczb całkowitych, posortowanych malejąco oraz bez duplikatów: " +
      str(user_unique_numbers) + ".")