"""
3. Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
wprowadzaniem błędnych danych przez użytkownika.
"""

# 0. Wprowadzenie funkcji zabezpieczającej program przed wprowadzeniem błędnych danych przez użytkownika.
def check_and_return_message(standard_msg, error_msg = "Podana wartość nie jest liczbą całkowitą. \n"):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


# 1. Definiowanie liczby oraz imion graczy

# 1.1. Definiowanie liczby graczy
def define_players():
    players = {}

    players_number = check_and_return_message("Wprowadź liczbę graczy: ")
    print()

    for i in range(int(players_number)):
        players.update(define_player(i + 1))

    return players


# 1.2. Definiowanie imion graczy
def define_player(player_no):
    player_points = []
    player_name = input("Wprowadź imię lub pseudonim " + str(player_no) + " gracza: ")
    return {player_name: player_points}


# 2. Definiowanie liczby punktów potrzebnej do wygranej
def define_win_points():

    win_points = check_and_return_message("Wprowadź liczbę punktów potrzebnych do wygranej: ")
    print()

    return int(win_points)


# 3. Pobieranie informacji o zdobytych punktach w każdej turze gry

# 3.1. Zwycięzkie punkty
def winner(players, win_points):

    for player_name, player_points in players.items():
        all_points = 0
        for points in player_points:
            all_points += points
        if all_points >= win_points:
            return True
    return False


# 3.2. Rozgrywka
def count_points(players, win_points):
    counter = 1
    while True:
        print("\nTura " + str(counter) + ":")
        for player_name in players.keys():
            player_points = check_and_return_message("Wprowadź punkty dla gracza " + player_name + ": ")
            players[player_name].append(player_points)

            if winner(players, win_points):
                return player_name
        counter += 1


# 4. Prezentacja wyników
def show_game_results(players, winner):
    print("\nZwycięzca rozgrywki to: " + winner + "!\n")
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_game_results(players, winner)