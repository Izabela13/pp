# class MyClass:
#
#     def __init__(self, x=1):
#         if x % 2 == 0:
#             self.a = x
#         else:
#             self.b = x
#
#
# obj = MyClass() # jeżeli została przyjęta wartość domyślna, to nie spełnia ona warunku parzystości
#
# if hasattr(obj, "a"):
#     print("a")
# else:
#     print("b")


class MyClass:

    def __init__(self, x=1):
        if x % 2 == 0:
            self.a = x
        else:
            self.b = x


class A:
    x = 1


obj = MyClass() # jeżeli została przyjęta wartość domyślna, to nie spełnia ona warunku parzystości

if hasattr(obj, "a"):
    print("a")
else:
    print("b")

obj2 = A()
print(hasattr(A, "y"))
print(hasattr(A, "x"))