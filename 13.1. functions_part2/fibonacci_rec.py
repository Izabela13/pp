# # To samo zadanie, co w pliku "fibonacci", ale z wykorzystaniem rekurencji

# # Demonstracja przed wykonaniem zadania
# def recursion(number): # Do funkcji będzie podstawiana wartość, np. "number".
#     if number == 20:   # warunek postawiony po to, aby w któymś momencie się zatrzymać
#         return         # wyjście z funkcji
#     print(number)      # wydrukowanie liczby
#     number += 1        # podniesienie liczby o 1
#     recursion(number)  # wywołanie funkcji przez samą siebie - to "number", które zostało podniesione o 1
                         # zostaje przekazane do funkcji i ponownie przechodzi przez ciało funkcji.

"""
1. Wywoływanie funkcji i podawanie jakiejś wartości "number", np. 10.
2. Zostanie sprawdzony warunek, czy "number" == 20. Jeśli tak, to funkcja nie zwróci nic.
3. Zostanie wydrukowana wartość 10.
4. Wartość 10 zostanie podniesiona o 1, czyli 11
5. Zostanie wywołana funkcja z wartością 11, co spowoduje ponowne wejście do funkcji.
Cały proces będzie się powtarzał do momentu, dopóki wartość "number" nie będzie równa 20.
Ta funkcja przypomina trochę matrioszki - jedna funkcja chowa się w drugą. Warunek "number == 20" był potrzebny po to,
aby w którymś momencie wyhamować funkcję.
"""

# recursion(10)  # Pojawią się wartości od 10 do 19, bo przy wartości 20 funkcja się zatrzymuje.
# # Następuje ciąg wywołań. W którymś momencie będzie trzeba to wszystko zwinąć. Przerwana zostanie każda funkcja.
# # Z każdej poszczególnej funkcji będzie trzeba wyjść. Recursion 20 zostanie wywołane, ale nic się nie wyświetli.
# print()
# recursion(19) # 19



# CIĄG FIBONACCIEGO Z MECHANIZMEM REKURENCJI - IMPLEMENTACJA pliku fibonacci z zaprzęgnięciem mechanizmu rekurencji
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    # wywołanie funkcji fib
    return fib(n - 1) + fib(n - 2)

for n in range(1, 10):
    print(n, "->", fib(n))

"""
# 1 1 2 3 5 8 13 21 34...

Wyniki:
1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34
"""