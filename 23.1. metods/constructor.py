# Funkcją konstruktora jest inicjalizacja obiektu

# class MyClass:
#     def __init__(self, name):
#         self.__name = name
#         print("Inicjalizuję obiekt!")
#
#     def getname(self):
#         return self.__name
#
# obj = MyClass("Iza")
# print("Mam na imię", obj.getname())



# Metody prywatne - zaczyna się od podkreślenia
class MyClass:
    def __my_private_metod(self):
        print("To jest metoda prywatna...")

    def my_public_method(self):
        self.__my_private_metod()
        print("To jest metoda publiczna")

obj = MyClass() # nic się nie pojawia
#obj.__my_private_method() # Zwróci wyjątek AtributeError (METODA PRYWATNA)
obj.my_public_method()
"""
To jest metoda prywatna...
To jest metoda publiczna

Metoda prywatna służy do ukrycia pewnych elementów przed użytkownikiem
"""

print()

print(obj.__dict__) # pusty słownik. nie ma tu żadnej zmiennej instancji, ktora mogłaby się pojawić przy wywołaniu
print(MyClass.__dict__) # szereg elementów

print()
print(MyClass.__name__) # MyClass

print()
print(type(obj).__name__) # Jak jest obiekt bez klasy, można wywołać w ten sposób

print()
print(MyClass.__module__) # klasa jest w module __main__
# Może się to zmienić, jeśli zaimportujemy coś z innego modułu, np. stack_oop
# Możemy też wywołać __module__ na obiekcie