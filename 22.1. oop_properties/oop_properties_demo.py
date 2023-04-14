class MyClass:
    def __init__(self, x=1):  # konstruktor (specjalna metoda __init__)
        self.x = x  # zmienna publiczna x (zmienna instancji), którą weźmiemy z parametru
        # nie ma tutaj kolizji nazw: "x" jest zmienną lokalną, "self.x" jest zmienną instancji

    def sety(self, y):  # przekazanie "self" i "y".
        self.y = y  # zmienne instancji mogą być definiowane poza konstruktorem


# # Ustawianie obiektów klasy "MyClass"
obj1 = MyClass()  # ustwiamy właściwość x = 1 (wartość domyślna)
obj1.x  # można się odwołać do zmiennej publicznej

obj2 = MyClass(4)  # ustwiamy właściwość x = 4 (jawnie podano 4)
obj2.sety(7)  # ustawiamy właściwość y = 7

obj3 = MyClass(3)
obj3.z = 99 # dodajemy nową właściwość i ustawiamy ją na z = 99 (zmienna instancji, dodana później)

# # Za pomocą __dict__ można obejrzeć, co mamy w obiektach.
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
"""
{'x': 1}
{'x': 4, 'y': 7}
{'x': 3, 'z': 99}

Konsekwencje są takie, że jeżeli teraz będziemy się chcieli odwołać do właściwości "y" na obiekcie 3 (a wiemy, że nie ma 
takiej), dostaniemy wyjątek AtributeError
"""
print()

#######################################################################################################################

# # PRYWATNE ZMIENNE INSTANCJI


class MyClass:
    def __init__(self, x=1):
        self.__x = x   # "x" to teraz prywatna zmienna insancji

    def sety(self, y):
        self.__y = y  # "y" to teraz prywatna zmienna instancji


obj1 = MyClass()  # ustwiamy właściwość x = 1 (wartość domyślna)

obj2 = MyClass(4)  # ustwiamy właściwość x = 4
obj2.sety(7)  # ustawiamy właściwość y = 7

obj3 = MyClass(3)
obj3.__z = 99  # dodajemy nową właściwość i ustawiamy ją na z = 99 (zmienna instancji, dodana później)

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
"""
{'_MyClass__x': 1}
{'_MyClass__x': 4, '_MyClass__y': 7}
{'_MyClass__x': 3, 'z': 99}

Dodawanie zmiennej prywatnej powoduje to, że Python wewnętrznie przekształca nazwy zmiennych. Z budowy tych nazw wynika, 
że jeśli zaistnieje taka potrzeba, do zmiennych prywatnych będzie się można odwołać. 

Co do zmiennej "__z" - mimo to, że nastąpiła próba uczynienia z niej zmiennej prywatnej, nic to nie daje. Zmienna "z"
pozostanie zmienną "z". Dodanie pseudoprywatnej zmiennej instancji na obiekcie, który jest już stworzony nie daje żadnych
korzyści, ponieważ nie spowoduje to przeobienia zmiennej na zmienną prywatną.
"""
print()

#######################################################################################################################

# # PRÓBA ODWOŁANIA SIĘ DO PRYWATNEJ ZMIENNEJ

# # Nie ma czegoś takiego, jak próba odwołania się do prywatnej zmiennej
# # print(obj1.__x)  # nie ma nawet takiej nazwy (AttributeError: 'MyClass' object has no attribute '__x')

# # Do prywatnej zmiennej można odwołać się przez "podkreślenie" + "nazwa klasy" + "nazwa zmiennej prywatnej"
print(obj1._MyClass__x)
print(obj3.__z)  # do zmiennej "z" można dostać się bez problemu, ponieważ została ona utworzona w trakcie działania programu.
print()

#######################################################################################################################

# # ZMIENNE KLASY

# # Oprócz zmiennych instancji występują również tak zwane zmienne klasy


class MyClass:
    # zmienna "counter" będzie zliczać wystąpienia wszystkich instancji klasy, czyli wszystkie obiekty i utwożenia
    counter = 0  # zmienna klasy, wspólna dla całej klasy obiektów
    """
    Jeżeli wiemy, że konstruktor wywoływany jest zawsze wtedy, kiedy tworzony jest nowy obiekt, to przy każdym
    wywołaniu konstruktora będziemy zwiększać licznik (zmienną "counter").
    Do konstruktora będzie można odwołać się po NAZWIE KLASY (MyClass). Nie można odwołać się po "self", bo "self" jest
    dla całej klasy. 
    """
    def __init__(self, x = 1):
        self.__x = x
    # Konstruktor wywoływany jest za każdym tworzeniem obiektu
        MyClass.counter += 1  # Zwiększenie przy każdym wywołaniu konstruktora


obj1 = MyClass(1)
print(obj1.__dict__, obj1.counter)
obj2 = MyClass(2)
print(obj2.__dict__, obj2.counter)
obj3 = MyClass(77)
print(obj3.__dict__, obj3.counter)

# MyClass(77)
# MyClass(77)
# MyClass(77)
# MyClass(77)

print("Ile obiektów?", MyClass.counter)
"""
Spodziewamy sie, że licznik wyświetli wartość 3.

{'_MyClass__x': 1} 1
{'_MyClass__x': 2} 2
{'_MyClass__x': 77} 3
Ile obiektów? 3

Jeśli zostanie utworzone jeszcze kilka obiektów, to licznik podniesie się o te obiekty.
Obiekt wie, której jest klasy, ale nie na odwrót. 
Klasa to coś bardzo ogólnego. Jeżeli mamy zmienną klasy, to wszystkie obiekty tej klasy mają dostęp do właściwości klasy.
Jeżeli mamy obiekt, to ma on już "swoje zabawki". 
"""
print()

#######################################################################################################################

# # PRYWATNA ZMIENNA KLASY


class MyClass:

    __counter = 0  # "counter" jest teraz prywatną zmienną klasy "MyClass"

    def __init__(self, x = 1):
        self.__x = x
        MyClass.__counter += 1


obj1 = MyClass(1)
print(obj1.__dict__, obj1._MyClass__counter)
obj2 = MyClass(2)
print(obj2.__dict__, obj2._MyClass__counter)
obj3 = MyClass(77)
print(obj3.__dict__, obj3._MyClass__counter)


print("Ile obiektów?", MyClass._MyClass__counter)
"""
{'_MyClass__x': 1} 1
{'_MyClass__x': 2} 2
{'_MyClass__x': 77} 3
Ile obiektów? 3
"""
print()

#######################################################################################################################

# WYWOŁANIE WŁAŚCIWOŚCI __dict__ DLA KLASY

print(MyClass.__dict__)
"""
'__module__': '__main__', '_MyClass__counter': 3, '__init__': <function MyClass.__init__ at 0x00000253D27059E0>, 
'__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
 '__doc__': None}
 
 Daje nam to informacje o zachowaniu danej klasy.
"""