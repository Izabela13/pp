# a = 1
# b = 4
#
# print("a =", a, "b =", b)
#
# # a = b
# # b = a
# #
# # print("a =", a, "b =", b)
#
# # # tworzenie zmiennej pomocniczej (poczekalni, do której na chwilę odłożymy wartość)
# # tmp = a
# # a = b
# # b = tmp
# #
# # print("a =", a, "b =", b)
#
# a, b = b, a # najprostszy sposób zamiany wartości
# print("a =", a, "b =", b)


# # Tworzenie listy
# numbers = [1, 2, 3]
#
# numbers[0], numbers[1] = numbers[1], numbers[0] # prosty sposób na zamianę dwóch elementów w liście
# print(numbers)


# sortowanie ciągów znaków
letters = ["A", "C", " ", "B"]
print(letters)

letters.sort()
print(letters)

letters.sort(reverse=True)
print(letters)
# Każdy znak jest zakodowany jakąś wartością.

print(ord("A"), ord("C"))
print(ord("a"), ord("c"))
# Kolejność sortowania bierze się z tablic ASCI