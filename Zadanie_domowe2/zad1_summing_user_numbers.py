"""
Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
• program powinien pobierać od użytkownika liczby całkowite,
• niepodanie liczby powinno zakończyć wprowadzanie danych,
• program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.
"""

# CZĘŚĆ I. Pobieranie liczb całkowitych od użytkownika.

# Pobierane od użytkownika liczby będą zapisywane do listy
user_numbers_list = []


print("Wprowadź dowolne liczby całkowite, które będą stanowić Twój zbiór.")
print("Po zakończeniu wprowadzania liczb nastąpi sumowanie osobno liczb parzystych i nieparzystych.")

counter = 1  # licznik wprowadzanych liczb

while True or 0:
    user_number = input("Podaj " + str(counter) + " liczbę: ")
    if user_number == "":
        break
    else:
        counter += 1
        user_number = int(user_number)
        user_numbers_list.append(user_number)

print("")
print("Zbiór prezenetuje się następująco: " + str(user_numbers_list) + ". \n")



# CZĘŚĆ II. Podawanie sumy liczb parzystych i sumy liczb nieparzystych.

# Tworzenie list zawierających osobno liczby parzyste i nieparzyste
user_numbers_even = []  # lista liczb parzystych
user_numbers_odd = []   # lista liczb nieparzystych

for number in user_numbers_list:
    if number % 2 == 0:
        user_numbers_even.append(number)
    else:
        user_numbers_odd.append(number)

print("Suma wyłącznie liczb parzystych w podanym zbiorze to: " + str(sum(user_numbers_even)) + ".")
print("Suma wyłącznie liczb nieparzystych w podanym zbiorze to: " + str(sum(user_numbers_odd)) + ".")