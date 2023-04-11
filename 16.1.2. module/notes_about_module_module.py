"""
Tworzenie własnych modułów.

Moduły mają standardowe rozszerzenie .py. Są to standardowe skrypty Pythona.

Na początku tworzenia modułu wstawia się zwykle wielolinijkowy string.
"""

#######################################################################################################################
"""
This is my first own module
"""

# Nasz moduł będzie miał zestaw jakichś funkcjonalności

# Funkcja sprawdzająca, czy coś jest napisem czy nie jest napisem
def is_string(val):  # funkcja będzie przyjmowała jakąś wartość i będzie zwracała jakiegoś Boolena (wartość logiczną).
    """ Simple string value validator """  # Opis tego, co będzie robić funkcja.
    return isinstance(val, str)  # funkcja ininstance bierze wartość i sprawdza, czy jest to obiekt klasy string.


# Sumator elementów listy
def sum_list_element(list): # jako parametr funkcja będzie przyjmować listę
    sum = 0

    for i in list:
        sum += i
    return sum


# Każdy, kto zaciągnie ten moduł będzie mógł korzystać z wprowadzonych przez nas funkcji


print(__name__) # __main__ (wywołanie modułu samodzielnie)
# Funkcja __name__ w obecnym wywołaniu pokazuje __main__, czyli wskazuje na wywołanie modułu przez nas samych.


# Ten fragment zostanie wykonany tylko w momencie, kiedy my sami będziemy wywoływać moduł
if __name__ == "__main__":  # pisanie oprogramowania do momentu, w którym wszystkie testy nie zostaną spełnione
    print(is_string("haha") == True)
    print(is_string(123) == False)
    print(sum_list_element([1, 1, 1]) == 3)
    print(sum_list_element([]) == 0)

"""
W każdej linijce korzystamy z wyżej zaimplementowanych funkcji i spodziewamy się otrzymać rezultat według logiki, 
na której funkcje zostały zbudowane. 
Jeżeli funkcje są dobrze napisane, to w powyższych printach wszędzie powinno pojawić się "True".

__main__
True
True
True
True

Pisanie modułu można zacząć od pisania zestawu testów i kodować funkcje do momentu, w którym nie pojawią się 
same wartości "True". Jest to jedna z technik programowania - programowanie sterowane testami. 
Na początku zapisujemy zestaw testów w dużym uproszczeniu. Najczęściej są to testy jednostkowe, które sprawdzają 
małą porcę kodu. Oprogramowanie jest pisane do momentu, dopóki wszystkie założenia testów nie zostaną spełnione.  

Przez to, że testy rozpoczynają się od warunku "if _name__ == "__main__", to ten fragment kodu zostanie wykonany tylko 
i wyłącznie, gdy twórca - w tym wypadku my - będzie wywoływał ten moduł z pozycji tego modułu. 

Kiedy twórca lub ktoś inny będzie importował ten moduł, fragment kodu, gdzie pojawiają się testy, zostanie pominięty.
"""

"""
Moduł można użyć. W naszym wypadku użyjemy go w skrypcie "main.py". Nazwa jest nieprzypadkowa. 
"""