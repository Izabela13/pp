"""
1. Napisz skrypt symulujący grę losową:
• użytkownik obstawia 6 liczb z 49,
• program losuje 6 liczb z 49,
• użytkownik dostaje informacje o ilości trafień.
"""

# import bibliotek
import random
from time import sleep




# Zmienna przechowująca wartość kumulacji w danym czasie.
rollover = 8_000_000   # Kumulacja w lotto - stan na dzień 18.02.2023.


# KOMUNIKATY
print("WEJDŹ DO ŚWIATA LOTTO!!! \n"), sleep(3)
print("W losowaniu bierze udział 49 liczb. Wygrywasz za więcej niż 2 trafienia."), sleep(2)

if rollover > 0:
    print("Obecnie do rozbicia kumulacja równa " + "{:,d}".format(rollover).replace(",", " ") + " zł!!! \n"), sleep(2)

print("Obstaw 6 liczb i sprawdź, czy wygrałeś/ aś. \n"), sleep(2)




# Tworzenie listy 49 liczb, z której zostanie wylosowana sekwencja 6-ciu liczb
lotto_list = []

for numb_in_game in range(1, 50):
    lotto_list.append(numb_in_game)
# Instrukcja do symulacji - najpierw gracz obstawia 6 liczb, następnie program losuje 6 liczb




# OBSTAWIANIE LICZB PRZEZ GRACZA
# Tworzenie listy 6 liczb wybranych przez gracza.
bettor_numbers = []

# zastosowanie pętli
counter = 1 # licznik wprowadzanych liczb

while counter <= 6:
    bet_number = int(input("Wprowadź " + str(counter) + " liczbę: "))
    if bet_number in bettor_numbers:
        print("Uwaga! Wprowadzono tę samą liczbę! Nie zmniejszaj swojej szansy na wygraną!")
        counter = counter
    elif bet_number < 1 or bet_number > 49:
        print("Uwaga! Wprowadzono liczbę spoza zakresu 1-49. Podaj ponownie liczbę mieszczącą się we wskazanym zakresie.")
        counter = counter
    else:
        bettor_numbers.append(bet_number)
        counter += 1
else:
    print("")
    print("Wytypowane przez Ciebie liczby to: ", end="")

for mark in bettor_numbers:
    print(mark, end="  ")

print("\n")
sleep(3)




# LOSOWANIE
# Tworzenie losowej sekwencji sześciu liczb
lotto = random.sample(lotto_list, 6)
## print(lotto)




# SPRAWDZANIE TRAFIEŃ
# bettor_numbers - lista liczb wybranych przez gracza
# lotto - lista liczb wylosowanych przez "maszynę losującą"

hits = []  # lista trafionych przez gracza liczb (lista "trafień")

for bet in bettor_numbers:
    if bet in lotto:
        hits.append(bet)


print("Wylosowane liczby Lotto to: ", end="")
for enum in lotto:
    print(enum, end="  ")

print("\n")
sleep(3)




# WYGRANE
"""
W Lotto, w ramach jednego zakładu prostego, ustala się cztery stopnie wygranych:
1) I   stopień - za 6 trafnie wytypowanych liczb, 
2) II  stopień - za 5 trafnie wytypowanych liczb, 
3) III stopień - za 4 trafnie wytypowane liczby,
4) IV  stopień - za 3 trafnie wytypowane liczby.

W przypadku gdy:    Stopień wygranych               Kumulacja
                    I       II      III     IV
występują wygrane
wszystkich stopni   44%     8%       % zmienny          -

brak wygranej 
I stopnia           -       8%       % zmienny         44%

brak wygranej 
II stopnia         44%       -       % zmienny          -

brak wygranych 
I i II stopnia      -        -       % zmienny          44%


WERSJA UPROSZCZONA NAGRÓD
                                    Nagrody wg. stanu na luty 2023     Średnia wypłaza w ostatnich 100 losowaniach
Nagroda IV stopnia (3 trafienia)  - gwarantowane 24 zł.                -
Nagroda III stopnia (4 trafienia) - 255,60 zł                          174,08 zł
Nagroda II stopnia (5 trafień)    - 7 461,10 zł                        5 495,77 zł
Nagroda I stopnia (6 trafień)     - gwarantowane 2 000 000 zł          - 
"""
prize_for_6 = 2_000_000
prize_for_5 = 7_460.10
prize_for_4 = 255.60
prize_for_3 = 24


if len(hits) == 6:
    print("OGROMNE GRATULACJE!!!")
    print('Padła szczęśliwa "SZÓSTKA" w LOTTO! Jesteś bogatszy/a o gwarantowane '
          + "{:,d}".format(prize_for_6).replace(",", " ") + " zł!"), sleep(3)
    if rollover > 0:
        print("Nagroda gwarantowana zostanie powiększona o rozbicie kumulacji. \n"), sleep(2)

elif len(hits) == 5:
    print("Gratulacje!!!")
    print('Padła "PIĄTKA" w LOTTO! Udało Ci się trafić w ' + str(hits) + "!"), sleep(3)
    print("W tym losowaniu dostajesz " + str(prize_for_5) + " zł!")
    if rollover > 0:
        print("Nagroda zostanie powiększona o rozbicie kumulacji. \n"), sleep(2)

elif len(hits) == 4:
    print("Gratulacje!!!")
    print('Padła "CZWÓRKA" w LOTTO! Udało Ci się trafić w ' + str(hits) + "!"), sleep(3)
    print("W tym losowaniu dostajesz " + str(prize_for_4) + " zł!")
    if rollover > 0:
        print("Nagroda zostanie powiększona o rozbicie kumulacji. \n"), sleep(2)

elif len(hits) == 3:
    print("Gratulacje!!!")
    print('Padła "TRÓJKA" w LOTTO! Udało Ci się trafić w ' + str(hits) + "!")
    print("Wędruje do Ciebie gwarantowane " + str(prize_for_3) + " zł! \n"), sleep(2)

else:
    if len(hits) == 2:
        print("Udało Ci się trafić w " + str(len(hits)) + " liczby: " + str(hits) + ".")
    elif len(hits) == 1:
        print("Udało Ci się trafić w " + str(len(hits)) + " liczbę: " + str(hits) + ".")
    else:
        print("Tym razem nie udało Ci się trafić w żadną liczbę.")

print("Spróbuj ponownie swojego szczęścia.")