"""
2. Korzystając z napisanej wcześniej klasy Stack:
• utwórz 3 stosy (3 obiekty klasy Stack),
• połóż na pierwszym stosie kolejno liczby od 1 do 100,
• ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
• ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
• ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.
"""


class Stack:
    def __init__(self):
        self.__stack_list = [] # pusta lista

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def show_val(self):
        print(self.__stack_list)


# Utworzenie 3 stosów (obiektów klasy Stack)
stack_1 = Stack()
stack_2 = Stack()
stack_3 = Stack()


# Położenie liczb od 1 do 100 na pierwszym stosie "stack_1"
print("Kładzenie liczb kolejno od 1 do 100 na pierwszym stosie.")
for n in range(1, 101):
    stack_1.push(n)

print("STOS 1:")
stack_1.show_val()
print("\n")


# Ściąganie kolejno elementów z pierwszego stosu i umieszczanie na drugim stosie
print("Ściąganie kolejnych liczb z pierwszego stosu i umieszczanie ich na drugim stosie.")
for n in range(100):
    stack_2.push(stack_1.pop())

print("STOS 1:")
stack_1.show_val()
print()

print("STOS 2:")
stack_2.show_val()
print("\n")


# Ściąganie kolejno elementów z drugiego stosu i umieszczanie na trzecim stosie
print("Ściąganie kolejnych liczb z drugiego stosu i umieszczanie ich na trzecim stosie.")
for n in range(100):
    stack_3.push(stack_2.pop())

print("STOS 2:")
stack_2.show_val()
print()

print("STOS 3:")
stack_3.show_val()
print("\n")


# Ściąganie kolejno elementów z trzeciego stosu
print("Ściąganie kolejnych liczb z trzeciego stosu.")

print("STOS 3 przed 'ściągnięciem' kolejnych liczb:")
stack_3.show_val()
print()

print("STOS 3 przy 'ściąganiu' kolejnych liczb:")
for n in range(100):
    print(stack_3.pop(), end=" ")  # ściąganie i wyświetlanie w tej samej linii elementów z trzeciego stosu