"""
Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
liczbę jedynek w ciągu bitów reprezentujących tę liczbę.
"""

# Pobieranie od użytkownika liczby całkowitej
user_number = int(input("Podaj dowolną liczbę całkowitą: "))


# Zamiana liczby całkowitej podanej przez użytkownika na ciąg bitów
user_number_as_bin = str(bin(user_number))
# print(user_number_as_bin)


# Zliczanie 1-nek w pętli
counter = 0  # ustawienie licznika na wartość początkową równą 0

for one in user_number_as_bin:
    if one == "1":
        counter += 1

# print(counter)

print("W liczbie " + str(user_number) + " zamienionej na ciąg bitów wartość 1 występuje "
      + str(counter) + " razy (" + user_number_as_bin + ").")