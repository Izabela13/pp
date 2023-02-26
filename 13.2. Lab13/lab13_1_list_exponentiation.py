"""
1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.
"""

def exponentiation(numbers): # BRAKŁO WSKAZANEJ POTĘGI
    print("Wprowadzone elementy listy: ", numbers)

    for i in range(len(numbers)):
        numbers[i] **= 2
    print("Podniesine do kwadratu elementy listy: ", numbers)


numbers = [1, 2, 3, 4, 5, 6, 7]
exponentiation(numbers)