class A:
    pass

class B:
    pass

class C (A, B):
    pass

print(C.__bases__) # Krotka: (<class '__main__.A'>, <class '__main__.B'>)

for c in C.__bases__:
    print(c.__name__)
"""
Krotka z nadklasami: 
A
B
"""