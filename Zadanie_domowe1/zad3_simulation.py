"""
Napisz skrypt pozwalający zasymulować zyski z lokat bankowych przy
następujących założeniach:
• własne środki 30 tys. zł,
• roczna lokata kapitału,
• kwartalna kapitalizacja odsetek (saldo będzie aktualizowane co 3 miesiące),
• oprocentowanie roczne dla 3 wariantów: 7,5%, 8% oraz 8,25%,
• pokazać salda po każdym kwartale,
• wyliczyć roczny zysk
"""

from time import sleep

print("\n"
"Symulacja zysków z lokat bankowych dla trzech rodzajów oprocentowania: \n"
"- 7.5 %; \n"
"- 8.0 %; \n"
"- 8.25 %; \n")

sleep (5) # czas na przeczytanie informacji

print(
"Kluczowe informacje: \n"
"- środki własne = 30 000 zł; \n"
"- roczna lokata kapitału; \n"
"- kwartalna kapitalizacja odsetek; \n")

sleep (5) # czas na przeczytanie informacji

print(
"Prezentacja salda po każdym kwartale oraz określenie rocznego zysku \n"
"dla każdego z trzech rodzajów oprocentowania rocznego."
"\n"
"\n")

sleep (5) # czas na przeczytanie informacji



# Tworzenie zmiennej przechowującej wkład początkowy oraz funkcji przechowującej oprocentowanie
own_funds = 30_000 # środki własne


def year_bank_rate(percent):
       if (percent == 0.0):
              return print("Wprowadzono wartość 0. Nie można wykonać działania")
       else:
              return float(percent)



# 1. Oprocentowanie roczne 7.5%
print("Symulacja zysku dla oprocentowania rocznego " + str(year_bank_rate(7.5)) + " %. \n")

sleep (5) # czas na przeczytanie informacji

quarter_bank_rate = year_bank_rate(7.5) / 4 # zmienna obliczająca oprocentowanie kwartalne z wartości podanej w funkcji
print("Przy oprocentowaniu rocznym w wysokości " + str(year_bank_rate(7.5)) + " %" + " kapitalizacja odsetek za każdy kwartał \n"
       "będzie wynosić: " + str(quarter_bank_rate) + " %." + " (wysokość oprocentowania rocznego / 4).")

sleep (5) # czas na przeczytanie informacji


# Krok 2. Wykorzystanie pętli while do określenia salda po każdym kwartale
own_funds_basic = 30000
i = 1 # iteracja
print(
"Dane prezentują się następująco: \n"
"kapitał początkowy = " + str(own_funds) + " zł;")
while i <= 4:
       i += 1
       own_funds = round(own_funds + (own_funds * (quarter_bank_rate/100)), 2)
       sleep(5)
       print(
             str(i - 1) + " kwartał: saldo konta: " + str(own_funds) + " zł; "
           + "zysk kwartalny w stosunku do kwoty bazowej: " + str(round(own_funds - own_funds_basic, 2)) + " zł; ")

sleep (5) # czas na przeczytanie informacji


own_funds_cap1 = round(own_funds_basic + own_funds_basic * (quarter_bank_rate/100),2)
own_funds_cap2 = round(own_funds_cap1 + own_funds_cap1 * (quarter_bank_rate/100),2)
own_funds_cap3 = round(own_funds_cap2 + own_funds_cap2 * (quarter_bank_rate/100),2)
own_funds_cap4 = round(own_funds_cap3 + own_funds_cap3 * (quarter_bank_rate/100),2)

print(
"\n"
"Zestawienie tabelaryczne salda po każdym kwartale: \n"
"Kwartał" + " " * 2 + "Kapitał Początkowy" + " " * 2 + "Odsetki" + " " * 5 + "Kapitał Końcowy" + " \n" +
"   I   " + " " * 2 + str(own_funds_basic) + " zł" + " " * 12 +
str(round(own_funds_cap1 - own_funds_basic, 2)) + " zł" +  " "  * 4 + str(own_funds_cap1) + " zł \n"

"   II  " + " " * 2 + str(own_funds_cap1) + " zł" + " " * 10 +
str(round(own_funds_cap2 - own_funds_cap1, 2)) + " zł" +  " "   * 3 + str(own_funds_cap2) + " zł \n"

"   III " + " " * 2 + str(own_funds_cap2) + " zł" + " " * 9 +
str(round(own_funds_cap3 - own_funds_cap2, 2)) + " zł" +  " "   * 3 + str(own_funds_cap3) + " zł \n"

"   IV  " + " " * 2 + str(own_funds_cap3) + " zł" + " " * 9 +
str(round(own_funds_cap4 - own_funds_cap3, 2)) + " zł" +  " "   * 3 + str(own_funds_cap4) + " zł \n")

