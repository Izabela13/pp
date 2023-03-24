"""
3. Napisz grę polegającą na zapamiętywaniu kolejnych słów.
Wylosowany gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej samej kolejności i także dodać swoje.

Rozgrywka kończy się gdy, któryś z graczy popełni błąd.

Na ekranie komputera przy każdej turze należy wymazać ekran np. przez wyświetlenie 100 pustych wierszy.
"""


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

    word = input("Wprowadź słowo: ")
    if word not in players_words:
        players_words.append(word)
    return players_words

# print(put_word())


# # Funkcja przechwytująca powtarzanie słów
def enumerate_words():

    repetition_words = []

    print("Wymień poprzednie słowa: ")
    while True:
        which_words = input(": ")
        repetition_words.append(which_words)
        if which_words == "":
            break

    return repetition_words


# print(enumerate_words())


# # Rozgrywka

def start():

    print(players_list[-1] + ", rozpoczynasz.")
    return put_word()


counter_2 = 1

while True:
    if counter_2 == 1:
        start()
        counter_2 += 1
    else:
        for i in range(len(players_list)):
            print(players_list[i], enumerate_words())
            if players_words == enumerate_words():
                print(put_word())
            else:
                print("Koniec gry.")
        counter_2 += 1