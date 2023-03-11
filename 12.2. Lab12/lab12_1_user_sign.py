"""
1. Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
ilość razy, w poziomie lub w pionie.
"""

# 1. Dowolny znak
# 2. Dowolna ilość razy
# 3. W poziomie lub w pionie


# Funkcja przyjmująca argumenty od użytkownika
print("WYŚWIETLENIE FUNKCJI PRZYJMUJĄCEJ DANE OD UŻYTKOWNIKA.")

def get_user_sign():

    sign = input("Podaj dowolny znak: ")
    amount = input("Podaj, ile razy chcesz wyświetlić znak: ")
    direction = input("Podaj, w jakim kierunku mają wyświetlać się znaki. "
                      "'H' = poziomo (horizontally), 'V' = pionowo (vertically): ")

    if sign == "":
        sign = "*"

    if amount == "":
        amount = 5

    for i in range(int(amount)):
        if direction in ("H", "h") or direction not in ("V", "v"):
            print((sign + " "), end="")
        elif direction == "V" or direction == "v":
            print(sign)
        i += 1
    else:
        print("\n")


# Wywołanie funkcji
get_user_sign()



# Funkcja przyjmująca dowolne argumenty, których nie wprowadza użytkownik
print("WYŚWIETLENIE FUNKCJI PRZYJMUJĄCEJ DANE W KODZIE.")

def get_sign(sign="*", amount=5, direction="H"):

    for i in range(amount):
        if direction in ("H", "h") or direction not in ("V", "v"):
            print((sign + " "), end="")
        elif direction == "V" or direction == "v":
            print(sign)
    else:
        print("\n")


# Wywołanie funkcji
get_sign()
get_sign(sign="@", amount=10)
get_sign(sign="$", direction="v")