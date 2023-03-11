"""
2. Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
prostokątów o następujących długościach boków:
• 4 i 5,
• 2678 i 5678,
• 344555 i 788998.
"""


# funkcja obliczająca obwód: 2 * (a +b)
def perimeter(a, b):
    return 2 * (a + b)


# funkcja obliczająca pole powierzchni: P = a * b
def surface_area(a, b):
    return a * b


# funkcja obliczająca długość przekątnej: c = (a ** 2 + b ** 2) ** 0.5
def diagonal_length(a, b):
    return round((a ** 2 + b ** 2) ** 0.5, 2)


# funkcja zbierająca wszystkie informacje:
def results(a, b):
    print("Dla prostokąta o długościach boków", a, "i", b, "obwód, pole powierzchni i długość przekątnej \n"
          "wynoszą kolejno: \n"
          "- obwód:              ", str(perimeter(a, b)) + "; \n"
          "- pole powierzchni:   ", str(surface_area(a, b)) + "; \n"
          "- długość przekątnej: ", str(diagonal_length(a, b)) + ". \n")


results(4, 5)
results(2_678, 5_678)
results(344_555, 788_988)