# # FUNKCJE - SPOSOBY WYKORZYSANIA


# # FUNKCJE I LISTY - WSPÓŁDZIAŁANIE
# # Zdefiniowanie funkcji, która będzie zliczać sumę elementów z naszej listy

# def sum_numbers(numbers): # ta funkcja będzie sparametryzowana. Będziemy do niej podawać listę liczb
#     sum = 0 # zmienna lokalna (niewidoczna poza funkcją)
#     for element in numbers: # zmienna pomocnicza "element", pod którą będą podstawiane kolejne elementy listy
#         sum += element # dodaj element do zmiennej "sum"
#     return sum # zwróć sumę

# sum_numbers([1, 2, 3]) # nie ma tutaj nigdzie funkcji print(), dlatego nic się nie pojawi w konsoli

# # Funkcja została zdefiniowana, została uruchomiona, wykonała jakieś zadanie, ale wynik się nie pojawił.
# # Wynik miał zostać tylko zwrócony, ale nie wydrukowany. Słowo kluczowe "return" zwraca wartość funkcji, ale
# # nie powoduje wyświetlenia wartości na konsoli.

# # Jeżeli chcemy zobaczyć, co zwraca funkcja, trzeba jawnie wstawić print()
# print(sum_numbers([1, 2, 3])) # 6 - dopiero po wyprintowaniu tego, co przekazuje funkcja widać wartość.


# # Można zdekomponować proces na poszczególne elementy.
# numbers = [1, 2, 3]  # 1. można utworzyć na początku zmienną, do której przypiszemy listę
# result = sum_numbers(numbers)  # 2. Do zmiennej "result" przypisana jest operacja "sum_numbers".
# # Podstawienie do funkcji zmiennej "numbers", która jest referencją do listy.
# print(result) # 3. wyświetlenie wyniku

"""
Interpreter nie wie, co to jest parametr "numbers". Interpreter próbuje podstawiać do funkcji dowolną wartość.
Co się stanie, gdy podstawimy wartość skalarną?
Zagrożenie pojawi się w pętli for, ponieważ nie można iterować po wartości skalarnej, np.:

sum_numbers(99) --> pod zmienną "numbers" podstawiam liczbę - pojawi się wyjątek - Type Error - obiekt int nie jest iterowalny.

Program próbował iterować po liczbie 99. Pojedyncza liczba nie jest ani ciągiem znaków ani nie jest to element sekwencyjny.
Żeby się zabezpieczyć należałoby wprowadzić jakiś element walidacyjny lub obsługę wyjątków. 
"""



# # DEFINIOWANIE FUNKCJI GENERUJĄCEJ LISTĘ Z LOSOWYMI LICZBAMI Z ZAKRESU OD 1 DO 99.
# # Jako parametr funkcji będziemy podawać, ile chcemy mieć wylosowanych liczb, a funkcja będzie zwracała zestaw.
# # PRZEJŚCIE DO PLIKU number_generator



# # ZASIĘG ZMIENNYCH (NAME SCOPE)

# def scope_test(): # funkcja będzie miała jedną zmienną lokalną
#     x = 123 # funkcja będzie wykonywała tylko tworzenie zmiennej lokalnej i przypisywanie wartości
# # Na razie nic się nie wyświetla.

# scope_test() # Nic się nie wyświetla, bo nie miało się wyświetlić.

# # Próba odwołania się do zmiennej lokalnej "x". Jest to nie możliwe.
# # print(x) # od razu pojawia się błąd - nierozwiązywalna referencja x; wartość x nie jest zdefiniowana
# # Interpreter nie wie, co to jest zmienna "x", ponieważ nigdzie nie została zdefiniowana.

# # Zmienna lokalna ma tylko zasięg funkcji. Poza funkcją zmienna "x" jest nieznana.


# # I KOMBINACJA. Zmienna "x" zdefiniowana poza ciałem funkcji

# def scope_test():
#     print("w środku funkcji: " + str(x))

# x = 99  # do zmiennej "x" zostaje przypisana wartość 99.
# scope_test()  # w środku funkcji: 99
# # Zmienna globalna "x" jest widoczna w ciele funkcji.


# # II KOMBINACJA. Zmienna "x" zdefiniowana poza ciałem funkcji. Nadpisywanie zmiennej "x".
# # Nic nie stoi na przeszkodzie, żeby nazwa zmiennej lokalnej pokrywała się z nazwą zmiennej globalnej.

# def scope_test():  # W ciele funkcji od momentu, kiedy zdefiniowaliśmy zmienną lokalną "x", będzie obowiązywać ta zmienna wewnętrzna.
#     x = 123  # napisanie chwilowe (przysłonięcie) w ciele funkcji zmiennej "x"
#     print("w środku funkcji: " + str(x))

