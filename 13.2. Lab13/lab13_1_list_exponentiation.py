"""
1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.
"""

def exponentiation(numbers, power):
    print("Wprowadzone elementy listy:", numbers)

    for i in range(len(numbers)):
        numbers[i] **= power
    print("Podniesine do potęgi", power, "elementy listy:", numbers)
    print()


exponentiation([1, 2, 3, 4, 5], 2)
exponentiation([1, 2, 3, 4, 5], 3)
exponentiation([1, 2, 3, 4, 5], 4)