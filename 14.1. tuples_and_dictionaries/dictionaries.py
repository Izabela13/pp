# # SŁOWNIKI

# # Słownik to zestaw "klucz-wartość".
# # Przykład - książka telefoniczna o nazwie "phones".
phones = {"Tomek": 345123456,
          "Ada":   123123123,
          "Karol": 999999999}

print(phones)  # {'Tomek': 345123456, 'Ada': 123123123, 'Karol': 999999999}
# # Jako klucz mamy string, jako wartość - jakieś liczby.

# # KLUCZ musi być NIEPOWTARZALNY, ponieważ jednoznacznie identyfikuje dany wpis w słowniku (jakąś wartość)
# # Jeżeli na końcu słownika "phone" zostanie dodany klucz "Tomek" z jakimś numerem telefonu (nową wartością), to
# # słownik automatycznie podmieni wartość wpisaną wcześniej na ostatnią (jakby najaktualniejszą).
phones = {"Tomek": 345123456,
          "Ada":   123123123,
          "Karol": 999999999,
          "Tomek": 100000000}

print(phones) # {'Tomek': 100000000, 'Ada': 123123123, 'Karol': 999999999}
# # Interpreter uznaje, że tworzony jest obiekt słownik, w którym została zaktualizowana jakaś wartość.
# # Jeżeli jakiś klucz pojawi się jeszcze raz w słowniku, wówczas zostanie nadpisany.



# # ODWOŁANIA DO SŁOWNIKA - UŻYCIE NAWIASÓW KWADRATOWYCH I METODY GET()

# # Przykład słownika - nauka języków obcych - konwersja z polskiego na angielski
animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

# # Odwołanie do słownika - przykład: chcielibyśmy zobaczyć, jak jest po angielsku "kot".
print(animals_dict["kot"])  # odwołanie za pomocą samych nawiasów kwadratowych
print(animals_dict.get("kot"))  # odwołanie za pomocą metody get()
# # Z zastosowaniem metody get() jest bezpieczniej, bo gdy użyjemy wyrazu, którego nie ma wśród zestawu kluczy,
# # zostanie zwrócona wartość "None".Odwołanie za pomocą nawiasów kwadratowych do klucza, którego nie ma w słowniku
# # kończy się wyjątkiem KeyError.

# # Funkcja get() ma dodatkowy parameter. Jeżeli nie znajdziemy nazwy klucza, to kolejnym parameterm będzie element,
# # który możemy zwrócić w miejsce elementu, którego brakuje.
print(animals_dict.get("krowa", "Brak takiego słowa"))  # Brak takiego słowa



# # W AKTUALNYCH WERSJACH PYTHONA SŁOWNIKI SĄ OBIEKTAMI UPORZĄDKOWANYMI
# # Do wersji 3.6 słowniki były kolekcjami nieuporządkowanymi. Nie mieliśmy pewności, czy jeżeli do słownika wstawimy
# # elementy w jakiejś kolejności, to w takiej kolejności je wyciągniemy.



# # WERYFIKACJA, CZY ISTNIEJE KLUCZ W SŁOWNIKU
words = ["kot", "lew", "chomik"] # lista słów, których znaczenie chcę sprawdzić w języku angielskim
for word in words:  # przechodzenie po liście za pomocą pętli for (wyciąganie słówka z listy słówek)
    if word in animals_dict:  # sprawdzenie: jeżeli "słówko" jest w słowniku, to...
        print(word, "->", animals_dict[word]) # ... wyciągnij słówko (odwołaj się do słownika po kluczu "word")
    else:
        print("Nie znaleziono słowa", word,  "w słowniku.") # ... wyświetl komunikat o braku słówka w słowniku
"""
Wyniki:
kot -> cat
Nie znaleziono słowa lew w słowniku.
chomik -> hamster
"""



# # ITEROWANIE PO SŁOWNIKU
# # Słownik nie jest obiektem sekwencyjnym - nie można po nim bezpośrednio iterować, ale są na to sposoby.

# # SPOSÓB 1. Można iterować po kluczach - wyciąganie metodą keys() wszystkich kluczy.
for key in animals_dict.keys(): # nie trzeba zapisywać ".keys()", domyślnie jest to najczęstsze odwołanie do słowników
    print(key, "->", animals_dict[key]) # Jeżeli mamy klucz, to mamy też wartość, ponieważ za pomocą klucza
    # w łatwy sposób można odwołać się do słownika
