# Ciąg Fibonnaciego to taki ciąg, który dwa pierwsze elementy są równe 1. Są one stałe i znane.
# Kolejne elementy ciągu są tworzone przez sumę dwóch poprzednich
# 1 1 2 3 5 8 13 21 34 ...

# Funkcja będzie wyznaczała wartość danego elementu.

def fib(n): # n będzie wskazywało na numer elementu ciągu
    if n < 1:
        return None
    if n < 3:
        return 1

    el1 = el2 = 1
    sum = 0 # na razie suma wynosi 0

    for i in range(3, n + 1):
        sum = el1 + el2
        el1, el2 = el2, sum
    return sum

# print(fib(5))  # 5
# print(fib(8))  # 21

for n in range(1, 101):
    print(n, "->", fib(n))