"""
3. Napisz grę polegającą na zapamiętywaniu kolejnych słów.
Wylosowany gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej samej kolejności i także dodać swoje.

Rozgrywka kończy się gdy, któryś z graczy popełni błąd.

Na ekranie komputera przy każdej turze należy wymazać ekran np. przez wyświetlenie 100 pustych wierszy.
"""


from time import sleep


# Wprowadzanie graczy do systemu
players_counter = 1
players_list = []

while True:
    player = input("Graczu " + str(players_counter) + ", podaj imię lub pseudonim: ")
    if players_counter == 1 and player == "":
        print("Nie wprowadzono gracza. Nastąpiło wyjście z gry.")
    if player == "":
        if player == "" and len(players_list) == 1:
            print("W grze może brać udział co najmniej 2 graczy.")
        else:
            break
    elif player in players_list:
        print("Nazwa gracza już istnieje. Wprowadź inne imię lub pseudonim. \n")
    else:
        players_counter += 1
        players_list.append(player)


print("\nW grze bierze udział:  ", end="")
for person in players_list:
    print(person, sep="", end="  ")
print("\n")


players_words = []


# Funkcja przechwytująca wprowadzane słowa
def put_word():

    while True:
        word = input("Wprowadź słowo: ")
        if word not in players_words and word != "":
            players_words.append(word)
            return players_words
        else:
            if word == "":
                print("Musisz wprowadzić słowo.")
            else:
                print("Wprowadzone słowo już się pojawiło. Podaj inne słowo.")


# # Funkcja przechwytująca powtarzanie słów
def enumerate_words():

    repetition_words = []

    print("Wymień poprzednie słowa: ")
    while True:
        which_words = input(": ")
        repetition_words.append(which_words)
        if which_words == "":
            break

    return repetition_words[:-1]


# # Funkcja rozpoczynająca rozgrywkę
def start():

    print(players_list[-1] + ", rozpoczynasz.")
    return put_word()


# # Funkcja porównująca słowa wprowadzone do systemu z powtarzanymi
def comparison(players_words):
    if players_words != enumerate_words():
        return print("Koniec gry.")
    else:
        return True


# # Rozgrywka
counter_2 = 1

while len(players_list) >= 2:
    if counter_2 == 1:
        start(), sleep(3)
        counter_2 += 1
        print("\n" * 100)
    else:
        for i in range(len(players_list)):
            print(players_list[i])
            if comparison(players_words) == True:
                put_word(), sleep(3)
                counter_2 += 1
                print("\n" * 100)
            else:
                if len(players_list) == 2:
                    print(players_list[i] + ", odpadasz z gry."), sleep(3)
                    players_list.pop(i)
                    break
                else:
                    print(players_list[i] + ", odpadasz z gry"), sleep(3)
                    players_list.pop(i)
                    print("\n" * 100)
                    counter_2 += 1
else:
    print("\nWygrał gracz o imieniu:", players_list[0])