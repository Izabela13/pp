# # IMPORTOWANIE MODUŁÓW

#######################################################################################################################
#######################################################################################################################

# # IMPORTOWANIE CAŁEGO MODUŁU
# # import "nazwa_modułu"

#######################################################################################################################

# # IMPORTOWANIE CAŁEGO MODUŁU "MATH" I ODWOŁYWANIE SIĘ DO JEGO ELEMENTÓW

# import math  # słowo kluczowe "import" + nazwa importowanego modułu, np. "math".
# # Dopóki moduł nie zostanie wykorzystany, PyCharm pokazuje nam go w kolorze szarym.

# # Odwołanie się do elementu danego modułu: "nazwa_modułu"."nazwa_elementu"
# print(math.pi)  # 3.141592653589793
# print(math.sin(math.pi/2))  # 1.0

#######################################################################################################################

# # SPOSOBY IMPORTOWANIA KILKU MODUŁÓW NA RAZ

# # Jeżeli chcemy zaimportować kilka modułów, to można zaimportować je za pomocą jednego importu:
# import math, sys

# # Czytelniejszym sposobem importowania wielu modułów jest importowanie ich linia po linii:
# import math
# import sys

# # Po słowie kluczowym można wpisywać kolejne moduły, ale zaleca się pisanie jeden pod drugim.

#######################################################################################################################

"""
Jak korzystać z modułów?
W przeglądarce wystarczy wpisać hasło "python standard library".
W dokumentacji Pythona znajduje się kompletny opis wszystkich elementów, które są w standardowej bibliotece Pythona.

Część funkcji jest wbudowana w Pythona. Funkcje wbudowane to funkcje, z których można korzystać bez żadnego importu.
Np. len(), type(), input(), int(), print()

Indeks elementów - wersja Pythona - Global Module Index
"""

#######################################################################################################################

# # PRZYKŁADY WYKORZYSANIA FUNKCJI Z MODUŁU "MATH"

# import math
# import sys

# # Wyświetlenie wartości silnii - funkcja "factorial()" w module math:
# print(math.factorial(5))  # 1 * 2 * 3 * 4 * 5; Wynik: 120
# print(math.factorial(12)) # Wynik: 479001600

# # Funkcja floor() z modułu math
# print(math.floor(4.9999))  # Wynik: 4 - ścięcie w dół

#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################

# # IMPORTOWANIE WYBRANYCH ELEMENTÓW MODUŁU
# # from "nazwa_modułu" import "nazwa_funkcji"

#######################################################################################################################

# # IMPORTOWANIE JEDNEGO ELEMENTU Z MODUŁU "MATH" I KWESTIE Z TYM ZWIĄZANE

# # Gdy chcemy zaimportować tylko jeden element:
# from math import pi

# # Do elementu danego modułu można odwołać się tylko po nazwie tego elementu:
# print(pi)

# # Nie zadziała natomiast dodanie nazwy modułu przed nazwą elementu:
# # print(math.pi)
# # Powyższe wyrażenie wygeneruje wyjątek "NameError". Nazwa "math" w przestrzeni nazw jest już niedostępna.

# # Jeżeli importujemy pojedyncze elementy modułów, to odwołanie się do elementu, którego nie zaimportowano
# # również jest niedostępne, np.:
# # print(sin(pi / 2)) # to wyrażenie wygeneruje błąd, ponieważ nazwa "sin" nie jest dostępna w tym momencie.
# # print(math.sin(pi/2)) # to wyrażenie również nie spowoduje możliwości wykorzystania funkcji "sin".
# # W powyższym przykładzie dostępne jest tylko i wyłącznie "pi". Jest to efekt pożądany, którzy porządkuje kod.

#######################################################################################################################

# # IMPORTOWANIE KILKU ELEMENTÓW Z MODUŁU "MATH" - PRZYKŁADY I KWESTIE Z TYM ZWIĄZANE

#from math import pi, sin, factorial, ceil

# print(pi)  # 3.141592653589793
# print(sin(pi/2))  # 1.0
# print(factorial(7))  # 5040
# print(ceil(3.8))  # 4

# # Można pobierać również wszystkie elementy danego modułu, ale ten sposób jest niezalecany i bardzo ryzykowny.
# from math import *

#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################

# # ALIASOWANIE - IMPORTOWANIE POD NOWĄ NAZWĄ
# # import "nazwa_modułu" as "nowa_nazwa_modułu"
# # from "nazwa_modułu" import "nazwa_funkcji" as "nowa_nazwa_funkcji"

#######################################################################################################################

# # Jeżeli zaimportujemy w sposób klasyczny moduł "math", to za pomocą aliasu można przypisać nową nazwę dla modułu.
# import math as m

# # Moduł "math" będzie teraz dostępny pod nazwą "m". Od tej pory do elementów modułu "math" można odwoływać się
# # za pomocą nazwy zastępczej "m" (aliasu).

# print(m.pi)


# # Gdybyśmy chcieli wrócić do nazwy modułu "math", będzie on niedostępny.
# # print(math.pi)

# # Samo "pi" również nie będzie dostępne:
# # print(pi)

# # Konsekwentnie trzeba używać aliasu.

#######################################################################################################################

