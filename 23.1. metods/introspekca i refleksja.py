class MyClass:
    x = 5

    def __init__(self):
        self.y = 9

obj = MyClass()
print(obj.x, obj.y) # 5 9

print(MyClass.__dict__)
print(obj.__dict__) # {'y': 9} zmienna instancji (charakterystyczna tylko dla obiektu)


# REFLEKSJA
setattr(obj, "z", 1)
print(getattr(obj, "x")) # INTROSPEKCJA - odczytanie
print("z:", obj.z)