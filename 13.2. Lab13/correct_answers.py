# Zadanie 1

# def pow(numbers, exponent):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
# print(pow([1, 2, 3], 2))
# print(pow([2, 7, 33], 5))


# Wariacje

# wariacja 1
# def pow2(numbers, exponent):
#     result = [] # kopia tablcy
#
#     for n in numbers:
#         result.append(n ** exponent)
#     return result
#
# print(pow2([1, 2, 3], 2))
# print(pow2([2, 7, 33], 5))


#  wariacja 2
# def pow3(numbers, exponent):
#     return [x ** exponent for x in numbers]
#
# print(pow3([1, 2, 3], 2))
# print(pow3([2, 7, 33], 5))



# # Zadanie 2 multiplication_table
#
# def show_operation(a, b):
#     print(a, "x", b, "=", a*b)
#     if a == 10 or b == 10:
#         return
#     elif a == 10:
#         show_operation(1, b + 1)
#     else:
#         show_operation(a + 1, b)
#
# show_operation(1, 1)



# Zadanie 3 simple fruit machine

"""
3. Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
w tym celu:
• za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
• kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
• wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
• przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
większą liczbę liter.
"""

import random

## print(ord()) # będzie zwracać numerek reprezentowany przez dany znak

# definiowanie funkcji i rozbijanie na moduły

# def draw_letter():
#     return chr(random.randint(ord("A"), ord("E")))
#
# def draw_row():
#     return [draw_letter() for i in range(3)]
#
# def check(row):
#     if row[0] == row[1] and row[1] == row[2]:
#         return True
#     else:
#         return False
#
# counter = 1
# while True:
#     row = draw_row()
#     print(row, counter)
#     if check(row):
#         break
#     else:
#         counter += 1

# Przy takim zbiorze nie przekroczy się 100

# Jak dużo zmian trzebaby wprowadzić do funkcji, żeby zwiększyć ilość liter do wylosowania i zakres losowania

# definiowanie funkcji i rozbijanie na moduły

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))  # 1 zmiana

def draw_row():
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]  # 2 zmiana

def check(row):  # 3 zmiana - losowanie do wartości NUMBER_OF_LETTERS

    first_element = row[0] # zmienna pomocnicza

    for element in row:
        if element != first_element:
            return False
        return True


counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    else:
        counter += 1