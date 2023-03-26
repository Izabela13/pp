# Object Oriented Programming

# # napisanie klasy - definiujemy klasę stosu
# # __init__(self) - Inicjalizacja obiektów tej samej klasy
#
# class Stack: # Upper Camel Case
#     def __init__(self): # declaracja ze słowem kluczowym "def".
#         print("Cześć!") # definiowanie konstruktora
#
# obj = Stack()
# # Po stworzeniu tego obiektu dostajemy "Cześć!". Zdefiniowany konstruktor __init__(self) wywoła się


# class Stack:
#     def __init__(self):
#         self.stack_list = [] # pusta lista
#
# obj = Stack()
# print(len(obj.stack_list)) # 0 (zwróciło się 0, bo stack_list to na razie pusta lista
#
# # Jeżeli właściwość zapiszemy z dwoma podkreślnikami, jest traktowana jako prywatna.
# # Hermetyzacja - zabezpieczenie przed przypadkową modyfikacją
# # Tylko klasa będzie dostępna


# class Stack:
#     def __init__(self):
#         self.__stack_list = [] # pusta lista

# obj = Stack()
# print(len(obj.__stack_list))
# # Wyjątek AttributeError - zabezpieczenie przed wykonaniem

# obj = Stack()
# obj.__stack_list = [4, 4, 4] # dodanie nowej właściwości, która jest widoczna
# print(len(obj.__stack_list))


# # Dodawanie nowej właściwości
# class Stack:
#     def __init__(self):
#         self.__stack_list = [] # pusta lista
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
# # obj = Stack()
# # obj2 = Stack()
# #
# # obj.push(3)
# # obj.push(2)
# # obj.push(1)
# #
# # obj.__stack_list = [4, 4, 4] # dodani nowej właściwości. Logika pozostaje niezmienna (I zaleta)
# #
# # print()
# #
# # print(obj.pop())
# # print(obj.pop())
# # print(obj.pop())
#
#
# obj = Stack()
# obj2 = Stack()
# obj3 = Stack()
#
# obj.push(3)
# obj.push(2)
# obj.push(1)
#
# obj2.push(4)
# obj2.push(4)
# obj2.push(4)
#
# obj3.push("Ania")
# obj3.push("Zosia")
# obj3.push("Tomek")
#
# print()
#
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
#
# print()
#
# print(obj2.pop())
# print(obj2.pop())
# print(obj2.pop())
#
# print()
#
# print(obj3.pop())
# print(obj3.pop())
# print(obj3.pop())


# Stos ma mieć możliwość dodatkowo zliczania sumy wszystkich elementów

class Stack:
    def __init__(self):
        self.__stack_list = [] # pusta lista

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class StackSum(Stack): # dziedziczenie
    def __init__(self):
        Stack.__init__(self) # jawnie wpisać argument self - jawne wywołanie konstruktora
        self.__sum = 0

    def get_sum(self):
        return self.__sum # sum jest prywatna, ale wolno nam się do niej odwołać

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


# ------------------------------------------------------------------------------------------


obj = StackSum()
obj2 = StackSum()

obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())

print()

print(obj.pop())
print(obj.pop())
print(obj.pop())

print()

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())

print()

print("Ściągamy elementy ze stosów!")
print("stos 1", obj.get_sum())
print("stos 2", obj2.get_sum())