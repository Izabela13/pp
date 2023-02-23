"""
Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
na ekranie, przy czym:
• program zapyta użytkownika o zakres minimum oraz maksimum,
• będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
• będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
• będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
• wyświetli wylosowane serie liczb.
"""

import random

print("Podaj zakres minimum i maksimum, aby otrzymać losową liczbę serii o losowej ilości liczb całkowitych.")

# Program pyta użytkownika o zakres minimum oraz maksimum.
user_min = int(input("Podaj liczbę całkowitą stanowiącą minimum zakresu: "))
user_max = int(input("Podaj liczbę całkowitą stanowiącą maksimum zakresu: "))
print("")



# Losowanie LICZBY LICZB do wylosowania z zakresu podanego przez użytkownika
drawn_number_for_amount = random.randint(user_min, user_max)  # zapisanie wylosowanej liczby do zmiennej

# Zakres liczb całkowitych może zawierać wartości ujemne.
# Gdy wylosowana liczba liczb w serii będzie ujemna, zostanie odwrócona na dodatnią.
drawn_number_for_amount_abs = 0  # abs = absolute value
if drawn_number_for_amount < 0:
    drawn_number_for_amount_abs = drawn_number_for_amount * -1
else:
    drawn_number_for_amount_abs = drawn_number_for_amount


# Losowanie LICZBY SERII LICZB do wylosowania z zakresu podanego przez użytkownika,
drawn_number_of_series = random.randint(user_min, user_max)  # zapisanie wylosowanej liczby serii do zmiennej

# Zakres liczb całkowitych może zawierać wartości ujemne.
# Gdy wylosowana liczba serii liczb będzie ujemna, zostanie odwrócona na dodatnią.
drawn_number_of_series_abs = 0  # abs = absolute value
if drawn_number_of_series < 0:
    drawn_number_of_series_abs = drawn_number_of_series * -1
else:
    drawn_number_of_series_abs = drawn_number_of_series


print("Z podanego zakresu minimum i maksimum wylosowano liczbę: \n"
      "-> |" + str(drawn_number_for_amount) + "|, która będzie stanowić ilość LICZB w serii. \n"
      "-> |" + str(drawn_number_of_series) + "|, która będzie stanowić ilość SERII liczb. \n")



# Losowanie serii liczb
adminicular_list = []  # lista pomocnicza
drawn_series_of_numbers = []  # wylosowane serie liczb

series = 0

while series < drawn_number_of_series_abs:
    for amount in range(drawn_number_for_amount_abs):
        adminicular_list.append(random.randint(user_min, user_max))
    series += 1
    drawn_series_of_numbers.append(adminicular_list)
    adminicular_list = []

## print(drawn_series_of_numbers)



# Wyświetlanie wylosowanych serii liczb
if drawn_number_for_amount_abs == 0 or drawn_number_of_series_abs == 0:
    print("Brak wartości do wyświetlenia.")
    if drawn_number_for_amount_abs == 0 and drawn_number_of_series_abs != 0:
        print("0 liczb do wylosowania.")
    elif drawn_number_for_amount_abs != 0 and drawn_number_of_series_abs == 0:
        print("0 serii do wylosowania.")
    elif drawn_number_for_amount_abs == 0 and drawn_number_of_series_abs == 0:
        print("0 liczb i serii do wylosowania.")
else:
    print("Oto serie wylosowanych liczb z zakresu od " + str(user_min) + " do " + str(user_max) + ":")

    i = 0  # indeks
    for number_series in range(len(drawn_series_of_numbers)):
        print((str(i+1) + ":"), drawn_series_of_numbers[i])
        i += 1