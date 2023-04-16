# Funkcją konstruktora jest inicjalizacja obiektu

# class MyClass:
#     def __init__(self, name):
#         self.__name = name  # zmienna instancji
#         print("Inicjalizuję obiekt!")  # funkcja konstruktora - inicjalizacja obiektu

#     def getname(self):
#         return self.__name

# obj = MyClass("Iza")
# print("Mam na imię", obj.getname())



# Metody prywatne - zaczyna się od podwójnego podkreślenia
class MyClass:
    def __my_private_method(self):
        print("To jest metoda prywatna...")  # Ta metoda będzie drukowała napis "To jest metoda prywatna".

    def my_public_method(self):
        self.__my_private_method()  # Metoda publiczna, która wywołuje metodę prywatną
        print("To jest metoda publiczna")


obj = MyClass()  # nic się nie pojawia, ponieważ metoda jest prywatna
# obj.__my_private_method()  # Zwróci wyjątek AtributeError (METODA PRYWATNA)
# obj._MyClass__my_private_method() # Mi to nie działa, choć powinno działać
obj.my_public_method()  # wywołanie metody publicznej, która wywoła metodę prywatną
"""
To jest metoda prywatna...
To jest metoda publiczna

Metoda prywatna służy do ukrycia pewnych elementów przed użytkownikiem.
Do metod prywatnych można odwołać się z wnętrza klasy, np. metoda publiczna wywołuje metodę prywatną
"""

print()


# Właściwość __dict__ dla obiektu i dla klasy.
print(obj.__dict__)  # pusty słownik. Nie ma tu żadnej zmiennej instancji, ktora mogłaby się pojawić przy wywołaniu
print(MyClass.__dict__)  # szereg elementów
"""
{}

{'__module__': '__main__', '_MyClass__my_private_method': <function MyClass.__my_private_method at 0x000001B1F19DA340>, 
'my_public_method': <function MyClass.my_public_method at 0x000001B1F19DA2A0>, '__dict__': <attribute '__dict__' of 
'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}

Dla obiektu dostajemy pusty słownik, ponieważ w zdefiniowanej klasie nie mamy zmiennej instancji, która mogłaby się
pojawić przy wywołaniu obiektu. 
Przy wywołaniu "MyClass.__dict__" pojawi się szereg elementów
"""


# Właściwość __name__ - zwraca nazwę klasy
print()
print(MyClass.__name__)  # MyClass

print()
print(type(obj).__name__)  # MyClass --> Jak jest obiekt bez klasy, można wywołać w ten sposób


# Właściwość __module__ - w jakim module znajduje się klasa
print()
print(MyClass.__module__)  # klasa jest w module __main__
"""
Może się to zmienić, jeśli zaimportujemy coś z innego modułu, np. 
print(Stack.__module__) --> stack_oop (Klasa "Stack" znajduje się w module "stack_oop")

Możemy też wywołać właściwość __module__ na obiekcie, np. 
print(obj.__module__) --> __main__
"""