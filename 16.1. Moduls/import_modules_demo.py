# import math # słowo kluczowe "import" oraz nazwa bibliotek, np. "math".
# import sys # Po słowie kluczowym można wpisywać kolejne moduły, ale zaleca się pisanie jeden pod drugim
#
# from math import pi, sin, factorial, ceil
# # Można pobierać również jako "from math import *" - ale ten sposób jest niezalecany
#
# print(math.pi) # 3.141592653589793
# print(math.sin(math.pi/2)) # 1.0
#
#
# print(math.factorial(5)) # 1 * 2 * 3 * 4 * 5; Wynik: 120
# print(math.floor(4.9999)) # Wynik: 4 - ścięcie w dół
#
#
# print(pi) # 3.141592653589793
# # Nazwa modułu będzie niedostępna - dostaniemy wyjątek NameError.
#
# print(sin(pi / 2))
# print(factorial(7))
#
#
# print(ceil(3.8)) # 4


# Aliasowanie
# # Jeżeli zaimportujemy w sposób klasyczny moduł math, to za pomocą aliasu można przypisać nową nazwę dla modułu
# import math as m
#
# print(m.pi)
# # Gdybyśmy chcieli wrócić do nazwy modułu "math", będzie on niedostępny. Konsekwentnie trzeba używać aliasu
# # print(math.pi).


# from math import pi as mathpi
# print(mathpi)
# print(pi) # samo "pi" będzie niedostępne



# from random import random, seed
#
# seed(0) # Przy każdym losowaniu ciąg liczb będzie taki sam, np.
# """
# 0.8444218515250481
# 0.7579544029403025
# 0.420571580830845
# 0.25891675029296335
# 0.5112747213686085
#
# Komputer może wylosować coś na podstawie jakiegoś parametru
# """
#
# for i in range(5):
#     print(random())
#
# # Ziarno, od którego zależy generowanie liczb jest zależne od czegoś, np. od zegara w komputerze


# from random import choice, sample
#
# #list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = [i for i in range(1, 11)]
#
# print(choice(list))
# print(sample(list, 5)) # Liczby losowane bez powtórzeń
# print(sample(list, 10)) # Za każdym razem liczby będą w innym ułożeniu
# # Jeżeli będziemy chcieli 11 liczb, dostaniemy wyjątek, ponieważ przekroczy zakres dostępnych liczb


# import platform
#
# # help(platform)
# print(platform.machine()) # AMD64 - nazwa procesora (?)
# print(platform.processor()) #Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
# print(platform.system()) # Windows
# print(platform.version()) # 10.0.22621
# print(platform.python_implementation()) # CPython
# print(platform.python_version_tuple()) # ('3', '10', '7')


# from platform import machine, version
# help(machine)
# print(machine())
#
# help(version)
# print(version()) # 10.0.22621 - Windos 11, numer oprogramowania 10.0.22621


from platform import platform

help(platform)
print(platform()) # Windows-10-10.0.22621-SP0 (nazwa marketingowa Windows 11)

"""
Funkcja platform ma dwa parametry:
platform(aliased=0, terse=0) - typ bool
"""

print(platform(True, True)) # Windows-10 (nadal jest to nowy system operacyjny znany pod nazwą Windows 11)
