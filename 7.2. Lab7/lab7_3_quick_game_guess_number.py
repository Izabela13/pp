"""
3. Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
3 szanse. Po nieudanej próbie gracz powinien otrzymać podpowiedź np.
o parzystości zgadywanej liczby itp..
"""

# Program będzie wprowadzał uśpienia do lepszej kompozycji komunikatów
from time import sleep

print("Zagrajmy w grę w zgadywanie liczb z przedziału od 1 do 10."), sleep(3),
print("Przed Tobą aż 3 szanse na odgadnięcie wylosowanej przeze mnie liczby."), sleep(3),
print("Gotów?"), sleep(2),
print("No to zaczynajmy! :) \n"), sleep(2)


import random
number = random.randint(1, 10)


# PIERWSZA SZANSA NA ODGADNIĘCIE WYLOSOWANEJ LICZBY
# Blok kodu dla pierwszej próby odgadnięcia wylosowanej liczby.
guess = int(input("Zgadnij, jaką liczbę wylosowałem: "))

# Jeśli gracz odgadł liczbę za pierwszym razem, to gra się kończy.
if guess == number:
    print("DOKŁADNIE TAK! JESTEŚ MISTRZEM! ZASŁUGUJESZ NA ZŁOTO! :D \n"), sleep(2)
# Zakończenie gry, jeśli ktoś podaje liczbę spoza zakresu 1-10. Gracz nic nie traci na początkowym etapie gry.
elif guess < 1 or guess > 10:
    print("Zwróć uwagę na zakres. Przypominam - zakres od 1 do 10. \n"), sleep(2)
# PODPOWIEDŹ I - OKREŚLENIE, CZY LICZBA JEST PARZYSTA CZY NIEPARZYSTA
else:
    print("Nie, chodzi o inną liczbę, ale żeby nie było tak trudno, to podam Ci pierwszą podpowiedź:"), sleep(2)
    if number % 2 == 0:
        print("Liczba, którą wylosowałem jest parzysta. \n"), sleep(2)
    else:
        print("Liczba, którą wylosowałem jest nieparzysta. \n"), sleep(2)

#######################################################################################################################

