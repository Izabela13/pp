# # PROGRAM POBIERAJĄCY OD UŻYTKOWNIKA 5 LICZB CAŁKOWITYCH

# # Stworzymy tablicę numbers

numbers = []

# for i in range(5):  # Od użytkownika będziemy pobierać w pętli 5 liczb całkowitych
#     n = int(input("Podaj liczbę całkowitą: "))  # liczby zapisywane będą do zmiennej "n"
#     numbers.append(n)  # następnie liczby będą zapisywane (dodawane) do listy "numbers"
# print(numbers) # wprowadzenie stringa spowoduje wystąpienie "ValueError", gdyż nie można przekonwertować int na str.

# #ValueError: invalid literal for int() with base 10: 'd'


# Wstawienie usprawnienia do programu.
# Wprowadzenie obsługi błędów. Program będzie prosił użytkownika o podanie liczby, dopóki nie poda jej poprawnie.

# Teraz będzie trzeba zrezygnować z pętli for, ponieważ program może wykonywać się więcej niż 5 razy.
# Potrzebny będzie counter, aby zliczać ilość poprawnych zapisanych liczb.

counter = 0

while True: # Pętla while potrzebuje "True", aby się w ogóle uruchomić.
    if counter > 4: # Jeżeli counter będzie większy od 4, opuszczamy pętlę.
        break
    try: # sprawdzenie, czy fragment kodu nie wygenerował jakiegoś wyjątku
        n = int(input("Podaj liczbę całkowitą: "))
        numbers.append(n) # jeżeli nie pojawił się wyjątek, liczba zostanie dopisana do listy "numbers"...
        counter += 1 # ... a counter zostanie zwiększony o 1.
    except: # obsłużenie błędu, jeżeli kod wygenerował jakiś błąd.
        print("To nie jest liczba całkowita! Spróbuj ponownie")

print(numbers)