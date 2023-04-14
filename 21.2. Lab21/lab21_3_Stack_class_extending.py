"""
3. Rozbuduj klasę Stack o następujące metody:
• empty() - powinna zwracać True jeżeli stos jest pusty, w przeciwnym wypadku zwracać False,
• size() - powinna zwracać rozmiar stosu,
• top() - powinna zwracać "górny" element stosu, czyli ten, który zostanie "ściągnięty" metodą pop().
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

    def empty(self):
        if len(self.__stack_list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.__stack_list)

    def top(self):
        if len(self.__stack_list) == 0:
            return "Brak elementów w stosie."
        return self.__stack_list[-1]


# Testy
stack = Stack()  # utworzenie instancji dla klasy "Stack"


# ZAŁOŻENIE: Stos jest pusty
print("Stos jest pusty:", end=" "), stack.show_val()
print()

# Test1: Sprawdzenie poprawności działania metody empty()
print("Czy stos jest pusty?", stack.empty())  # True

# Test 2: Sprawdzenie poprawności działania metody size()
print("Ile elementów jest w stosie?", stack.size())  # 0

# Test 3: Sprawdzenie poprawności działania metody top()
print("Jaki jest górny element stosu?", stack.top())  # Brak elementów w stosie.
print("\n")


# ZAŁOŻENIE: Stos zawiera jakieś elementy
for n in range(1, 11):
    stack.push(n)

print("Stos zawiera elementy:", end=" "), stack.show_val()
print()

# Test1: Sprawdzenie poprawności działania metody empty()
print("Czy stos jest pusty?", stack.empty())  # False

# Test 2: Sprawdzenie poprawności działania metody size()
print("Ile elementów jest w stosie?", stack.size())  # 10

# Test 3: Sprawdzenie poprawności działania metody top()
print("Jaki jest górny element stosu?", stack.top())  # 10
print()

print("Usuwam 3 elementy ze stosu.")
for n in range(3):
    stack.pop()

print("Stos po usunięciu 3-ech elementów:", end=" "), stack.show_val()
print("Jaki jest górny element stosu?", stack.top())  # 7