# DRUGA (I TRZECIA) SZANSA NA ODGADNIĘCIE WYLOSOWANEJ LICZBY
    guess_2 = int(input("Podaj drugą opcję: "))

    # a) blok kodu, który aktywuje się, jeśli gracz wprowadzi po raz drugi tę samą liczbę
    if guess_2 == guess:
        print("Podajesz drugi raz tę samą liczbę! Czy to przypadek?"), sleep(2)
        if number % 2 == 0 and guess_2 == guess and guess_2 % 2 != 0: # Jeśli powtórnie wprowadzona liczba nie będzie parzysta (a wylosowana jest parzysta), program upomni gracza.
            print("Poza tym wprowadzasz liczbę nieparzystą, a wylosowana przeze mnie liczba jest PARZYSTA!"), sleep(3)
        elif number % 2 != 0 and guess_2 == guess and guess_2 % 2 == 0: # Jeśli powtórnie wprowadzona liczba będzie parzysta (a wylosowana jest nieparzysta), program upomni gracza.
            print("Poza tym wprowadzasz liczbę parzystą, a wylosowana przeze mnie liczba jest NIEPARZYSTA!"), sleep(3)

        # Jeżeli gracz wprowadził po raz drugi tę samą liczbę, będzie miał jedną możliwość skorygowania się.
        print("Mam nadzieję, że to tylko omsknięcie. Daję Ci jeszcze raz drugą szansę. \n"), sleep(2)
        guess_2_b = int(input("Podaj jeszcze raz drugą opcję: "))

        # Jeżeli gracz z uporem maniaka będzie wpisywał tę samą liczbę, zakończy grę.
        if guess_2_b == guess_2 and guess_2 == guess:
            print("Wprowadzasz po raz trzeci tę samą liczbę! To chyba jednak nie jest przypadek! :( \n"), sleep(3)
            print("Myślę, że na tym możemy zakończyć!"), sleep(2)
            print("Chodziło mi o " + str(number) + "!"), sleep(2)
            print("Następnym razem nie podawaj tej samej liczby 3 razy pod rząd...  \n"), sleep(2)

        # Jeśli gracz wprowadzi liczbę spoza zakresu 1-10, automatycznie zakończy grę.
        elif guess_2_b < 1 or guess_2_b > 10:
            print("Wprowadzasz liczbę spoza wspomnianego zakresu 1-10!"), sleep(3)
            print("Myślę, że na tym możemy zakończyć to podejście."), sleep(2)
            print("Chodziło mi o " + str(number) + "!"), sleep(2)
            print("Następnym razem pamiętaj, że chodzi o zakres od 1 do 10. \n"), sleep(2)

        # Jeśli gracz wpisał poprzednio tę samą liczbę, ale się poprawił, nadal może odgadnąć wylosowaną liczbę.
        elif guess_2_b == number:
            print("TAK! Dobrze, że strategia wprowadzania tych samych liczb pod rząd została zmieniona!"), sleep(3)
            print("Powiedzmy, że udało Ci się odgadnąć wylosowaną przeze mnie liczbę za drugim razem. :) \n"), sleep(3)

        # Jeśli gracz się poprawił i nie wprowadził po raz trzeci tej samej odpowiedzi, ale nadal nie odgadł liczby, dostanie drugą podpowiedź.
        elif guess_2_b != guess and guess_2_b != number:
            print("Nadal to nie ta liczba. Ale żeby Ci ułatwić odgadywanie, to podam Ci drugą podpowiedź:"), sleep(2)
            if number >= 1 and number <= 5:
                print("Wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5. \n"), sleep(2)
            else:  # nie ma innych możliwości niż przedział [6-10]
                print("Wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10. \n"), sleep(2)

            # Trzecia szansa dla gracza, który wprowadził dwa razy z rzędu tę samą liczbę.
            # Jeśli gracz wróci do poprzednich wyborów, zostanie upomniany i zakończy grę.

            # Gdy gracz wraca do pierwszej podanej przez siebie opcji:
            guess_3 = int(input("Podaj trzecią opcję: "))
            if guess_3 == guess:
                print("Dlaczego wracamy do początkowej liczby? Przecież już wtedy powiedziałem Ci, że to nie ta! :( "), sleep(2)
                if (number >= 1 and number <= 5) and guess_3 > 5:
                    print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5, a podana przez Ciebie liczba występuje w przedziale między 6 a 10."), sleep(3)
                elif number > 6 and (guess_3 >= 1 and guess_3 <= 5):
                    print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10, a podana przez Ciebie liczba występuje w przedziale między 1 a 5."), sleep(3)
                print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
                print("Wylosowana liczba to " + str(number) + ". \n"), sleep(2)

            # Gdy gracz wraca do drugiej podanej przez siebie opcji:
            elif guess_3 == guess_2 or guess_3 == guess_2_b:
                print("Dlaczego wracamy do poprzedniej liczby? Przecież już wtedy powiedziałem Ci, że to nie ta! :( "), sleep(2)
                if (number >= 1 and number <= 5) and guess_3 > 5:
                    print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5, a podana przez Ciebie liczba występuje w przedziale między 6 a 10."), sleep(3)
                elif number > 6 and (guess_3 >= 1 and guess_3 <= 5):
                    print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10, a podana przez Ciebie liczba występuje w przedziale między 1 a 5."), sleep(3)
                print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
                print("Wylosowana liczba to " + str(number) + ". \n"), sleep(2)

            # Gdy gracz wprowadzi liczbę spoza zakresu 1-10:
            elif guess_3 < 1 or guess_3 > 10:
                print("Wprowadzona liczba nie należy do zakresu 1-10!"), sleep(2)
                print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
                print("Wylosowana liczba to " + str(number) + ". \n"), sleep(2)

            # Gdy gracz mimo wszystko nie zgadnie liczby:
            elif guess_3 != number and guess_3 != guess_2 and guess_3 != guess_2_b and 0 < guess_3 < 11:
                print("Przykro mi :( , niestety nie tym razem. :( "), sleep(2)
                print("Wylosowana przeze mnie liczba to " + str(number) + ". \n"), sleep(2)

    # b) Komunikat, gdy gracz odgadł liczbę za drugim razem (i nie wprowadzał tej samej liczby dwa razy z rzędu);
    elif guess_2 == number:
        print("TAK! Gratulacje, udało Ci się odgadnąć za drugim razem! SREBRO WĘDRUJE DO CIEBIE! :D \n"), sleep(2)


