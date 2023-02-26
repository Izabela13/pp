# Zadanie 1
# phones = {
#     "Adam": 123123123,
#     "Karol": 111222333,
#     "Mariola": 453453453,
#     "Iza": 443443443
# }
#
# while True:
#     name = input("Podaj imię: ")
#     if name == "":
#         break
#     if name in phones:
#         print("Telefon:", phones[name])
#     else:
#         print("Nie znaleziono telefonu dla imienia" + name)


# Zadanie 2 Lists_tuple
# def merge_lists_without_duplicates(source, target):
#     for e in source:
#         if e not in target:
#             target.append(e)
#
# def transform_data(list1, list2, list3):
#     result = []
#     merge_lists_without_duplicates(list1, result)
#     merge_lists_without_duplicates(list2, result)
#     merge_lists_without_duplicates(list3, result)
#     return tuple(result)
#
# print(transform_data([1, 2], [1, 1], [4, 4, 4]))
# print(transform_data([1, 2, 3,], [1, 2, 3], [4, 5, 6]))
# print(transform_data(["Ala", "ma"], ["Ala", "ma", "kota"], ["mysz"]))



# Zadanie 3 game_points

def define_player(player_no):
    player_points = []
    player_name = input("Podaj imię " + str(player_no) + " gracza: ")
    return {player_name: player_points}

def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy (1-8): "))
    for i in range(players_total):
        players.update(define_player(i + 1)) # zaczynamy od 0, dlatego potrzebujemy i + 1
    return players

def define_win_poins():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))

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
            player_points = int(input("Podaj punkty dla gracza" + player_name + ": "))
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