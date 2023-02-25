"""
2. Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
prostokątów o następujących długościach boków:
• 4 i 5,
• 2678 i 5678,
• 344555 i 788998.
"""


# funkcja obliczająca obwód: 2 * (a +b)
# funkcja obliczająca pole powierzchni: P = a * b
# funkcja obliczająca długość przekątnej: c = (a ** 2 + b ** 2) ** 0.5

# perimieter - obwód

def length(a, b):
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))

    return \
        2 * (a * b)

