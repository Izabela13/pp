# # FUNKCJE - WPROWADZENIE


# # FUNKCJE WBUDOWANE input() i print()

# # Funkcja input() i print() to też funkcje wbudowane w język Python
# # tworzenie zmiennej i używanie funkcji input(), która przekazuje wartość bezpośrednio do zmiennej.
# # Funkcja input() może być uruchomiona:
# # 1) albo bez żadnych argumentów
# # 2) albo z argumentem, który jest np. ciągiem znaków
# name = input("Jak masz na imię? ")  # "Jak masz na imię? " to argument funkcji input()
# print(("Witaj " + name + "!") * 100) # funkcja print() również ma swoje możliwości - może przekazywać argumenty



# # PRZEJŚCIE DO PLIKU ŹÓDŁOWEGO get_and_show_numbers



# # PRZEKAZYWANIE PARAMETRÓW/ ARGUMENTÓW POZYCYJNYCH
# print("raz", "dwa", "trzy") # wynik: raz dwa trzy
# # kolejność, w jakiej podaliśmy argumenty, w takiej kolejności zostały wyświetlone na ekranie

def introduce(first_name, last_name): # metoda "introduce" bedzie miała dwa parametry ("first_name" i "last_name")
    print("Cześć, jestem", first_name, last_name) # metoda "introduce" będzie wyświetlała przywitanie

# # Wywołanie funkcji - wprowadzenie argumentów do parametrów:
introduce("Jan", "Kowalski") # W takiej kolejności, w jakiej argumenty zostały przekazane, w takiej zostały wyświetlone.
introduce("Kowalski", "Jan") # Jeżeli pomylimy się, dostaniemy argumenty w kolejności, w jakiej przekazaiśmy do funkcji.

# # Przekazywanie argumentów słów kluczowych - można jawnie określić, jakie argumenty mają zostać wprowadzone.
introduce(last_name="Kowalski", first_name="Jan") # teraz kolejność nie ma znaczenia. Kolejność została ustalona w funkcji.

# # Czy można miksować sposoby przekazywania argumentów?
# # Sposoby przekazywania argumentów do funkcji można mieszczać. Trzeba przestrzegać zasady:
# # 1. najpierw argumenty pozycyjne
# # 2. argumenty jako słowa kluczowe
# # introduce("Jan", last_name="Kowalski") # ten kod zadziała

# # introduce(last_name="Kowalski", "Jan") # ten kod się nie uruchomi.
# # Dostaniemy komunikat, że argument pozycyjny jest umiejscowiony za argumentem słów kluczowych.


# # Mieszany sposób przkazywania argumentów w funkcji print()
# print("raz", "dwa", "trzy", sep=" - ") # użycie separatora czy end'a to również użycie słów kluczowych.



# # WARTOŚCI DOMYŚLNE ARGUMENTÓW FUNKCJI

def introduce(first_name = "Jan", last_name = "Kowalski"): # dodawanie wartości domyślnych
    print("Cześć, jestem", first_name, last_name)

# #Co nam to daje? Daje nam to to, że jeżeli znajdzie się ktoś, kto wywoła funkcję bez żadnych argumentów,
# # to dostaniemy wynik z wartościami, które zdefiniowaliśmy jako wartości domyślne przy definiowaniu funkcji.
introduce() # Wynik: Cześć, jestem Jan Kowalski

# # Może się zdarzyć, że ktoś poda tylko pierwszy albo tylko drugi argument. Wówczas argument, który nie został podany,
# # wyświetli się z wartością domyślną.
introduce("Marcin",) # brak nazwiska lub imienia wyświetli wartości domyślne, np. Cześć, jestem Marcin Kowalski

# # Należy tutaj zachować ostrożność. Przy definiowaniu wartości domyślnych musimy je ustawiać na samym końcu, tzn.
# # nie jesteśmy w stanie zrobić np. czegoś takiego: "first_name" będzie wartością domyślną, a "last_name" trzeba podać.
# # def introduce(first="Jan", last_name):
# #     print("Cześć, jestem", first_name, last_name)
# # Pojawi się komunikat o tym, że niedomyślny parametr poprzedza domyślny parametr.

# # Można podać tylko jeden parametr przy wywoływaniu funkcji:
introduce(last_name="Nowak")



# # ZWRACANIE WARTOŚCI PRZEZ FUNKCJĘ - RETURN
# # w poprzednich funkcjach RETURN równało się None.
def introduce(first_name = "Jan", last_name = "Kowalski"): # ta funkcja nigdzie nie ma słowa kluczowego return
    print("Cześć, jestem", first_name, last_name)
    # return None # domyślnie słowo kluczowe "return" jest ustawione na "None"
# # Nie ma znaczenia, czy jest "return None", czy nie ma. Za każdym razem funkcja zwróci jakąś wartość.
# # Równie dobrze można ustawić po "return" jakąś inną wartość, np. "return 12". Wówczas funkcja zwróci wartość 12.
print(introduce()) # Wynik: "None" - "None" to wartość, którą zwraca ta funkcja
"""
Wynik:
Cześć, jestem Jan Kowalski
None
"""



# SPOSOBY WYKORZYSTANIA TEGO, CO ZWRACA FUNKCJA - plik źródłowy count_down (odliczanie)



# Niedokończona funkcja
def my_fun(): # Funkcja będzie zwracała wartość None
    #TODO
    pass # zaślepka - często stosowana, gdy nie wiemy jak zaimplementować funkcję, ale chcemy, żeby kod się uruchamiał.

print(my_fun()) #None

if my_fun() == None: # Możemy sprawdzić, czy funkcja zwraca coś czy nie
    print("Funkcja na razie nic nie zwraca.")