"""
Wyniki:
kot -> cat
pies -> dog
chomik -> hamster

Istnieje uproszczony sposób zapisu - nie trzeba zapisywać metody ".keys()", ponieważ twórcy języka Python przewidzieli, 
że to będzie najczęstszy sposób odwołania do słowników. Wersja bez metody keys():

for key in animals_dict:
    print(key, "->", animals_dict[key])
"""


# # SPOSÓB 2. metoda values() - wyciąganie tylko i wyłącznie wartości:
for val in animals_dict.values():
    print(val) # Zamykamy możliwości, ponieważ wyświetlą się tylko wartości w słowniku, a nie wyświetlą się klucze.
"""
Wyniki:
cat
dog
hamster
"""


# # SPOSÓB 3. PODEJŚCIE 1. wyciąganie krotek - metoda items()
for item in animals_dict.items(): # wyciągamy elementy, tzw. "itemy".
    print(item) # dostaniemy zestaw krotek ('klucz', 'wartość')
"""
Wyniki: 
('kot', 'cat')
('pies', 'dog')
('chomik', 'hamster')

Krotka jest pewnym zabezpieczeniem, aby nie pozwolić na modyfikację danych w słowniku.
"""

# # SPOSÓB 3. PODEJŚCIE 2. Zamiast zapisywać w jednej zmiennej można od razu zapisać "klucz-wartość".
for pl, en in animals_dict.items():
    print(pl, "->", en) # działa jak: a, b = (1, 2) ==> a = 1, b = 2
"""
W przypadku powyżej można odwoływać się przez zmienne "pl" i "en".
Działa to na zasadzie:
    a, b = (1, 2)
    print(a)
    print(b)
    
    Wynik:
    1
    2

Wyniki:
kot -> cat
pies -> dog
chomik -> hamster
"""



# # MODYFIKACJA SŁOWNIKA

# # DOPISANIE. Jeżeli chcemy dopisać jakiś element, to wywołujemy słownik, podajemy [klucz] i dopisujemy "wartość".
animals_dict["świnka"] = "pig" # KLUCZ:WARTOŚĆ
print(animals_dict)  # {'kot': 'cat', 'pies': 'dog', 'chomik': 'hamster', 'świnka': 'pig'}


# # AKTUALIZACJA - DODANIE KLUCZA/ MODYFIKACJA KLUCZA JUŻ ISTNIEJĄCEGO - metoda update()
# # 1. Dodawanie klucza.
animals_dict.update({"kurczak": "chicken"})
print(animals_dict)  # {'kot': 'cat', 'pies': 'dog', 'chomik': 'hamster', 'świnka': 'pig', 'kurczak': 'chicken'}

# # 2. Zmiana/ modyfikacja
animals_dict.update({"świnka": "piggy"})
print(animals_dict)  # {'kot': 'cat', 'pies': 'dog', 'chomik': 'hamster', 'świnka': 'piggy', 'kurczak': 'chicken'}
# # Element "świnka" nie zmieni swojego położenia (nie zostanie przesunięty na koniec), ponieważ ten klucz już istniał.
# # Za pomocą metody update() zmieniono jedynie wartość dla tego klucza.



# # KOPIA SŁOWNIKA - metoda copy()
dict2 = animals_dict.copy()  # użycie metody copy()
print(dict2)  # metoda copy() powoduje, że dostaniemy kopię słownika "animals_dict".



# # USUWANIE ELEMENTÓW - funkcja del, metoda popitem() i metoda clear():
# # Jeżeli będziemy chcieli usunąć konkretny element, to tak jak w przypadku list można użyć funkcji del
del dict2["świnka"] # w notacji nawiasów kwadratowych podajemy, co chcemy usunąć
print(dict2)  # {'kot': 'cat', 'pies': 'dog', 'chomik': 'hamster', 'kurczak': 'chicken'}

# # Jeżeli chcemy usunąć ostatni element, przyda się metoda popitem()
dict2.popitem() # zniknie ostatni element. Za każdym kolejnym wywołaniem funkcji będą usuwane pojedyncze elementy.
print(dict2)  # {'kot': 'cat', 'pies': 'dog', 'chomik': 'hamster'}

# # Usunięcie wszystkich elementów - użycie metody clear()
dict2.clear() # Wyczyści cały słownik
print(dict2)  # {} 