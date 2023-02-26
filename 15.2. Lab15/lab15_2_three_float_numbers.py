"""
2. Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
Uwzględnij możliwość pomyłki użytkownika.
"""

print("Podaj trzy liczby zmiennoprzecinkowe.")

counter = 1
float_list = []

while counter <= 3:
    try:
        number = float(input("Podaj " + str(counter) + " liczbę zmiennoprzecinkową: "))
        float_list.append(number)
        counter += 1
    except:
        print("To nie jest liczba.")

print(float_list)