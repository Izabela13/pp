# To samo zadanie, ale z wykorzystaniem rekurencji

# def recursion(number):
#     if number == 20: # warunek postawiony po to, aby w któymś momencie się zatrzymać
#         return
#     print(number)
#     number += 1
#     recursion(number)
#
# recursion(10)
# # następuje ciąg wywołań. Recursion 20 zostanie wywołane, ale nic się nie wyświetli
# print()
# recursion(19) # 19


# Ciąg Fibonnaciego
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    # użyjemy informacji, które są wcześniej
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