# # Jeżeli chcielibyśmy zaimportować pojedyncze elementy moduły "math", to za pomocą aliasu można nadać pobranemu
# # elementowi nową nazwę.

# from math import pi as mathpi
# # Stała "pi" będzie dostępna tylko i wyłącznie pod nową nazwą ("mathpi")

# print(mathpi)

# # Stała "pi" nie będzie dostępna pod nazwą "math.pi" ani "pi".
# # print(maht.pi) # odwołanie się do nazwy modułu jest niedostępne.
# # print(pi)      # wywołanie stałej "pi" przez samo "pi" jest niedostępne.

#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################

# # Przejście do skryptu "dir()_function".

#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################

# WYKORZYSANIE ELEMENTÓW NIEKTÓRYCH MODUŁÓW

#######################################################################################################################

# WYKORZYSANIE ELEMENTÓW NIEKTÓRYCH ELEMENTÓW MODUŁU "RANDOM" - "RANDINT" i "SEED"


# import random

# print(random.randint(1, 3))  # Losowanie jednej liczby z zakresu od 1 do 3.

# # Funkcja random() nie przyjmuje żadnych elementów. Wylosuje ona liczbę rzeczywistą z przedziału od 0 do >1
# print(random.random())  # np. 0.5246580416497025


# # Element seed() - ziarno, od którego zależy, jak ten algorytm będzie generował liczby.
# from random import random, seed

# # Wygenerowanie 5-ciu pseudolosowych liczb:
# for i in range(5):
#    print(random())
"""
Przy każdym losowaniu będą pojawiać się pseudolosowe liczby. Za każdym razem te liczby będą inne.
Liczby będą inne, ponieważ ten algorytm jest tak zbudowany, że to ziarno, od którego zależy generowanie tego ciągu
liczb jest oparte na jakimś zmiennym elementcie, np. na zegarze komputera.
"""

"""
Udowodnimy, że jeżeli wywołamy funkcję "seed" i ustawimy ją na jakąś stałą, która nie będzie się zmieniać, to
za każdym losowaniem ciąg liczb będzie identyczny.
"""

# seed(0)  # Przy każdym losowaniu ciąg liczb będzie taki sam, np. przy dodaniu do funkcji "seed" argumentu o wartości 0:

# for i in range(5):
#    print(random())
"""
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085

Jest to dowód na to, że losowanie liczb przez komputer jest zawsze oparte o jakiś punkt odniesienia, ponieważ komputer
może wygenerować jakieś wartości na podstawie jakiegoś zmieniającego się parametru.
"""

#######################################################################################################################

# WYKORZYSANIE ELEMENTÓW NIEKTÓRYCH ELEMENTÓW MODUŁU "RANDOM" - "CHOICE" I "SAMPLE"


# from random import choice, sample  # przy takim imporcie mamy do dyspozycji tylko dwa elementy.

# # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = [i for i in range(1, 11)]  # generowanie elementów listy za pomocą wyrażenia listowego

# print(choice(list))      # wybieranie liczby ze zbioru "list" (losowanie)
# print(sample(list, 5))   # Liczby losowane bez powtórzeń
# print(sample(list, 10))  # Za każdym razem liczby będą w innym ułożeniu
# # Jeżeli będziemy chcieli 11 liczb, dostaniemy wyjątek ValueError, ponieważ przekroczy zakres dostępnych liczb.

#######################################################################################################################

# WYKORZYSANIE ELEMENTÓW NIEKTÓRYCH ELEMENTÓW MODUŁU "PLATFORM"

# import platform

# # help(platform)  # po wywołaniu funkcji help() dostaniemy dokładny opis tego, co zawiera dany moduł

# print(platform.machine())               # AMD64 - ogólna nazwa procesora
# print(platform.processor())             # Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
# print(platform.system())                # Windows
# print(platform.version())               # 10.0.22621
# print(platform.python_implementation()) # CPython
# print(platform.python_version_tuple())  # ('3', '10', '7')

"""
Funkcja machine(): 
- wyświetlenie ogólnej nazwy procesora
- Komputery na których pracujemy na uczelni są zbudowane na procesorze firmy AMD64

Funkcja processor():
- szczegółowsze informacje, tj. dokładne informacje o procesorze. 
- pod nazwą Intel są podkładki z nazwą AMD

Funkcja  system():
- ogólna nazwa systemu operacyjnego (wynik: Windows)

Funkcja version():
- dokładna wersja systemu operacyjnego (wynik: 10.0.22621)

Funkcja python_implementation()
- z jakiej implementacji Pythona korzystamy na uczelni (wynik: CPython)

Funkcja python_version_tuple():
- z jakiej wersji Pythona korzystamy na uczelni (wynik: ('3', '10', '7'))
"""


# from platform import machine, version
# help(machine)
# print(machine())

# help(version)
# print(version()) # 10.0.22621 - Windos 11, numer oprogramowania 10.0.22621


# from platform import platform

# help(platform)
# print(platform()) # Windows-10-10.0.22621-SP0 (nazwa marketingowa Windows 11)

"""
Funkcja "platform()" ma dwa parametry:
platform(aliased=0, terse=0) - typ bool
"""

# print(platform(True, True)) # Windows-10 (nadal jest to nowy system operacyjny znany pod nazwą Windows 11)

#######################################################################################################################
#######################################################################################################################