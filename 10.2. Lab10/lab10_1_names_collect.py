""""
1. Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
• pobrać kolejne elementy i zapisać je do listy,
• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.
"""

amount = int(input("Wprowadź liczbę imion, jakie chcesz wprowadzić: "))
names = []

i = amount

for i in range(amount):
    if i <= amount:
        names.append(input("Wprowadź " + str(i + 1) + " imię: "))
print("Pobrano następujący zbiór imion:", names)

