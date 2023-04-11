# MODUŁ DO OBSŁUGI GRY W LOTTO

from random import sample

# MECHANIZM I służący do wylosowania 6-ciu liczb
# Funkcja losująca 6 liczb z 49
def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort() # liczby będą od razu sortowane
    return lucky_numbers # zwracane będą już posortowane liczby


# MECHANIZM II służący do pobrania od użytkownika zestawu jego liczb.
# Mechanizm do skreślania liczb przez użytkownika
def get_user_numbers():  # "Pobierz liczby od użytkownika"
    n = 6                # Definiowanie, ile liczb będziemy pobierać od użytkownika. Zapisujemy je do zmiennej "n".
    counter = 1          # Zmienna "counter" będzie zliczać, ile liczb zostało pobranych poprawnie.
    user_numbers = []    # Pobrane liczby będą zapisywane do listy "user_numbers".

    while counter < n + 1:  # Pętla będzie działa do momentu, dopóki "counter" będzie mniejszy od n + 1
        try:  # Wprowadzenie obsługi błędów
            number = int(input("Podaj " + str(counter) + " liczbę (1-49): "))  # od tego momentu tworzonie zabezpieczeń
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue  # za pomocą instrukcji "continue" przechodzimy do początku pętli. Nie podnosimy "countera"
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziału od 1 do 49!")
                continue  # za pomocą instrukcji "continue" przechodzimy do początku pętli. Nie podnosimy "countera"
        except:
            print("To nie jest liczba. Proszę podać liczbę całkowitą")
            continue  # za pomocą instrukcji "continue" przechodzimy do początku pętli. Nie podnosimy "countera"

        user_numbers.append(number)
        counter += 1

    user_numbers.sort()  # sortowanie liczby
    return user_numbers  # wyjście poza pętlę - zwrócenie liczb podanych przez użytkownika.


# MECHANIZM III: mechanizm sprawdzający liczby
def check_numbers(user_numbers, lucky_numbers):  # argumenty to dwa zestawy: liczby wprowadzone i liczby wylosowane.
    # jako argumenty musimy przekazać liczby, które podał użytkownik ("user_numbers") oraz
    # liczby, które zostały wylosowane ("lucky_numbers").
    counter = 0  # "counter" będzie zliczał ilość trafionych liczb
    for number in user_numbers:  # funkcja będzie porównywać dwa zestawy liczb
        if number in lucky_numbers:  # sprawdzanie, czy liczba z zestawu użytkownika znajduje się wśród wylosowanych
            counter += 1
    return counter  # zwrócenie liczby trafionych numerów


"""
Testowanie
Jeżeli właściwość __name__ jest ustawiona na __main__, to przekłada się na to, że jeżeli to my będziemy wywoływać
ten skrypt (moduł), to pozwoli to sprawdzić poszczególne funkcje.
"""
if __name__ == "__main__": # Jeżeli my będziemy wywoływać moduł
    user_numbers = get_user_numbers()  # pobieranie tego, co zwróci funkcja
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)