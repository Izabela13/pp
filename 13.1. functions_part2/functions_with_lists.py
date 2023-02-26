# # Funkcja będzie zliczać sumę elementów z naszej listy
#
# def sum_numbers(numbers): # ta funkcja będzie sparametryzowana. Będziemy do niej podawać listę liczb
#     sum = 0 # zmienna lokalna
#     for element in numbers:
#         sum += element
#     return sum
#
# sum_numbers([1, 2, 3]) # nie ma tutaj nigdzie funkcji print, dlatego nic się nie pojawi w konsoli
# # Funkcja została zdefiniowana, wykonała jakieś zadanie, ale wynik się nie pojawił
#
# print(sum_numbers([1, 2, 3])) # 6 - wygląda, że wszystko się zgadza
#
# # można utworzyć na początku zmienną
# numbers = [1, 2, 3]
# result = sum_numbers(numbers) # numbers jest referencją
# print(result)
#
#
# # Interpreter nie wie, co to jest parametr
# # sum_numbers(99) # pod numbers podstawiam liczbę - pojawi się wyjątek - Type Error - obiekt int nie jest iterowalny
# # program próbował iterować po liczbie 99



# # definiowanie funkcji
# def scope_test():
#     x = 123 # funkcja będzie wykonywała tylko tworzenie zmiennej lokalnej i przypisywanie wartości
# # na razie nic się nie wyświetla.
#
# # scope_test()
# # print(x) # od razu pojawia się błąd - nierozwiązywalna referencja x; wartość x nie jest zdefiniowana
#
# # zmienna lokalna ma tylko zasięg funkcji. Poza funkcją x jest nieznane



# # x definiujemy poza ciałem funkcji
# def scope_test():
#     print("w środku funkcji: " + str(x))
#
# x = 99
# scope_test()



# # x definiujemy poza ciałem funkcji
# def scope_test():
#     x = 123 #napisanie chwilowe (przysłonięcie) w ciele funkcji
#     print("w środku funkcji: " + str(x))
#
# x = 99
# scope_test() #w środku funkcji: 123
# print("na zewnątrz: " + str(x)) # na zewnątrz: 99
#
# # nazwy zmiennych nie przeszkadzają sobie, ponieważ są oddzielone zasięgami (lokalny/ globalny)



# # wpływanie na zmienną globalną i dokonywanie zmiany
# def scope_test():
#     global x
#     x = 123
#     print("w środku funkcji " + str(x))
#
# x = 99
# scope_test()
# print("na zewnątrz: " + str(x))

"""
Nastąpiło nadpisanie zmiennej x

Wynik:
w środku funkcji 123
na zewnątrz: 123
"""



# # Przekazywanie argumentów do funkcji
#
# def change_value(n): # do tej funkcji będziemy przekazywać argumenty
#     print("przed zmianą: ", n)
#     n += 1
#     print("po zmianie: ", n)
#
# # Funkcja będzie modyfikowała wartość n
# val = 7 # int jest wartością niezmienną (niemutowalną)
# change_value(val) #czy wyołanie tej funkcji wpływnie na wartość zminnej val = 7 ?
# print(val)



# # Przekazywanie listy - wartość nieskalarna
#
# def change_value(n): # n = val - do listy możemy odwołać się przez nazwę n i val. Jest jedna lista i dwie nazwy
#     print("przed zmianą: ", n)
#     n = [0, 0] # dla tej referencji podstawiamy całkiem nową listę. Ona będzie w innym miejscu - mamy 2 listy i 2 nazwy
#     print("po zmianie: ", n) # [0, 0]
#
# # Funkcja będzie modyfikowała wartość n
# val = [1, 2] # nazwa, która przechowuje odwołanie --> przekazanie do funkcji change value
# change_value(val) # pod n podstawiana jest referencja
# print(val)
"""
Wyniki:
przed zmianą:  [1, 2]
po zmianie:  [0, 0]
[1, 2]
"""



# # Zmiana dla listy n o indeksie 0 i podstawianie 999
#
# def change_value(n): # n = val - od tego momentu mamy dwie zmienne - lokalną i globalną
#     print("przed zmianą: ", n)
#     n[0] = 999 # dla tej referencji, do której mamy odwołanie - zmień to samo miejsce w liście na 999.
#     print("po zmianie: ", n) #
#
# # Funkcja będzie modyfikowała wartość n
# val = [1, 2] # nazwa, która przechowuje odwołanie --> przekazanie do funkcji change value
# change_value(val) # pod n podstawiana jest referencja
# print(val)
"""
Wyniki: 
przed zmianą:  [1, 2]
po zmianie:  [999, 2]
[999, 2]
"""


# WYPRZEDZENIE TEMATU KROTEK (TUPLI) I SŁOWNIKÓW
# def my_func(*args): # gdy nie chcemy określać, ile podamy argumentów
#     for el in args:
#         print(el)
#
# my_func(1, 2, 3, 4, 5, 6, 7, 8)
# # Ta-dam. Załatwienie wieloargumentowości. Sposób przekazywania argumentów pozycyjnie
# # Sposób przekazywania argumentów za pomocą słów kluczowych - słowniki



def my_func(**args): # gdy nie chcemy określać, ile podamy argumentów
    for el in args.items():
        print(el)

my_func(val1 = "raz", val2 = 999)
"""
Wyniki:
('val1', 'raz')
('val2', 999)
"""