# x = 99
# scope_test() # w środku funkcji: 123
# print("na zewnątrz: " + str(x)) # na zewnątrz: 99

"""
Przypisanie wartości do lokalnej zmiennej "x" nie wpływa w żaden sposób na zdefiniowaną globalnie wartość zmiennej "x".
Nazwy zmiennych nie przeszkadzają sobie, ponieważ są oddzielone odpowiednimy zasięgami (lokalny/ globalny).
Nazwa zmiennej lokalnej przestaje istnieć poza funkcją. Zmienna globalna "x" nadal posiada wartość 99. 
Żadna zmienna nie nadpisuje innej zmiennej.
"""


# # III KOMBINACJA. Wpływanie na zmienną globalną i dokonywanie zmiany.
# # Możemy mieć potrzebę wpłynięcia na zmienną globalną i zmienić ją za pomocą funkcji.
# # Po uruchomieniu funkcji "scope_test" zmienna globalna "x" (99) ma przyjąć wartość ustawioną w funkcji (123).

# def scope_test():
#     global x  # "Od tego momentu traktuj zmienną "x" jako zmienną globalną.
#     x = 123   # To, co stało się w środku funkcji będzie teraz miało wpływ na zmienną globalną.
#     print("w środku funkcji " + str(x))  # zmienna globalna została nadpisana.

# x = 99
# scope_test()  # w środku funkcji: 123
# print("na zewnątrz: " + str(x))  # na zewnątrz: 123

"""
Nastąpiło nadpisanie zmiennej "x". To, co się stąło w środku funkcji (lokalnie), miało wpływ na to, co było na zewnątrz
(na zmienną globalną "x").

Wynik:
w środku funkcji: 123
na zewnątrz: 123
"""



# # PRZEKAZYWANIE ARGUMENTÓW DO FUNKCJI

# # I. Przekazywanie wartości skalarnej.
# # Definiowanie funkcji, której zadaniem będzie zmiana wartości

# def change_value(n): # do tej funkcji będziemy przekazywać argumenty
#     print("przed zmianą: ", n) # informacja pomocnicza - ile ma "n" przed zmianą
#     n += 1  # podniesienie wartości "n" o 1.
#     print("po zmianie: ", n) # informacja pomocnicza - ile ma "n" po zmianie

# # Funkcja będzie modyfikowała wartość "n"
# val = 7 # do zmiennej "val" przypisujemy wartość int równą 7. Int jest wartością niezmienną (niemutowalną).
# change_value(val) #czy wywołanie tej funkcji wpływnie na to, że wartość zminnej val = 7 ulegnie zmianie? NIE
# print(val) # sprawdzanie wpływu na globalną zmienną "val".
"""
ANALIZA: 

Mamy zmienną "val", do której przypisujemy wartość int 7 (wartość całkowita). Uruchamiamy i przekazujemy wartość val = 7
za pomocą nazwy "val" do funkcji "change_value". Program przeskakuje do funkcji. Zmienna "n" w funkcji "change_value" = 7.
Następuje podstawienie wartości ze zmiennej "val" do zmiennej "n". 

Int to wartość niezmienna (niemutowalna), więc podczas podstawienia wartości 7 do zmiennej "n" w funkcji "change_value"
utworzy się kopia wartości zmiennej "val". 
1. print("przed zmienną:", n) --> Kopia wartości "7" zostanie wyświetlona. 
2. n += 1                     --> Pod wartość 7 zostanie wprowadzona wartość 7 + 1.
3. print("po zmianie:", n)    --> Wyświetli się wartość 8.
Funkcja cały czas pracuje na kopii. Na koniec "n" znika z pamięci. Program wraca do miejsca, w którym przerwał.
Wyświetlenie tego, co jest w zmiennej "val" będzie cały czas taka sama, czyli 7. 

Wyniki:
przed zmianą: 7
po zmianie: 8
7
"""


# # II. Przekazywanie listy - wartość nieskalarna

# I. PRZYKŁAD - wartość listy nie ulega zmianie
# def change_value(n): # "n" będzie listą. n = val - do listy możemy odwołać się przez nazwę n i val. Jest 1 lista i 2 nazwy
#     print("przed zmianą: ", n)
#     n = [0, 0] # dla tej referencji podstawiamy całkiem nową listę. Ona będzie w innym miejscu - mamy 2 listy i 2 nazwy
#     print("po zmianie: ", n) # [0, 0]

