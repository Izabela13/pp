"""
2. Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenia do 100.
"""

def multiplication_table(x, y):

    if x == 10 and y == 10:
        return

    elif x <= 10 and y <= 10:
        print(str(x), "x", str(y), "=", str(x * y))
        y += 1
        if y == 10:
            print(str(x), "x", str(y), "=", str(x * y))
            print()
            x += 1
            y = 1
        multiplication_table(x, y)


print("\nTabliczka mnożenia do 100 (dla liczb od 1 do 10).\n")
multiplication_table(1, 1)