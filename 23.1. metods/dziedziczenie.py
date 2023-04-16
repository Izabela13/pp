# WŁAŚCIWOŚĆ __bases__

class A:
    pass


class B:
    pass


class C (A, B):  # Klasa "C", która będzie dziedziczyć po klasie "A" i "B"
    pass


print(C.__bases__)  # Krotka z nadklasami, po których dziedziczy klasa: (<class '__main__.A'>, <class '__main__.B'>)

for c in C.__bases__:
    print(c.__name__)
"""
Krotka z nadklasami: 
A
B
"""