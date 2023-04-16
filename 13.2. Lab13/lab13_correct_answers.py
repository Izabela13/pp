# # Zadanie 1: power_numbers

# def pow(numbers, exponent):  # funkcja będzie przyjmowała 2 parametry: listę ("numbers") i potęgę ("exponent")
#     for i in range(len(numbers)):  # iterowalna pętla + sprawdzanie funkcją len() ilości elementów w liście
#         numbers[i] = numbers[i] ** exponent  # podnoszenie do poęti od razu będzie modyfikować listę
#     return numbers  # zwrócenie listy po wykonaniu operacji potęgowania

# print(pow([1, 2, 3], 2))  # do funkcji "pow" zostaje przekazana tablica (lista) i potęga
# print(pow([2, 7, 33], 5))


# # WARIACJE DO ZADANIA 1
# # W przykładzie zostaje zwrócona lista numbers (return). Nawet jeżeli lista nie byłaby zwracana to i tak zostnie
# # zmodyfikowana. Istnieje ryzyko, że podstawiona do funkcji referencja do listy i tak zmodyfikuje listę.

# # wariacja 1
# def pow2(numbers, exponent):  # 2 parametry: lista ("numbers") i potęga ("exponent")
#     result = [] # kopia tablcy  # pusta lista (zmienna lokalna "result")

#     for n in numbers:  # iterowanie od razu po liście "numbers" - indeksy nie będą wywoływane
#         result.append(n ** exponent)  # do nowej listy "result" za pomocą metody append będą dodawane nowe wartości
#     return result  # bezpieczniejsze podejście, ponieważ tworzona jest kopia tablicy

# print(pow2([1, 2, 3], 2))
# print(pow2([2, 7, 33], 5))


#  wariacja 2 (kompaktowa)
# def pow3(numbers, exponent):
#     return [x ** exponent for x in numbers]  # wykorzystanie wyrażenia listowego

# print(pow3([1, 2, 3], 2))
# print(pow3([2, 7, 33], 5))



# # Zadanie 2 multiplication_table

# def show_operation(a, b):  # przekazanie 2 parametrów ("a" i "b")
#     print(a, "x", b, "=", a*b)  # funkcja będzie wyświetlała operację mnożenia
      # rekurencja: po wyświetleniu pierwszej operacji, wyświetlamy kolejną
#     if a == 10 and b == 10: # zabezpieczenie programu, aby program zatrzymał się w którymś momencie
#         return  # jeżeli a = 10 i b = 10, to zatrzymaj się (zwróć "None")
#     elif a == 10:
#         show_operation(1, b + 1) # jeżeli a = 10, to zwiększanie "b" o 1 i podstawienie pod "a" wartości 1
#     else: # jeżeli a jest inne niż 10, to...
#         show_operation(a + 1, b) # ... zwiększ "a" o 1 i zostaw wartość "b".

# show_operation(1, 1)
"""
if a == 10 and b == 10:
    return
W tym bloku zostanie wyłapana sytuacja skrajna, czyli moment, w którym "a" = 10 i "b" = 10. Ta sytuacja ma definitywnie
zakończyć cały algorytm.

Jeżeli "a" = 10, a "b" jest inne niż 10, to program wejdzie do bloku elif:
elif a == 10:
    show_operation(1, b + 1)
Dojdzie do "resetu" dla "a", czyli do zmiennej "a" zostanie przypisana wartość 1 (czyli program znowu zacznie liczyć od 1),
ale jednocześnie zwiększy się wartość zmiennej "b" (b + 1). Program znowu wejdzie do pętli, ale zmienna "b" zostanie
zwiększona.

Program zatrzyma się, gdy dojdzie do a = 10 i b = 10. Te wartości jeszcze się wyświetlą.

W tym przykładzie:
REKURENCJA, czyli wywołanie funkcji w funkcji.
DODANIE WARUNKÓW, które mają doprowadzić do wyhamowania funkcji, gdy tabliczka mnożenia dojdzie do 10 x 10 = 100.
"""



# Zadanie 3 simple fruit machine

"""
3. Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
w tym celu:
• za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
• kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
• wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
• przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
większą liczbę liter.
"""

# import random  # na pewno będzie potrzebny moduł random.

