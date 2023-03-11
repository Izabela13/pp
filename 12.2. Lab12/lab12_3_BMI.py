"""
3. Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
• zapytaj użytkownika o wzrost i wagę,
• stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
• stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
  otyłość) na podstawie wskaźnika BMI,
• zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.
"""

"""
Informacje pomocnicze:
BMI = masa ciała (kg) / wzrost (m)²

Zakresy: 
• poniżej 16,0 – wygłodzenie,
• 16.0 – 16.9 – wychudzenie,
• 17.0 – 18.4 – niedowaga,
• 18.5 – 24.9 – wartość prawidłowa,
• 25.0 – 29.9 – nadwaga,
• 30.0 – 34.9 – I stopień otyłości,
• 35.0 – 39.9 – II stopień otyłości,
• powyżej 40.0 – III stopień otyłości (inaczej: otyłość skrajna).
"""


# 2. Funkcja obliczająca wskaźnik BMI na podstawie podanych przez użytkownika danych
def bmi_count(height_cm, weight_kg):
    return round(weight_kg / (height_cm * 0.01) ** 2, 1)


# 3. Funkcja wyznaczającą odpowiednią kategorię na podstawie wskaźnika BMI
def bmi_range(bmi):
    if bmi < 16.0:
        return "wygłodzenie"

    elif bmi <= 16.9:
        return "wychudzenie"

    elif bmi <= 18.4:
        return "niedowaga"

    elif bmi <= 24.9:
        return "waga prawidłowa"

    elif bmi <= 29.9:
        return "nadwaga"

    elif bmi <= 34.9:
        return "I stopień otyłości"

    elif bmi <= 39.9:
        return "II stopień otyłości"

    elif bmi >= 40.0:
        return "III stopień otyłości"


# 1. Pytanie użytkownika o jego wzrost i wagę.
print("Kalkulator BMI – oblicz swój wskaźnik masy ciała (Body Mass Index).")
height_cm = int(input("Podaj swój wzrost w centymetrach: "))
weight_kg = int(input("Podaj swoją wagę w kilogramach: "))
print()


# 4. Prezentacja wyników z wykorzystaniem wcześniej przygotowanych funkcji
bmi = bmi_count(height_cm, weight_kg)
bmi_category = bmi_range(bmi)

print("Twoje BMI wynosi:", bmi_count(height_cm, weight_kg))
print("Mieścisz się w kategorii:", bmi_category)