# # Zadanie 1: safe_int_taster

# # Zaczynamy od stworzenia odpowiedniej funkcji:

# def safe_int(arg): # pobieramy argumnet
#     return int(arg) # argument przekonwertowany na wartość int.


# # Testowanie
# print(safe_int(1))
# print(safe_int(7.2))
# print(safe_int("jeden"))

# # ValueError: invalid literal for int() with base 10: 'jeden'

"""
Obsługa wyjątku.
Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int i zwrócić go.
Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja powinna zwrócić None.
"""

# def safe_int(arg): # pobieramy argumnet
#     try:
#         return int(arg) # argument przekonwertowany na wartość int.
#     except:
#         return None


# # Testowanie
# print(safe_int(1))
# print(safe_int(7.2))
# print(safe_int("jeden"))
"""
Wyniki: 
1
7
None
"""



# # Zadanie 2: fetch_floating_numbers

# # Pozyskane liczby zapisywane będą do listy

# numbers = []
# counter = 1  # do wykorzystania w pętli while

# # while True:  # pętla ustawiona jest domyślnie na wykonywanie się jako pętla nieskończona
# #    if counter > 3:
# #         break  # wyjście z pętli
# #
# #     number = float(input("Podaj " + str(counter) + " liczbę zmiennoprzecinkową: "))# Tutaj może wydarzyć się wyjątek
# #     numbers.append(number)  # jeżeli liczba zostanie pozyskana, zostanie dopisana do listy "numbers"
# #     counter += 1  # zwiększenie countera


# while True:  # pętla ustawiona jest domyślnie na wykonywanie się jako pętla nieskończona
#     if counter > 3:
#         break  # wyjście z pętli

#     try:
#         number = float(input("Podaj " + str(counter) + " liczbę zmiennoprzecinkową: "))  # Tutaj może wydarzyć się wyjątek
#         numbers.append(number)  # jeżeli liczba zostanie pozyskana, zostanie dopisana do listy "numbers"
#         counter += 1  # zwiększenie countera
#     except:
#         print("Podana wartość jest niepoprawna. Spróbuj ponownie!")

# print(numbers)



# Zadanie 3: game_points_2
"""
3. Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
wprowadzaniem błędnych danych przez użytkownika.
"""

"""
Gdzie są wrażliwe miejsca? 
Wrażliwe miejsca są wszędzie tam, gdzie pobierane są jakieś wartości, szczególnie tam, gdzie nie zależy nam na stringu.
Problem pojawia się tam, gdzie próbujemy konwertować wartość.
"""

# Pobierz i zwaliduj liczby całkowite
def fetch_and_validate_int(standard_msg, error_msg = "To nie jest liczba"): # oprócz standardowego komunikatu pojawi się komunikat o błędzie
    while True: # Funkcja będzie wywoływana ponownie
        try:
            return int(input(standard_msg)) # To, co podał użytkownik funkcji (jeśli wszystko pójdzie dobrze)
        except:
            print(error_msg) # Jeżeli wystąpi błąd, podajemy error_msg.

"""
Żeby użyć funkcji "fetch_and_validate_int" w różnych miejscach programu najlepiej podać tekst, który ma zostać wyświetlony użytkownikowi. 
Funkcja będzie miała na pewno jakiś standardowy komunikat - parametr "standard_msg".  

Oprócz standardowego komunikatu, który zostanie wyświetlony użytkownikowi będzie jeszcze niestandardowy komunikat - o błędzie.
Do komunikatu o błędzie można dopisać domyślną wartość "To nie jest liczba".
Wszędzie, gdzie nie zostanie podana wartość parametru standard_msg, zostanie użyty standardowy komunikat. 

Gdyby funkcja fetch_and_validate_int została tylko w jednym miejscu, to wykonywałaby się tylko raz. 
"""

def define_player(player_no):
    player_points = []
    player_name = input("Podaj imię " + str(player_no) + " gracza: ")
    return {player_name: player_points}

def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbę graczy (1-8): ") # WKLEJENIE NAZWY FUNKCJI!!!
    for i in range(players_total):
        players.update(define_player(i + 1)) # zaczynamy od 0, dlatego potrzebujemy i + 1
    return players

def define_win_poins():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ") # WKLEJENIE NAZWY FUNKCJI!!!

def is_winner(players, win_points):
    for player_name, player_points in players.items():
        sum = 0
        for p in player_points:
            sum += p
        if sum >= win_points:
            return True
        return False

def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura", counter)
        for player_name in players.keys():
            player_points = fetch_and_validate_int("Podaj punkty dla gracza " + player_name + ": ") # WKLEJENIE NAZWY FUNKCJI!!!
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1

def show_results(players, winner):
    print("\nWygrał gracz o imieniu", winner, ", brawo!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_poins()
winner = count_points(players, win_points)
show_results(players, winner)


"""
Za każdym razem nadpisujemy funkcję input o dodatkowy charakter sprawdzający. 

funkcja fetch_and_validate_int ma ustawiony domyślny parametr "error_msg", ale można dopisać również, co innego, np.
players_total = fetch_and_validate_int("Podaj liczbę graczy (1-8): ", "Źle!") 
W przypadku, gdy do funkcji dopiszemy własny komunikat o błędzie, wówczas program skorzysta z komunikatu dopisanego.

Np. w przyszłości może zajść potrzeba, aby dopisać "Błąd! To nie jest poprawna liczba graczy!" albo "Błąd! To nie jest
poprawna liczba punktów!".
"""