"""
Jeżeli mamy losowanie liter, to mogą być pomocne dwie funkcje:
1) ord() - od nazwy "ordinal", czyli "uporządkowanie". Funkcja zwraca numer reprezentowany przez dany znak, np.
print(ord("A")) --> 65, co oznacza, że w tabeli ASCI znak "A" jest reprezentowany przez wartość 65.
2) chr() - od nazwy "character". Funkcja zamienia wartość liczbową na znak, np.
print(chr(65)) --> "A"
"""
## print(ord()) # będzie zwracać numerek reprezentowany przez dany znak

# # Definiowanie funkcji i rozbijanie na moduły logiczne (części składowe zadania).

# # 1. Za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E.

# # I moduł - wylosowanie jednej litery.
# def draw_letter():
#     return chr(random.randint(ord("A"), ord("E")))  # Zwróć literę (można też wpisać 65-69)

# # II moduł - wylosowanie całego rzędu liter.
# def draw_row(): # funkcja "wylosuj cały rząd"
#     return [draw_letter() for i in range(3)] # użycie wyników funkcji draw_letter() dla pętli for


# # 2. Kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A.
"""
"Kontynuuj losowanie", czyli: 
1) losowanie będzie musiało przebiegać w jakiejś pętli. 
2) w którymś momencie będzie trzeba przerwać pętlę.

Stąd dopisanie funkcji, która będzie sprawdzała, czy dany rząd liter to moment, w którym litery są takie same.
"""

# def check(row): # funkcja ma parametr "row". Do funkcji będzie podstawiany wylosowany rząd liter.
#     if row[0] == row[1] and row[1] == row[2]: # Warunek sprawdzający, czy element z indeksem[0] jest taki sam jak...
#         return True # Jeżeli warunek jest spełniony, to mamy pewność, że wszystkie elementy są sobie równe.
#     else:
#         return False


# # 3. PĘTLA, KTÓRA BĘDZIE REALIZOWAŁA LOSOWANIA, WYŚWIETLAŁA INFORMACJĘ O WYNIKACH LOSOWAŃ I NUMERZE PRÓBY
# counter = 1 # ilość losowań będzie zapisywana w liczniku
# while True: # iterowanie w pętli while. Pętla while zacznie się od wartości "True".
#     row = draw_row()    # rząd liter zapisywany będzie do zmiennej "row". Losowanie rządu liter za pomocą funkcji.
#     print(row, counter) # wyświetlenie użytkownikowi rzędu liter i numeru próby.
#     if check(row):      # sprawdzenie. Jeżeli okaże się, że w rzędzie znajdują się trzy takie same litery, to...
#         break           # ... przerywamy pętlę - korzystamy z instrukcji break.
#     else:               # jeżeli nie, to pętla przechodzi do kolejnego losowania, i...
#         counter += 1    # ... zmienna "counter" zostaje podniesiona o 1.

# # Przy takich założeniach, że zbiór jest dość mały, bardzo trudno jest przekroczyć wartość 100.



# # Jak dużo zmian trzebaby wprowadzić w skrypcie, żeby zwiększyć ilość liter do wylosowania i zakres losowania?

# # SYMULACJA

# # Zwiększenie zakresu liter
"""
Dla przygotowanej funkcji draw_letter() zmianę można wprowadzić w jednym miejscu, tj. w miejsce ord("E") wstawić, np. H.
Jeżeli natomiast chcemy przygotować skrypt do późniejszych zmian, to możemy zdefiniować pewne stałe (pod które można 
później podstawiać wartości).
"""

import random

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5


def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))  # 1 ZMIANA - wprowadzenie stałych


def draw_row():
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]  # 2 ZMIANA - losowanie do ustalonej stałej


def check(row):  # 3 ZMIANA - losowanie do wartości NUMBER_OF_LETTERS

    first_element = row[0] # pomocnicza zmienna lokalna, do której zostanie zapisany pierwszy element wylosowanego rzedu

    for element in row: # iteracja po wylosowanym rzędzie
        if element != first_element: # czy kolejny element nie jest równy pierwszemu elementowi wylosowanego rzędu...
            return False # ... jeżeli nie, to wychodzimy z pętli (return False).
    return True  # jeżeli przejdziemy pętlę, to znaczy, że wszystko jest identyczne.


counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

"""
Przy niewielkim zwiększeniu liczby elementów ilość losowań dochodzi do dziesiątków tysięcy. 
"""
