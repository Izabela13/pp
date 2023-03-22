"""
2. Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
Uwzględnij możliwość pomyłki użytkownika.
"""

print("Podaj trzy liczby zmiennoprzecinkowe. \n")

counter = 1
floating_numbers = []

while counter <= 3:
    try:
        number = float(input("Podaj " + str(counter) + " liczbę zmiennoprzecinkową: "))
        floating_numbers.append(number)
        counter += 1
    except:
        print("Podana wartość nie jest liczbą. Spróbuj ponownie. \n")

print("")
print("Wprowadzone liczby:", floating_numbers)