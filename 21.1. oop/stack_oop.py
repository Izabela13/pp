# # OBJECT ORIENTED PROGRAMMING - PROGRAMOWANIE ZORIENTOWANE OBIEKTOWO


######################################################################################################################


# # Napisanie klasy - definiujemy klasę stosu
"""
__init__ to specjalna metoda, która ma specjalną funkcję. Jest to tak zwany konstruktor.
KONSTRUKTOR to metoda, która będzie służyła do inicjalizacji obiektów, które będą tworzone za pomocą klasy.

    __init__(self) --> Inicjalizacja obiektów tej samej klasy
        print("Cześć!")

Jeżeli w metodzie __init__*=(self) zapiszemy wywołanie komendy "Cześć!", to przy tworzeniu obiektu w klasie
zostanie wywołany napis "Cześć!". Jeżeli mamy zdefiniowaną metodę konstruktora i mamy zdefiniowany konstruktor,
to ten konstruktor wykona się.

Jeżeli przy konstruktorze nie byłoby printa:
    __init__(self)
        # print("Cześć!")
        pass
to nic się nie wyświetli.

Jeżeli metoda zostałaby zmieniona na jakąś inną, np.
    __bla_bla_init__(self)
        # print("Cześć!")
        pass
to również nic się nie wyświetli.

Rozpoczęcie tworzenia konstruktora __init__ automatycznie uzupełni (self)
"""


class Stack:  # notacja Upper Camel Case (zalecana). Definiujemy KLASĘ STOSU
    # METODY (ZACHOWANIA) dla klasy tworzymy podobnie jak funkcje za pomocą deklaracji
    def __init__(self): # deklaracja ze słowem kluczowym "def". DEFINIOWANIE KONSTRUKTORA
        print("Cześć!") # definiowanie konstruktora


obj = Stack()  # Nawiasy odnoszą się do wywołania funkcji __init__(self)
# Po stworzeniu tego obiektu dostajemy "Cześć!". Zdefiniowany konstruktor __init__(self) wywołał się.

print()


######################################################################################################################


# Wykorzystamy konstruktor do tego, żeby zrobić pewien zabieg:
class Stack:
    def __init__(self):
        self.stack_list = []  # UŻYCIE WŁAŚCIWOŚCI "self" (specjalny element). Dla tej właściwości powstanie lista

obj = Stack()  # Tworzenie obiektu
print(len(obj.stack_list))  # 0 (zwróciło się 0, bo "stack_list" na razie pusta lista

print()


######################################################################################################################


"""
Jeżeli właściwość zapiszemy z nazwą, która ma dwa podkreślniki, to ta właściwość będzie traktowana jako właściwość prywatna.
"Właściwość prywatna" oznacza, że nie będzie ona dawana użytkownikowi. Ta właściwość będzie mogła być wykorzystywana 
przez klasę. 

Fachowo nazywa się to ENKAPSULACJA lub HERMETYZACJA - zabezpieczenie przed przypadkową modyfikacją
W przykładzie nie chcemy bezpośrednio modyfikować stosu.
Dla programistów z zewnątrz dostęp do listy "__stack_list" będzie ograniczony. 
Tylko klasa będzie mogła manipulować właściwością listy "__stack_list".

Klasa najczęściej modyfikowana jest w oddzielnym pliku i w oddzielnym module.
"""


class Stack:
    def __init__(self):
        self.__stack_list = []  #  __stack_list --> dodajemy właściwość prywatną


# -------------------------------------------------------------------------------

# obj = Stack()
# print(len(obj.__stack_list))  # Próba wyświetlenia właściwości "__stack_list" zakończy się błędem
""" 
Wyjątek AttributeError - zabezpieczenie przed wykonaniem
    AttributeError: 'Stack' object has no attribute '__stack_list'

Jest to zabezpieczenie przed tym, aby nie móc modyfikować 
"""

