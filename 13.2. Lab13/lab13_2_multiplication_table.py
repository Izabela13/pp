"""
2. Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.
"""

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     # użyjemy informacji, które są wcześniej
#     return fib(n - 1) + fib(n - 2)
#
# for n in range(1, 10):
#     print(n, "->", fib(n))


# def multiplication(n, m):
#     n * m
#
#     for n in range(1, 11):
#         print(n, "*", n, "=", multiplication(n))

def multiplication(m, n):

    for m in range(1, 11):
        for n in range(1, 11):
            m * n

    return print(m*n)