# PODPOWIEDŹ II - OKREŚLENIE, W JAKIM PRZEDZIALE MIEŚCI SIĘ WYLOSOWANA LICZBA: [1, 5] CZY [6, 10]
    else:
        if guess_2 < 1 or guess_2 > 10: # Gdy gracz przekracza zakres 1-10, zostanie upomniany.
            print("Zwróć uwagę na zakres! Pamiętaj, podawaj liczby od 1 do 10."), sleep(2)

        print("Nadal to nie ta liczba."), sleep(2)
        if number % 2 == 0 and guess_2 % 2 != 0:
            print("Poza tym podana przez Ciebie liczba była nieparzysta, a wylosowana przeze mnie liczba jest PARZYSTA!"), sleep(3)
        if number % 2 != 0 and guess_2 % 2 == 0:
            print("Poza tym podana przez Ciebie liczba była parzysta, a wylosowana przeze mnie liczba jest NIEPARZYSTA!"), sleep(3)
        print("Ale żeby jeszcze bardziej ułatwić Ci odgadywanie, to podam drugą podpowiedź:"), sleep(2)

        if number >= 1 and number <= 5:
            print("Wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5. \n"), sleep(2)
        else: # nie ma innych możliwości niż przedział [6-10]
            print("Wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10. \n"), sleep(2)

#######################################################################################################################

# TRZECIA SZANSA NA ODGADNIĘCIE WYLOSOWANEJ LICZBY, GDY OSOBA NIE PODAŁA ZA DRUGIM RAZEM TEJ SAMEJ LICZBY
        guess_3 = int(input("Podaj trzecią opcję: "))

        # a) opcja, gdy gracz przekracza zakres 1-10
        if guess_3 < 1 or guess_3 > 10 and guess_3 != guess and guess_3 != guess_2:
            print("Przekraczasz zakres liczb! Już to było mówione - zakres od 1 do 10!"), sleep(2)
            print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
            print("Wylosowana liczba to " + str(number) + "."), sleep(2)
            print("Następnym razem zwracaj uwagę na zakres liczb, jaki masz do wyboru. \n"), sleep(2)

        # b) opcja, gdy gracz wraca do liczby, którą podał poprzednio
        if guess_3 == guess:
            print("Dlaczego wracamy do początkowej liczby? Przecież już wtedy powiedziałem Ci, że to nie ta! :( "), sleep(2)
            if (number >= 1 and number <= 5) and guess_3 > 5:
                print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5, a podana przez Ciebie liczba występuje w przedziale między 6 a 10."), sleep(3)
            elif number > 6 and (guess_3 >= 1 and guess_3 <= 5):
                print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10, a podana przez Ciebie liczba występuje w przedziale między 1 a 5."), sleep(3)
            print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
            print("Wylosowana liczba to " + str(number) + ". \n"), sleep(2)

        elif guess_3 == guess_2:
            print("Dlaczego wracamy do poprzedniej liczby? Przecież już wtedy powiedziałem Ci, że to nie ta! :( "), sleep(2)
            if (number >= 1 and number <= 5) and guess_3 > 5:
                print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 1 a 5, a podana przez Ciebie liczba występuje w przedziale między 6 a 10."), sleep(3)
            elif number > 6 and (guess_3 >= 1 and guess_3 <= 5):
                print("Poza tym wylosowana przeze mnie liczba znajduje się w przedziale między 6 a 10, a podana przez Ciebie liczba występuje w przedziale między 1 a 5."), sleep(3)
            print("Niestety, ale to była ostatnia szansa na odgadnięcie. :( "), sleep(2)
            print("Wylosowana liczba to " + str(number) + ". \n"), sleep(2)

        # c) blok kodu przy zgadywaniu po raz trzeci, gdy gracz nie wprowadza wcześniej podanych liczb
        if guess_3 == number:
            print("Tak! A jednak, do trzech razy sztuka! BRĄZ DLA CIEBIE! :) \n"), sleep(2)
        elif guess_3 != guess_2 and guess_3 != guess and 0 < guess_3 < 11:
            print("Przykro mi :( , niestety nie tym razem. :( "), sleep(2)
            print("Wylosowana przeze mnie liczba to " + str(number) + ". \n"), sleep(2)


print("To może jeszcze raz? ;)")