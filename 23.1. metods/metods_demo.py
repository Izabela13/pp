# class MyClass:

#     def my_method(self): # domyślny parametr "self". Dla metod jest on obowiązkowy.
#         print("To jest moja metoda")

# obj = MyClass()  # obiekt klasy "MyClass"
# obj.my_method()  # wywołanie metody "my_method".




# class MyClass:

#     def my_method(self, x):  # poza parametrem "self" został dołożony przez nas parametr "x".
#         print("To jest moja metoda z parametrem:", x)

# obj = MyClass()
# obj.my_method(123)  # parameter nie jest określony, można wpisać string,




# class MyClass:
#     y = 99  # zdefiniowana zmienna klasowa, tj. "y" = 99

#     def my_method(self, x):
#         print("To jest moja metoda z parametrem:", x, "i zmienną klasy", self.y) # odwołanie do y przez parametr "self"
"""
jeśli chcieć odwołać się bezpośrednio do zmiennej "y" (bez parametru "self"), to "y" będzie pokdreślony na czerwono
(PyCharm zgłosi błąd). Przy zapisie bez parametru "self", "y" jest nierozpoznawalny, ponieważ metoda "my_method" myśli,
że chcemy odwołać się do jakiejś lokalnej zmiennej, która powinna być zdefiniowana w tej metodzie. Jeżeli chcemy się
odwołać do zmiennej klasy można to zrobić przez parameter "self" --> "self.y".
"""
# obj = MyClass()
# obj.my_method(123)




class MyClass:
    y = 99

    def my_method(self, x):
        self.other_method()  # odwołanie do innej metody za pomocą parametru "self"
        print("To jest moja metoda z parametrem:", x, "i zmienną klasy", self.y) # odwołanie do y przez parametr "self"

    def other_method(self):
        print("To jest metoda", self.y)
        print()

obj = MyClass()
obj.my_method(123)

"""
Metoda "my_method" wywołała metodę "other_method". Dlatego w pierwszej kolejności pojawiło się: 

    To jest metoda 99
    
a później: 

    To jest moja metoda z parametrem: 123 i zmienną klasy 99


W programowaniu obiektowym można metoda może odwołać się do innej metody, która została później zdefiniwoana. 
Jest to cecha programowania obiektowego. Tworząc obiekty nie trzeba tworzyć kolejności. Nie ma znaczenia jak w klasie będą
uporządkowane elementy dlatego, że klasa nie jest wykonywana "od początku do końca". 
Klasa ma zbiór właściwości. W zależności od tego, jaka właściwość jest wywoływana, tak klasa sobie z tym poradzi.

Są jednak dobre praktyki. Zmienne klasowe zaleca się pisać na samej górze. Konstruktor to pierwsza metoda. 
- na początku właściwości związane z klasą
- konstruktor i właściwości instancji 
- zmienne instancji
Metody nie muszą być w tej samej kolejności, w jakiej będą wywoływane, bo klasie metody nie są wywoływane tak jak 
w przypadku skryptu - od góry do dołu. Z kolei poza klasą kolejność już obowiązuje. 
"""