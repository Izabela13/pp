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
        print(Stack)


# 3 stosy (obiekty klady Stack)
obj1 = Stack()
obj2 = Stack()
obj3 = Stack()


# na pierwszym stosie kolejno liczby od 1 do 100
obj1.push(i for i in range(1, 101))
#obj1.push([i for i in range(1, 101)])

# ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim
obj2.pop()

