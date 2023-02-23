""""
1. Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
• pobrać kolejne elementy i zapisać je do listy,
• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.
"""

print("Możesz utworzyć własny zbiór imion.")
amount = int(input("Podaj, ile imion chcesz wprowadzić do zbioru: "))
print("Teraz wprowadź imiona. Pamiętaj, że ilość wprowadzanych imion musi odpowiadać podanej liczbie imion.")

print("")

names = [] # lista imion

counter = 0 # początek listy

for name in range(amount):
    counter += 1
    names.append(input("Podaj " + str(counter) + " imię: "))
else:
    print("Oto lista wprowadzonych przez Ciebie imion: ", names)
