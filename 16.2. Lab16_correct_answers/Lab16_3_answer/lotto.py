from random import sample

def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort()
    return lucky_numbers


def get_game_system(): # Dodatkowa funkcja, która będzie pytać użytkownika, jaką ilość liczb chce skreślić.
    while True:
        try:
            n = int(input("Podaj, ile liczb chcesz skreślić (6-12)?"))
            if n < 6 or n > 12: # Jeżeli wartość podana przez użytkownika będzie poza zakresem, dostanie informację.
                print("Należy podać liczbę z przedziału 6-12!")
                continue # Będziemy męczyć użytkownika dopóty, dopuki nie poda poprawnej liczby.
            break # Jeżeli wszystko jest OK, powinniśmy wyjść z pętli.
        except:
            print("To nie jest liczba!")
    return n # Gdyby polecenie "return" było przesunięte do pozycji "except", wówczas nie byłoby co zwracać.
# return musi zostać zwrócone dopiero po wyjściu z pętli


# Mechanizm do skreślania liczb przez użytkownika
def get_user_numbers():
    n = get_game_system() # tutaj ustawiona na sztywno była wartość 6 (zahardkodowana)
    """
    Funkcję "get_game_system()" można użyć wewnątrz funkcji "get_user_numbers". Co nam to da?
    Nigdzie nie będzie trzeba modyfikować już napisanego programu. 
    Nasz program "lotto_game", który nic nie wie o funkcji "get_game_system()", będzie mógł być wykonywany dokładnie
    w ten sam sposób, ponieważ modyfikujemy tylko i wyłącznie bibliotekę. 
    """
    counter = 1
    user_numbers = []

    while counter < n + 1: # Pętla będzie działa do momentu, dopóku counter będzie mniejszy od n + 1
        try:
            number = int(input("Podaj " + str(counter) + " liczbę (1-49): "))
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziału od 1 do 49!")
                continue
        except:
            print("To nie jest liczba. Proszę podać liczbę całkowitą")
            continue

        user_numbers.append(number)
        counter += 1

    user_numbers.sort()
    return user_numbers


def check_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter



if __name__ == "__main__": # Jeżeli my będziemy wywoływać moduł
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)