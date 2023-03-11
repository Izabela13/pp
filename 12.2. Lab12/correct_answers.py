# # Zadanie 1: char_printer

# # Będziemy potrzebować funkcji. Funkcja powinna:
# # 1) być sparametryzowana
# # 2) pobierać 3 argumenty (i posiadać 3 parametry)
# # 3) może przyjąć parametry domyślne

# # Zmienne "character", "rep" i "vert" to zmienne dostępne tylko i wyłącznie w ciele funkcji.
# # Fachowo mówiąc zmienne w funkcji to PARAMETRY i zakres widzialności tych wszystkich parametrów, czyli tych zmiennych
# # będzie tylko i wyłącznie w bloku funkcji. Nigdzie indziej nie będą one używane.

# def print_char(character = "*", rep = 10, vert=False):  # ustawienie domyślnych parametrów: * * * * * * * * * *
#     for i in range(rep):  # Po pierwsze znaczek ("character") ma się wyświetlić określoną ilość razy.
#         if vert:  # Zanim dojdzie do wyświetlania znaku, musimy sprawdzić parametr "vert".
#             print(character)  # Jeżeli zależy nam na tym, żeby znak wyświetlił się w pionie, wystarczy print znaku.
#         else:  # Jeżeli chcemy wyświetlić znaki w poziomie, wchodzimy do bloku else.
#             print(character + " " , end="")  # Wystarczy dodać słowo kluczowe 'end=""' w princie.
#     if not vert:  # Dodawanie odstępu pomiędzy kolejnymi wyświetleniami
#         print()
#     print() # Dodanie odstępu

# print_char()
# print_char("+", 5, True)
# print_char("^", 7, True)

# # Funkcja powinna być sparametryzowana
# # Parametry to zmienne, ale tylko w obrębie funkcji. Nie można ich użyć na zewnątrz.



# # Zadanie 2: rectangles

# # Zaczniemy od stworzenia kilku funkcji. Funkcje będą liczyły obwód, pole powierzchni i długość przekątnej.

# def perimeter(a, b):
#     return 2 * a + 2 * b  # obwód

# def surface_area(a, b):
#     return a * b  # pole powierzchni

# def diagonal_lenght(a, b):
#     return (a ** 2 + b ** 2) ** (1 / 2)  # długość przekątnej (z twierdzenia Pitagorasa)

# def show_result(a, b): # funkcja wyświetlająca rezultaty - w tej funkcji będziemy wywoływać inne funkcje
#     print("Prostokąt o bokach", a, "i", b)
#     print("Obwód:", perimeter(a, b))
#     print("Pole powierzchni:", surface_area(a, b))
#     print("Długość przekątnej:", diagonal_lenght(a, b))
#     print()  # do zrobienia odstępu
# # stos wywołań
# # poszczególne obliczenia wykonają się w funkcji "show_result" za pomocą innych funkcji, które wcześniej zostały przygotowane.
# # "a" i "b" zostaną przekazane do funkcji "show_result", dzięki czemu będzie można przekazać je do innych funkcji


# show_result(4, 5)
# show_result(2678, 5678)
# show_result(344555, 788988)

"""
PODSUMOWANIE:
1. Stworzyliśmy funkcje do liczenia poszczególnych obszarów. 
2. Napisaliśmy funkcję, która korzysta z funkcji wcześniejszych.
3. Wywołaliśmy tylko 3 razy funkcję "show_result".

Siła tego rozwiązania jest taka, że:
- jeżeli doszłoby do jakichś poprawek, poprawkę wprowadzamy w jednym miejscu.
- kod jest dużo bardziej czytelny.
- kod jest dużo bardziej spójny.
- zapisywanie funkcji nie ma przypadkowej kolejności - stanowią one logiczny ciąg.
"""



# # Zadanie 3: bmi_solver

# # BMI = waga / wzrost**2

# # 2. Funkcje definiujemy na górze kodu - pierwsza funkcja
def calculate_bmi(weight_in_kg, height_in_cm):  # będziemy podawać te wartości, które pozyskaliśmy od użytkownika
    return weight_in_kg / height_in_cm ** 2 # operator potęgowania ma wyższy priorytet, więc nie musimy wstawiać nawiasu


# # 3. Druga funkcja
def determinate_bmi_category(bmi): # będziemy tu podawać wskaźnik BMI
    if bmi < 18.5: # na postawie wskaźnika i odpowiednich warunków wyznaczymy kategorie
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return  "nadwaga"
    else:
        "otyłość"

# return - chcemy uzyskać odpowiedni ciag znaków i przekazać go do innego miejsca kodu.
# Dlatego nie wstawiamy print()


# 1. Zaczynamy od zapytania użytkownika o wzrost i wagę.
print("Obliczanie wskaźnika BMI.")
weight_in_kg = float(input("Podaj swoją wagę w kilogramach: "))  # wiadomo, co jest w zmiennej - waga w kilogramach
height_in_cm = float(input("Podaj swój wzrost w centymetrach: ")) # wiadomo, że zmienna przechowuje wzrost w cm


# 4. Prezentacja wyników wcześniej wykorzystach funkcji
# 4.1. Musimy policzyć BMI. Skorzystamy z wcześniej przygotowanej funkcji "calculate_bmi".
bmi = calculate_bmi(weight_in_kg, height_in_cm * 0.01)

# 4.2. Kategorie BMI zapisujemy do zmiennej "category" i korzystamy z funkcji "determinate_bmi_category".
#      Do funkcji przekazujemy wskaźnik bmi (wyliczony powyżej)
category = determinate_bmi_category(bmi)

# Wypisanie informacji użytkownikowi:
print("Wskaźnik BMI:", bmi)
print("Kategoria:", category)