# # Funkcja będzie modyfikowała wartość n
# val = [1, 2] # nazwa, która przechowuje odwołanie --> przekazanie do funkcji change value
# change_value(val) # pod n podstawiana jest referencja
# print(val)
"""
ANALIZA: 

Mamy zmienną "val", która przechowuje odwołanie/ referencję do listy zapisanej gdzieś w pamięci. Zmienna "val" zostaje
przekazana do funkcji "change_value". Funkcja "change_value" zostaje wywołana z argumentem odwołującym się do listy. 

Program przeskakuje do funkcji. Pod "n" podstawiana jest referencja, czyli "n" = "val". Ile jest list w pamięci? 1. 
A ile jest referncji/ nazw, które odwołują się do tej listy? 2 - do listy można odwołać się przez zmienną "val" i "n". 
Odwołanie zachodzi nadal do tej samej listy. 
1. print("przed zmienną:", n) --> zostanie wyświetlone [1, 2]. 
2. n = [0, 0]                 --> Dla referencji "n" podstawiamy jakąś całkiem nową listę (będzie ona w pamięci komputera).
Mamy teraz 2 listy i 2 nazwy. Każda nazwa wskazuje teraz na inną listę: "val" = [1, 2] a "n" = [0, 0].
3. print("po zmianie:", n)    --> Wyświetli się wartość [0, 0].

print(val) pokaże [1, 2], ponieważ nie zmieniliśmy nic w liście, na którą wskazywąło "n". Pod "n" podstawiono całkiem
nowy obiekt za pomocą przypisania. Od danego momentu w funkcji zmienna "n" staje się czymś innym niż zmienna "val".
Zmienna "n" może być czymś zupełnie innym niż listą, np. liczbą, napisem. 

Wyniki:
przed zmianą:  [1, 2]
po zmianie:  [0, 0]
[1, 2]
"""


# # II PRZYKŁAD - zmiana wartości listy za pomocą funkcji
# # Zmiana dla listy o nazwie "n" o indeksie 0 i podstawianie 999

# def change_value(n): # n = val - od tego momentu mamy dwie zmienne - lokalną i globalną
#     print("przed zmianą: ", n)
#     n[0] = 999 # dla tej referencji, do której mamy odwołanie - zmień to samo miejsce w liście na 999.
#     print("po zmianie: ", n)

# # Funkcja będzie modyfikowała wartość n
# val = [1, 2] # nazwa, która przechowuje odwołanie --> przekazanie do funkcji "change_value"
# change_value(val) # pod nazwą "n" podstawiana jest referencja
# print(val)
"""
ANALIZA: 

Mamy listę "val" = [1, 2]. Zmieniamy ją przez wywołanie funkcji "change_value". Podstawiamy nazwę "val" odwołującą się
do jakiejś listy, która jest w pamięci, do funkcji "change_value". Przeskakujemy do poczatku funkcji. 

W funkcji pod "n" wykonywana jest operacja przypisania "n" = "val". Od tego momentu mamy dwie zmienne - jedną lokalną, 
drugą globalną, które odwołują się do jednej listy w pamięci (do listy [1, 2]).
1. print("przed zmienną:", n) --> zostanie wyświetlone [1, 2]. 
2. n[0] = 999                 --> Polecenie "zmień element o indeksie 0 dla referencji (listy), do której mamy odwołanie
pod 'n' - zmień to samo miejsce w liście na 999. Dokona się taka zmiana: [1, 2] --> [999, 2].
3. print("po zmianie:", n)    --> Wyświetli się wartość [999, 2]. Zmieniona została ta sama lista, na którą wskazuje też
wartość "val". 

Wyniki: 
przed zmianą:  [1, 2]
po zmianie:  [999, 2]
[999, 2]
"""



# PRZEJŚCIE DO PLIKU fibonacci i później do fibonacci_rec



# # WYPRZEDZENIE TEMATU KROTEK (TUPLI) I SŁOWNIKÓW
# # Jak to jest zrobione, że do funkcji print można podać dowolną ilość argumentów

# # Przekazywanie do funkcji zestawu argumentów, przy czym nie chcemy definiować, ile tych argumentów jest.
# def my_func(*args): # użycie notacji z gwiazdka, gdy nie chcemy określać, ile podamy argumentów (krotka).
#     for el in args: # krotka jest elementem sekwencyjnym, można po nim iterować.
#         print(el)

# my_func(1, 2, 3, 4, 5, 6, 7, 8) # teraz można podać dowolną ilość argumentów
# # Załatwienie wieloargumentowości. Sposób przekazywania argumentów pozycyjnie.


# # Sposób przekazywania argumentów za pomocą słów kluczowych - słowniki
# def my_func(**args): # Dwie gwiazdki przy "args", gdy nie chcemy określać, ile podamy argumentów
#     for el in args.items(): # zapis danych do słownika - iteracja zachodzi po ITEMACH (metoda items)
#         print(el)

# my_func(val1 = "raz", val2 = 999)
"""
Wyniki:
Funkcja zwróci szereg krotek - klucz i wartość jako krotki w nawiasach okrągłych.
('val1', 'raz')
('val2', 999)
"""