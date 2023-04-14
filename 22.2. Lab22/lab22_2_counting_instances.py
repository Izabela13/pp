"""
2. Napisz klasę zliczającą wszystkie powstałe swoje instancje.
"""

class MyClass:

    counter = 0

    def __init__(self):
        MyClass.counter += 1


print()
print("Ilość początkowa instancji:", MyClass.counter, "\n")

print("Generowanie instancji:")
for o in range(10):
    o = MyClass()
    print("instancja", MyClass.counter)

print()
print("Suma powstałych instancji:", MyClass.counter)