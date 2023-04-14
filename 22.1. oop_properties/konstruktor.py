# # FUNKCJA hasattr() - CZY MA ATRYBUT?


class MyClass:

    def __init__(self, x=1):
        if x % 2 == 0:  # Jeżeli "x" będzie parzyste, to...
            self.a = x  # ... przypisz to, co jest w "x"
        else:
            self.b = x


obj = MyClass()  # Jeżeli została przyjęta wartość domyślna, to nie spełnia ona warunku parzystości.

if hasattr(obj, "a"): # Jeżeli nasz obiekt ma właściwość "a"...
    print("a")  # ... wyświetl "a"
else:
    print("b")


print()

#######################################################################################################################


class MyClass:

    def __init__(self, x=1):
        if x % 2 == 0:
            self.a = x
        else:
            self.b = x


class A:
    x = 1  # klasa "A" ma właściwość zmienną "x" równą 1


obj = MyClass() # jeżeli została przyjęta wartość domyślna, to nie spełnia ona warunku parzystości

if hasattr(obj, "a"):
    print("a")
else:
    print("b")

obj2 = A()
print(hasattr(A, "y"))  # Czy klasa "A" ma atrybut "y"? Powinniśmy dostać "False".
print(hasattr(A, "x"))  # Czy klasa "A" ma atrybut "x"? Powinniśmy dostać "True".