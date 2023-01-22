"""
Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
określonego przez użytkownika.
"""

print("Wprowadź dowolny zakres liczb całkowitych. "
      "Zostanie Ci zwrócony zakres liczb podzielnych przez: 3, 5, 7.")
num_from = int(input("Wprowadź liczbę stanowiącą początek Twojego zakresu: "))
num_to = int(input("Wprowadź liczbę stanowiącą koniec Twojego zakresu: "))
print("Oto lista liczb z Twojego zakresu, które są podzielne albo przez 3 albo przez 5 albo przez 7: ")
for x in range(num_from, num_to + 1):
    if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        print(x)
    else:
        print("", end="")