sleep (10) # czas na przeczytanie informacji

print("Przy 30 000 zł lokacie, kwartalnej kapitalizacji odsetek i oprocentowania rocznego " + str(year_bank_rate(7.5)) + " % \n"
      "zysk roczny wynosi: " + str(round(own_funds - own_funds_basic, 2)) + " zł.")

sleep (5) # czas na przeczytanie informacji
###############################################################################################################################



# 2. Oprocentowanie roczne 8.0%
print(
"\n" * 3 +
"Symulacja zysku dla oprocentowania rocznego " + str(year_bank_rate(8.0)) + " %. \n")

sleep (5) # czas na przeczytanie informacji

quarter_bank_rate = year_bank_rate(8.0) / 4 # zmienna obliczająca oprocentowanie kwartalne z wartości podanej w funkcji
print("Przy oprocentowaniu rocznym w wysokości " + str(year_bank_rate(8.0)) + " %" + " kapitalizacja odsetek za każdy kwartał \n"
       "będzie wynosić: " + str(quarter_bank_rate) + " %." + " (wysokość oprocentowania rocznego / 4).")

sleep (5) # czas na przeczytanie informacji


# Krok 2. Wykorzystanie pętli while do określenia salda po każdym kwartale
own_funds_basic = 30000
own_funds = 30000 # przy wcześniejszej pętli zmienna 'own_funds' została nadpisana.
i = 1 # iteracja

print(
"Dane prezentują się następująco: \n"
"kapitał początkowy = " + str(own_funds) + " zł;")
while i <= 4:
       i += 1
       own_funds = round(own_funds + (own_funds * (quarter_bank_rate/100)), 2)
       sleep(5)
       print(
             str(i - 1) + " kwartał: saldo konta: " + str(own_funds) + " zł; "
           + "zysk kwartalny w stosunku do kwoty bazowej: " + str(round(own_funds - own_funds_basic, 2)) + " zł; ")

sleep (5) # czas na przeczytanie informacji


own_funds_cap1 = round(own_funds_basic + own_funds_basic * (quarter_bank_rate/100),2)
own_funds_cap2 = round(own_funds_cap1 + own_funds_cap1 * (quarter_bank_rate/100),2)
own_funds_cap3 = round(own_funds_cap2 + own_funds_cap2 * (quarter_bank_rate/100),2)
own_funds_cap4 = round(own_funds_cap3 + own_funds_cap3 * (quarter_bank_rate/100),2)

print(
"\n"
"Zestawienie tabelaryczne salda po każdym kwartale: \n"
"Kwartał" + " " * 2 + "Kapitał Początkowy" + " " * 2 + "Odsetki" + " " * 5 + "Kapitał Końcowy" + " \n" +
"   I   " + " " * 2 + str(own_funds_basic) + " zł" + " " * 12 +
str(round(own_funds_cap1 - own_funds_basic, 2)) + " zł" +  " " * 4 + str(own_funds_cap1) + " zł \n"

"   II  " + " " * 2 + str(own_funds_cap1) + " zł" + " " * 10 +
str(round(own_funds_cap2 - own_funds_cap1, 2)) + " zł" +  " " * 4 + str(own_funds_cap2) + " zł \n"

"   III " + " " * 2 + str(own_funds_cap2) + " zł" + " " * 10 +
str(round(own_funds_cap3 - own_funds_cap2, 2)) + " zł" +  " " * 3 + str(own_funds_cap3) + " zł \n"

"   IV  " + " " * 2 + str(own_funds_cap3) + " zł" + " " * 9 +
str(round(own_funds_cap4 - own_funds_cap3, 2)) + " zł" +  " " * 3 + str(own_funds_cap4) + " zł \n")