obj = Stack()
obj.__stack_list = [4, 4, 4]  # dodanie nowej właściwości, która jest dodatkowo widoczna
print(len(obj.__stack_list))  # 3

print()


#######################################################################################################################


# Dodawanie nowej właściwości
class Stack:
    def __init__(self):  # ZDEFINIOWANA WŁAŚCIWOŚĆ
        self.__stack_list = []  # pusta lista

    def push(self, val):  # METODA I
        self.__stack_list.append(val)  # Z wnętrza klasy można odwołać się bezpośrednio do właściwości

    def pop(self):  # METODA II
        val = self.__stack_list[-1]  # zmienna lokalna będzie lokalna dla metody.
        del self.__stack_list[-1]
        return val


# obj = Stack()
# obj2 = Stack()

# obj.push(3)
# obj.push(2)
# obj.push(1)

# Próba wstawienia np. trzech 4-ek spowoduje dodanie nowej właściwości, ale logika pozostanie niezmienna.
# obj.__stack_list = [4, 4, 4]  # dodanie nowej właściwości. Logika pozostaje niezmienna (I zaleta)

# print()

# print(obj.pop())
# print(obj.pop())
# print(obj.pop())

# Dodawanie kolejnych obiektów
obj = Stack()
obj2 = Stack()
obj3 = Stack()

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

obj3.push("Ania")
obj3.push("Zosia")
obj3.push("Tomek")

print()

print(obj.pop())  # 1
print(obj.pop())  # 2
print(obj.pop())  # 3

print()

print(obj2.pop())  # 4
print(obj2.pop())  # 4
print(obj2.pop())  # 4

print()

print(obj3.pop())  # Tomek
print(obj3.pop())  # Zosia
print(obj3.pop())  # Ania

print()

# Ściąganie obiektów z poszczególnych stosów można poprzelatać (dzięki hermetyzacji, enkaspulacja).


#######################################################################################################################


"""
Stos ma mieć możliwość dodatkowo zliczania sumy wszystkich elementów.
Nie będziemy psuć już istniejącej klasy. Możemy dodać nową klasę, która będzie miała właściwość stosu, który ma nowe zachowanie.
"""


class Stack:
    def __init__(self):
        self.__stack_list = [] # pusta lista

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class StackSum(Stack):  # Ta klasa będzie dziedziczyła po wcześniejszej --> w nawiasach okrągłych wpisujemy klasę
    def __init__(self):  # konstruktor - metoda __init__
        Stack.__init__(self) # jawnie wpisać argument self - jawne wywołanie konstruktora nadklasy
        self.__sum = 0  # Ta klasa będzie miała właściwość sumowania.

    def get_sum(self):  # METODA, KTÓRA POBIERA SUMĘ
        return self.__sum  # zmienna "sum" jest prywatna, ale wolno nam się do niej odwołać

    def push(self, val):       # KOREKTA METODY "push"
        self.__sum += val      # sumowanie
        Stack.push(self, val)  # odwołanie się do metody "push z klasy nadrzędnej "Stack".

    def pop(self):             # NADPISANIE METODY "pop"
        val = Stack.pop(self)  # Korzystamy z nadklasy "Stack"
        self.__sum -= val      # Odwołanie się do właściwości "sum" i odjęcie wartości "val"
        return val             # Dzięki temu możemy przechowywać sumę


"""
Przez zasadę dziedziczenia dziedziczy się wszystko to, co zostało zaimplementowane wcześniej oraz nowe możliwości.
W tym przykładzie nową możliwością jest przechowywanie sumy wszystkich elementów.
"""
# ------------------------------------------------------------------------------------------


obj = StackSum()
obj2 = StackSum()

print("Umieszczamy elementy na stosach!")

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

# PRZED ŚCIĄGANIEM ZE STOSU
print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())

print()

print(obj.pop())
print(obj.pop())
print(obj.pop())

print()

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())

print()

# PO ŚCIĄGNIĘCIU ZE STOSU
print("Ściągamy elementy ze stosów!")
print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())


#######################################################################################################################