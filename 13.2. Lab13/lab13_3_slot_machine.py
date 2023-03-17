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


# Funkcja losująca 3 litery ze zbioru od A do E:

def draw_3_letters():
    drawn_letters = []

    for letter in range(3):
        drawn_letters.append(chr(random.randint(ord("A"), ord("E"))))

    return drawn_letters


# Funkcja losująca litery do momentu wystąpienia 3 takich samych liter:

def checking_letters(letters_row):
    if letters_row[0] == letters_row[1] == letters_row[2]:
        return True


# Wyświetlenie informacji o wynikach poszczególnych losowań oraz numer próby
print("Losowanie 3 liter ze zbioru od A do E do momentu uzyskania rzędu tych samych liter.")

counter = 1
while True:
    letters_row = draw_3_letters()
    print("Wynik losowania:", letters_row, " Numer próby:", counter)
    if checking_letters(letters_row):
        break
    else:
        counter += 1
print("\n")


# Jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także większą liczbę liter?

# 1 ZMIANA: określenie zakresu liter
first_letter = "A"
last_letter = "F"
# 2 ZMIANA: określenie, ile liter będzie zawierał rząd
number_row = 5


# Funkcja losująca litery ze zbioru określonego zmiennymi "first_letter" i "last_letter":
def draw_letters():
    drawn_letters = []

    for letter in range(number_row):  # zakres liter do wylosowania określony jest w zmiennej "number_row"
        drawn_letters.append(chr(random.randint(ord(first_letter), ord(last_letter))))

    return drawn_letters


# 3 ZMIANA: sprawdzanie w pętli, czy poszczególne litery są takie same

# Funkcja losująca litery do momentu wystąpienia takich samych liter w rzędzie:
def check_all_letters(letters_row):

    first_from_left = letters_row[0]

    for letter in letters_row:
        if letter != first_from_left:
            return False
    return True


# Wyświetlenie informacji o wynikach poszczególnych losowań oraz numer próby
print("Losowanie", number_row, "liter ze zbioru od", first_letter, "do", last_letter, "do momentu uzyskania rzędu tych samych liter.")

counter = 1
while True:
    letters_row = draw_letters()
    print("Wynik losowania:", letters_row, " Numer próby:", counter)
    if check_all_letters(letters_row):
        break
    else:
        counter += 1