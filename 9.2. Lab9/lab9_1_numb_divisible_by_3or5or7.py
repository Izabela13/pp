"""
Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
określonego przez użytkownika.
"""

print("Zostaniesz poproszony(a) o wprowadzenie dowolnego zakresu liczb całkowitych. \n"
      "Z podanego przez Ciebie zakresu zostanie zwrócony zbiór liczb podzielnych odrębnie przez: 3, 5 i 7. \n")

num_from = int(input("Wprowadź liczbę całkowitą stanowiącą początek zakresu: "))
num_to = int(input("Wprowadź liczbę całkowitą stanowiącą koniec zakresu: "))

print("")

print("Oto lista liczb wyselekcjonowanych z podanego przez Ciebie zakresu, które są podzielne albo przez 3 albo przez 5 albo przez 7: ")
for num in range(num_from, num_to + 1):
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(num, end="; ")
    else:
        print("", end="")

print("")
print("")

print("Liczby z zakresu od", num_from, "do", num_to)
print(" - podzielne przez 3 to:", end=" ")
for div in range(num_from, num_to + 1):
    if div % 3 == 0:
        print(div, end="; ")

print("\n - podzielne przez 5 to:", end=" ")
for div in range(num_from, num_to + 1):
    if div % 5 == 0:
        print(div, end="; ")

print("\n - podzielne przez 7 to:", end=" ")
for div in range(num_from, num_to + 1):
    if div % 7 == 0:
        print(div, end="; ")
