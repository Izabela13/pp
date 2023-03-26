# class MyClass:
#
#     def my_method(self): # domyślny parametr "self". Dla metod jest obowiązkowy
#         print("To jest moja metoda")
#
# obj = MyClass()
# obj.my_method()




# class MyClass:
#
#     def my_method(self, x):
#         print("To jest moja metoda z parametrem:", x)
#
# obj = MyClass()
# obj.my_method(123)




# class MyClass:
#     y = 99
#
#     def my_method(self, x):
#         print("To jest moja metoda z parametrem:", x, "i zmienną klasy", self.y) # odwołanie do y przez parametr "self"
#
# obj = MyClass()
# obj.my_method(123)




class MyClass:
    y = 99

    def my_method(self, x):
        self.other_method() # odwołanie do innej metody za pomocą metody "self"
        print("To jest moja metoda z parametrem:", x, "i zmienną klasy", self.y) # odwołanie do y przez parametr "self"

    def other_method(self):
        print("To jest metoda", self.y)
        print()

obj = MyClass()
obj.my_method(123)

# Cecha programowania obiektowego. Tworząc obiekty nie trzeba tworzyć kolejności. Nie ma znaczenia jak w klasie będą
# uporządkowane elementy, dlatego, że klasa nie jest wykonywana od początku do końca.
# Klasa ma zbiór właściwości. W zależności od tego, co jest wywoływane, taka kolejność się pojawi.

# konstruktor to pierwsza metoda