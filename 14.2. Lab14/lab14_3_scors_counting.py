"""
3. Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
• definiowanie liczby oraz imion graczy,
• definiowanie liczby punktów potrzebnych do wygranej,
• pobieranie informacji o zdobytych punktach w każdej turze gry,
• wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy
"""


gamers = int(input("Wprowadź liczbę graczy: "))
gamers_names = []

counter = 1

for gamer in range(gamers):
    gamer_name = input("Wprowadź imię " + str(counter) + " gracza: ")
    if counter < gamers and gamer_name not in gamers_names:
        gamers_names.append(gamer_name)
        counter += 1
    elif gamer_name in gamers_names:
        print("Imię gracza już istnieje. Wprowadź inne imię lub pseudonim.")

# win_scores = int(input("Wprowadź liczbę punktów potrzebnych do wygranej: "))
#
# scores = int(input("Wprowadź punkty gracza: "))