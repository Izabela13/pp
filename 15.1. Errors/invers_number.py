# Program pobiera liczbę rzeczywitsą i podaje jej odwrotność

# while True:
#     number = int(input("Podaj liczbę całkowitą: "))
#     print("Odwrotna liczba to", 1 / number)


# while True:
#     try:
#         number = int(input("Podaj liczbę całkowitą: "))
#         print("Odwrotna liczba to", 1 / number)
#     except:
#         print("Coś poszło nie tak...") # Użytkownik nadal nie wie, co poszło nie tak


# Co może pójść nie tak:
# ZeroDivisionError
# ValueError


while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ValueError:
        print("To nie jest liczba całkowita")
    except ZeroDivisionError:
        print("Błąd dzielenia przez zero")
    except:
        print("Coś poszło nie tak...")