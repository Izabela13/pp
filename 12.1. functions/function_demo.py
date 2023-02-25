# Funkcja input i print to też funkcje
# name = input("Jak masz na imię? ")
# print(("Witaj " + name + "!") * 100)


# Przekazywanie paramterów/ argumentów pozycyjnych.
# print("raz", "dwa", "trzy") # efekt: raz dwa trzy
#
# def introduce(first_name, last_name):
#         print("Cześć, jestem", first_name, last_name)
#
# introduce("Jan", "Kowalski") # W takiej kolejności, w jakiej argumenty zostały przekazane, w takiej zostały wyświetlone
# introduce("Kowalski", "Jan")
#
# introduce(last_name="Kowalski", first_name="Jan") # teraz kolejność nie ma znaczenia


# sposoby przekazywania argumentów do funkcji można mieszczać. Trzeba przestrzegać zasady:
# 1. najpierw argumenty pozycyjne
# 2. słowa kluczowe
# introduce(last_name="Kowalski", "Jan") # ten kod się nie uruchomi.

# mieszany sposób przkazywania argumentów
# print("raz", "dwa", "trzy", sep=" - ")


# Podawanie argumentów domyślnych

# def introduce(first_name = "Jan", last_name = "Kowalski"):
#     print("Cześć, jestem", first_name, last_name)
#
# introduce("Marcin",) # brak nazwiska lub imienia wyświetli wartości domyślne
# introduce(last_name="Nowak")



# # RETURN
# # w poprzednich funkcjach RETURN równało się None.
# def introduce(first_name = "Jan", last_name = "Kowalski"):
#     print("Cześć, jestem", first_name, last_name)
# print(introduce())
# """
# Wynik:
# Cześć, jestem Jan Kowalski
# None
# """



def my_fun():
    #TODO
    pass # zaślepka - często stosowane, gdy nie wiadomo jak zaimplementować tę funkcję, ale kod ma się uruchamiać

print(my_fun()) #None

if my_fun() == None:
    print("Funkcja na razie nic nie zwraca.")