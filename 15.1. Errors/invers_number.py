# # Program pobiera liczbę rzeczywitsą i podaje jej odwrotność

# while True:
#     number = int(input("Podaj liczbę całkowitą: "))
#     print("Odwrotna liczba to", 1 / number)


# while True:
#     try: # Podejrzany fragment, który może wywołać problemy objęty jest klauzulą
#         number = int(input("Podaj liczbę całkowitą: "))
#         print("Odwrotna liczba to", 1 / number)
#     except:
#         print("Coś poszło nie tak...") # Użytkownik nadal nie wie, co poszło nie tak


# # Co może pójść nie tak:
# # ZeroDivisionError - wpisanie 0 do programu, ponieważ nie można dzielić przez 0.
# # ValueError - wpisanie ciągów znaków


while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ValueError: # konkretny błąd - to nie jest liczba całkowita
        print("To nie jest liczba całkowita")
    except ZeroDivisionError: # konkretny błąd - nie można wykonać dzielenia przez 0
        print("Błąd dzielenia przez zero")
    except:
        print("Coś poszło nie tak...")