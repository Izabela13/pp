# Ciąg Fibonnaciego to taki ciąg, który dwa pierwsze elementy ma równe 1. Są one stałe i znane.
# Kolejne elementy ciągu są tworzone przez sumę dwóch poprzedzających go elementów.
# 1 1 2 3 5 8 13 21 34 ...

# Funkcja będzie wyznaczała wartość danego elementu.

def fib(n):  # Funkcja będzie wyznaczała wartość danego elementu. "n" będzie wskazywało na numer elementu ciągu.
    # Dodanie warunków sprawdzających do funkcji.
    if n < 1:  # Jeżeli liczba będzie mniejsza niż 1, to nic nie zostanie zwrócone (ciąg musi zaczynać się od 1).
        return None
    if n < 3:  # Jeżeli fib = 1 lub fib = 2, to funkcja będzie zwracać wartość 1.
        return 1 # Jeżeli podane "n" jest mniejsze od 3, to zwrócona zostanie wartość 1.

    # Za każdym razem, żeby wyliczyć wartość n-tego elementu trzeba znać dwa elementy poprzedzające.
    el1 = el2 = 1  # element_1 i element_2 wynoszą 1 (sytuacja startowa - początek ciągu Fibonacciego).
    sum = 0  # Zmienna pomocnicza "sum". Na razie suma wynosi 0. Zmienna "sum" będzie sumować w pętli.

    for i in range(3, n + 1):  # w pętli for w zakresie od 3 (bo nie interesuje nas element 1 i 2) do "n + 1"
        sum = el1 + el2  # zmienna "sum" będzie przechowywać sumę elementów pierwszego i drugiego. Jeżeli mamy sumę to
        el1, el2 = el2, sum  # musimy przesunąć element 1 i element 2. Od tego momentu element_1 będzie elementem_2 a...
    return sum  # ... element_2 będzie sumą, którą sobie policzyliśmy, czyli "sum".

# print(fib(5))  # 5
# print(fib(6))  # 8
# print(fib(2))  # 1
# print(fib(8))  # 21

# Wypisanie wszystkich elementów ciągu Fibonacciego dla zakresu od 1 do 100.
for n in range(1, 101):
    print(n, "->", fib(n))  # Wyświetlenie elementu i wartość danej pozycji ciągu Fibonacciego