sleep (10) # czas na przeczytanie informacji

print("Przy 30 000 zł lokacie, kwartalnej kapitalizacji odsetek i oprocentowania rocznego " + str(year_bank_rate(8.0)) + " % \n"
      "zysk roczny wynosi: " + str(round(own_funds - own_funds_basic, 2)) + " zł.")

sleep (5) # czas na przeczytanie informacji
###############################################################################################################################



# 3. Oprocentowanie roczne 8.25%
print(
"\n" * 3 +
"Symulacja zysku dla oprocentowania rocznego " + str(year_bank_rate(8.25)) + " %. \n")

sleep (5) # czas na przeczytanie informacji

quarter_bank_rate = year_bank_rate(8.25) / 4 # zmienna obliczająca oprocentowanie kwartalne z wartości podanej w funkcji
print("Przy oprocentowaniu rocznym w wysokości " + str(year_bank_rate(8.25)) + " %" + " kapitalizacja odsetek za każdy kwartał \n"
       "będzie wynosić: " + str(quarter_bank_rate) + " %." + " (wysokość oprocentowania rocznego / 4).")

sleep (5) # czas na przeczytanie informacji


# Krok 2. Wykorzystanie pętli while do określenia salda po każdym kwartale
own_funds_basic = 30000
own_funds = 30000 # przy wcześniejszej pętli zmienna 'own_funds' została nadpisana.
i = 1 # iteracja

print(
"Dane prezentują się następująco: \n"
"kapitał początkowy = " + str(own_funds) + "zł;")
while i <= 4:
       i += 1
       own_funds = round(own_funds + (own_funds * (quarter_bank_rate/100)), 2)
       sleep(5)
       print(
             str(i - 1) + " kwartał: saldo konta: " + str(own_funds) + " zł; "
           + "zysk kwartalny w stosunku do kwoty bazowej: " + str(round(own_funds - own_funds_basic, 2)) + " zł; ")

sleep (5) # czas na przeczytanie informacji


own_funds_cap1 = round(own_funds_basic + own_funds_basic * (quarter_bank_rate/100),2)
own_funds_cap2 = round(own_funds_cap1 + own_funds_cap1 * (quarter_bank_rate/100),2)
own_funds_cap3 = round(own_funds_cap2 + own_funds_cap2 * (quarter_bank_rate/100),2)
own_funds_cap4 = round(own_funds_cap3 + own_funds_cap3 * (quarter_bank_rate/100),2)

print(
"\n"
"Zestawienie tabelaryczne salda po każdym kwartale: \n"
"Kwartał" + " " * 2 + "Kapitał Początkowy" + " " * 2 + "Odsetki" + " " * 5 + "Kapitał Końcowy" + " \n" +
"   I   " + " " * 2 + str(own_funds_basic) + " zł" + " " * 12 +
str(round(own_funds_cap1 - own_funds_basic, 2)) + " zł" +  " " * 3 + str(own_funds_cap1) + " zł \n"

"   II  " + " " * 2 + str(own_funds_cap1) + " zł" + " " * 9 +
str(round(own_funds_cap2 - own_funds_cap1, 2)) + " zł" +  " " * 3 + str(own_funds_cap2) + " zł \n"

"   III " + " " * 2 + str(own_funds_cap2) + " zł" + " " * 9 +
str(round(own_funds_cap3 - own_funds_cap2, 2)) + " zł" +  " " * 3 + str(own_funds_cap3) + " zł \n"

"   IV  " + " " * 2 + str(own_funds_cap3) + " zł" + " " * 10 +
str(round(own_funds_cap4 - own_funds_cap3, 2)) + " zł" +  " " * 3 + str(own_funds_cap4) + " zł \n")

sleep (10) # czas na przeczytanie informacji

print("Przy 30 000 zł lokacie, kwartalnej kapitalizacji odsetek i oprocentowania rocznego " + str(year_bank_rate(8.25)) + " % \n"
      "zysk roczny wynosi: " + str(round(own_funds - own_funds_basic, 2)) + " zł.")

sleep (5) # czas na przeczytanie informacji
###############################################################################################################################