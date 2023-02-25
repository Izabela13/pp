# # Zadanie 1 char_print
#
# def print_char(character = "*", rep = 10, vert=False): # ustawienie domyślnych parametrów
#     for i in range(rep):
#         if vert:
#             print(character)
#         else:
#             print(character + " " , end="")
#     if not vert:
#         print()
#     print()
#
# print_char()
# print_char("+", 5, True)
# print_char("^", 7, True)
#
# # Funkcja powinna być sparametryzowana
# # Parametry to zmienne, ale tylko w obrębie funkcji.



# # Zadanie 2
#
# def permiter(a, b):
#     return 2 * a + 2 * b
#
# def surface_area(a, b):
#     return a * b
#
# def diagonal_lenght(a, b):
#     return (a ** 2 + b ** 2) ** 0.5
#
# def show_result(a, b):
#     print("Prostokąt o bokach", a, "i", b)
#     print("Obwód:", permiter(a, b))
#     print("Pole powierzchni:", surface_area(a, b))
#     print("Długość przekątnej:", diagonal_lenght(a, b))
#     print()
# # stos wywołań
#
# show_result(4, 5)
# show_result(2678, 5678)
# show_result(344555, 788988)



# Zadanie 3

# BMI = waga / wzrost**2

def calculate_bmi(weight_in_kg, height_in_cm):
    return weight_in_kg / height_in_cm ** 2 # operator potęgowania ma wyższy priorytet

def determinate_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return  "nadwaga"
    else:
        "otyłość"

print("Obliczanie wskaźnika BMI.")
weight_in_kg = float(input("Podaj swoją wagę w kilogramach: "))
height_in_cm = float(input("Podaj swój wzrost w centymetrach: "))

bmi = calculate_bmi(weight_in_kg, height_in_cm * 0.01)
category = determinate_bmi_category(bmi)

print("Wskaźnik BMI:", bmi)
print("Kategoria:", category)