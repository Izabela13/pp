"""
3. Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
• definiowanie liczby oraz imion graczy,
• definiowanie liczby punktów potrzebnych do wygranej,
• pobieranie informacji o zdobytych punktach w każdej turze gry,
• wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy
"""

# 1. Definiowanie liczby oraz imion graczy

# 1.1. Definiowanie liczby graczy
def define_players():
    players = {}

    while True:
        players_number = input("Wprowadź liczbę graczy: ")
        print()
        if players_number == "0" or players_number == "":
            print("Wprowadzono nieprawidłową wartość.")
        elif players_number == "1":
            print("Liczba graczy musi być większa niż 1 gracz.")
        else:
            for i in range(int(players_number)):
                players.update(define_player(i + 1))
            break

    return players


# 1.2. Definiowanie imion graczy
def define_player(player_no):
    player_points = []
    player_name = input("Wprowadź imię lub pseudonim " + str(player_no) + " gracza: ")
    return {player_name: player_points}


# 2. Definiowanie liczby punktów potrzebnej do wygranej
def define_win_points():

    while True:
        win_points = input("Wprowadź liczbę punktów potrzebnych do wygranej: ")
        print()
        if win_points == "0" or win_points == "":
            print("Wprowadzono nieprawidłową wartość.")
        else:
            break

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
            player_points = int(input("Wprowadź punkty dla gracza " + player_name + ": "))
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