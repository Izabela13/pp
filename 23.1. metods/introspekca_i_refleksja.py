class MyClass:
    x = 5  # zmienna klasy

    def __init__(self):  # za pomocą konstruktora definiujemy zmienną instancji
        self.y = 9  # zmienna instsancji


obj = MyClass()
print(obj.x, obj.y)  # 5 9 --> właściwości

print(MyClass.__dict__)  # wszystkie właściwości klasy
print(obj.__dict__)  # {'y': 9} --> zmienna instancji (charakterystyczna tylko dla obiektu)


# REFLEKSJA - podmienianie jakiejś właściwości za pomocą funkcji "setattr()"
setattr(obj, "z", 1)  # "Dodaj nowy atrybut i ustaw go na 1". Wstrzyknięcie.
print(getattr(obj, "x"))  # INTROSPEKCJA - odczytanie - getattr()
print("z:", obj.z)  # z: 1