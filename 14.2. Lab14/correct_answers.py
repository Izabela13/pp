# # Zadanie 1: phone_numbers

# # Kluczem będzie imię, wartością - numer telefonu
# phones = {
#     "Adam": 123123123,
#     "Karol": 111222333,
#     "Mariola": 453453453,
#     "Iza": 443443443
# }

# # Algorytm - pętla while
# while True:  # Warunek ustawiony na "True"
#     name = input("Podaj imię: ")
#     if name == "":  # Jeżeli podane imię będzie wartością "None", to ...
#         break  # ... wyjdź z pętli
#     if name in phones:  # Jeżeli imię będzie znajdowało się w słowniku, to...
#         print("Telefon:", phones[name])  # ... wyświetl informacje o telefonie
#     else:
#         print("Nie znaleziono telefonu dla imienia", name)



# # Zadanie 2: lists_tuple

# # Druga funkcja sprawdzająca czy w liście nie ma już tych elementów
# def merge_lists_without_duplicates(source, target):  # lista źródłowa = "source", lista wynikowa = "target"
#     for e in source: # Jedna lista będzie dodawna do drugiej listy, a przy okazji sprawdzane będzie, czy...
#         if e not in target: # w liście "target" nie powtarzają się elementy.
#             target.append(e)


# # Pierwsza funkcja to funkcja ogólna - główna funkcja, która będzie pobierała 3 listy
# def transform_data(list1, list2, list3):
#     result = []  # tworzenie listy, do której będą dodawane elementy
#     merge_lists_without_duplicates(list1, result)  # wywoływanie funkcji i podstawianie list źródłową i docelową ("result")
#     merge_lists_without_duplicates(list2, result)  # obsługiwana jest każda lista z osobna
#     merge_lists_without_duplicates(list3, result)
#     return tuple(result)  # transformacja listy na krotkę


# # Testy dla funkcji "transform_data"
# print(transform_data([1, 2], [1, 1], [4, 4, 4]))
# print(transform_data([1, 2, 3], [1, 2, 3], [4, 5, 6]))
# print(transform_data(["Ala", "ma"], ["Ala", "ma", "kota"], ["mysz"]))



# Zadanie 3: game_points

# 2. Zanim funkcja "define_players" utworzy graczy, trzeba stworzyć pojedynczego gracza
def define_player(player_no):
    player_points = [] # Gracz będzie posiadał jakąś liczbę punktów. Punkty będą dopisywane co turę
    player_name = input("Podaj imię " + str(player_no) + " gracza: ") # Pobieranie imienia gracza.
    return {player_name: player_points} # Jeżeli każdy gracz będzie miał imię i punkty, to można wykorzystać słownik.
# W słowniku będą przechowywani gracze oraz ich punkty. Kluczem będzie imię gracza, a wartością lista z punktami.
# Tym sposobem do gracza będzie można dostać się przez klucz, a także zsumować elementy listy.
# Na końcu ma zostać zwrócony mini-słownik, który będzie się składał z klucza i listy punktów.
# Na początku, przy definiowaniu gracza, punkty gracza to będzie pusta lista.


# 1. Funkcja definiująca wszystkich graczy
def define_players():
    players = {} # Tworzenie pustego słownika przechowującego graczy
    players_total = int(input("Podaj liczbę graczy (1-8): ")) # informacja o ilości definiowanych graczy
    for i in range(players_total): # Jeżeli mamy informację o ilości graczy, to w pętli możemy pobrać imiona
        players.update(define_player(i + 1)) # zaczynamy od 0, dlatego potrzebujemy i + 1
    # Do słownika będziemy dodawać (robić update) graczy, których będziemy pobierać metodą "define_player".
    # "define_player" za każdym razem będzie zwracać słownik, którego kluczem jest nazwa użytkownika i pusta lista punktów.
    return players # zwrócenie graczy


# 3. Definiowanie liczby punktów potrzebnej do wygranej
def define_win_poins():
    return int(input("Zdefiniuj liczbę punktów wygranej: "))


# 5. Funkcja pomocnicza, definiująca, czy ktoś jest zwycięzcą.
def is_winner(players, win_points): # Żeby liczyć punkty potrzebny będzie słownik "players" i poziom wygranej
    for player_name, player_points in players.items(): # sprawdzanie, czy mamy zwycięzcę - zostaną zwrócone krotki
        sum = 0
        for p in player_points: # bierzemy jendego gracza i sumujemy jego punkty
            sum += p
        if sum >= win_points: # czy suma nie jest większa lub równa limitowi punktów?
            return True
    return False


# 4. Definiowanie funkcji, która będzie realizowała zbieranie punktów do momentu, dopóki ktoś nie uzyska liczby
#    punktów, która określona jest jako wygrana.
def count_points(players, win_points):
    counter = 1 # ta zmienna będzie wskazywała turę gry
    while True: # Będziemy kręcić się w tej pętli dopóty, dopóki ktoś nie osiągnie zwycięzkiej liczby punktów
        print("\nTura", counter) # informacja o turze gry
        for player_name in players.keys(): # tura dla każdego gracza ze słownika
            player_points = int(input("Podaj punkty dla gracza " + player_name + ": ")) # prośba o podanie punktów tury
            players[player_name].append(player_points) # wstawianie punktów do listy
            # dla słownika "players", dla klucza "[player_name]" dodajemy (append()) punkty gracza z danej tury
            if is_winner(players, win_points): # Jeżeli mamy zwycięzcę,
                return player_name # kto jest tym zwycięzcą
        counter += 1 # Jeżeli nie mamy zwycięzcy, to przechodzimy do kolejnej tury


# 6. Prezentacja wyników
def show_results(players, winner): # potrzebny jest słownik z graczami i zwycięzca (winner)
    print("\nWygrał gracz o imieniu", winner, ", brawo!\n") # Pokazanie, kto wygrał
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players() # Program wystartuje, ponieważ musimy zdefiniować wszystkich graczy.
win_points = define_win_poins() # Przypisanie punktów wygranej korzystając z funkcji "define_win_points()"
winner = count_points(players, win_points) # Winner
show_results(players, winner) # Metoda "show_results" potrzebuje graczy i winnera