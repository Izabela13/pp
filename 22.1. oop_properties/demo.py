# class MyClass:
#     def __init__(self, x=1):
#         self.x = x  # zmienna publiczna x
#
#     def sety(self, y):
#         self.y = y # zmienna prywatna (self to konstruktor, w którym następuje inicjalizacja. Sugestia, że można poprawić)
#
#
# obj1 = MyClass() # ustwiamy właściwość x = 1 (wartość domyślna)
# print(obj1.x) # można się odwołać do zmiennej publicznej
#
# obj2 = MyClass(4) # ustwiamy właściwość x = 4
# obj2.sety(7) # ustawiamy właściwość y = 7
#
# obj3 = MyClass(3)
# obj3.z = 99 # dodajemy nową właściwość i ustawiamy ją na z = 99 (zmienna instancji, dodana później)
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
# """
# {'x': 1}
# {'x': 4, 'y': 7}
# {'x': 3, 'z': 99}
# """
#
# # Konsekwencje są takie, że jeżeli teraz będziemy się chcieli odwołać do y, wystąpi wyjątek


# # Prywatne zmienne instancji
# class MyClass:
#     def __init__(self, x=1):
#         self.__x = x  # prywatna zmienna insancji
#
#     def sety(self, y):
#         self.__y = y # prywatna zmienna instancji
#
#
# obj1 = MyClass() # ustwiamy właściwość x = 1 (wartość domyślna)
#
# obj2 = MyClass(4) # ustwiamy właściwość x = 4
# obj2.sety(7) # ustawiamy właściwość y = 7
#
# obj3 = MyClass(3)
# obj3.__z = 99 # dodajemy nową właściwość i ustawiamy ją na z = 99 (zmienna instancji, dodana później)
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
# """
# {'_MyClass__x': 1}
# {'_MyClass__x': 4, '_MyClass__y': 7}
# {'_MyClass__x': 3, 'z': 99}
#
# Dodanie pseudoprywatnej zmiennej nie spowoduje przeobienia jej na zmienną prywatną
# """
#
# # print(obj1.__x) # nie ma nawet takiej nazwy
# # AttributeError: 'MyClass' object has no attribute '__x'
#
# print(obj1._MyClass__x)
# print(obj3.__z)


# Oprócz zmiennych instancji są również zmienne klasy
# Prywatne zmienne instancji
# class MyClass:
#
#     counter = 0 # zmienna klasy, wspólna dla całej klasy obiektów
#
#     def __init__(self, x = 1):
#         self.__x = x
#     # Konstruktor wywoływany jest za każdym tworzeniem obiektu
#         MyClass.counter += 1 # Zwiększenie przy każdym wywołaniu konstruktora
#
#
# obj1 = MyClass(1)
# print(obj1.__dict__, obj1.counter)
# obj2 = MyClass(2)
# print(obj2.__dict__, obj2.counter)
# obj3 = MyClass(77)
# print(obj3.__dict__, obj3.counter)
#
# # MyClass(77)
# # MyClass(77)
# # MyClass(77)
# # MyClass(77)
#
# print("Ile obiektów?", MyClass.counter)
# """
# {'_MyClass__x': 1} 1
# {'_MyClass__x': 2} 2
# {'_MyClass__x': 77} 3
# Ile obiektów? 3
# """
#
# # Klasy mają dostęp do właściwości klas.



class MyClass:

    counter = 0 # zmienna klasy, wspólna dla całej klasy obiektów

    def __init__(self, x = 1):
        self.__x = x
    # Konstruktor wywoływany jest za każdym tworzeniem obiektu
        MyClass.__counter += 1 # Zwiększenie przy każdym wywołaniu konstruktora


obj1 = MyClass(1)
print(obj1.__dict__, obj1._MyClass__counter)
obj2 = MyClass(2)
print(obj2.__dict__, obj2._MyClass__counter)
obj3 = MyClass(77)
print(obj3.__dict__, obj3._MyClass__counter)

# MyClass(77)
# MyClass(77)
# MyClass(77)
# MyClass(77)

print("Ile obiektów?", MyClass._MyClass__counter)
"""
{'_MyClass__x': 1} 1
{'_MyClass__x': 2} 2
{'_MyClass__x': 77} 3
Ile obiektów? 3
"""

# Klasy mają dostęp do właściwości klas.