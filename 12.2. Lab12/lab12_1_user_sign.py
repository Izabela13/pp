"""
1. Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
ilość razy, w poziomie lub w pionie.
"""

# 1. Dowolny znak
# 2. Dowolna ilość razy
# 3. W poziomie lub w pionie

def get_sign():
    sign = input("Podaj dowolny znak: ")
    amount = int(input("Podaj, ile razy chcesz wyświetlić znak: "))
    direction = input("Podaj, w jakim kierunku mają wyświetlać się znaki. Wpisz 'PION' lub 'POZIOM': ")
    if direction == "POZIOM":
        return (sign + " \n") * amount
    else:
        return sign * amount

print(get_sign())