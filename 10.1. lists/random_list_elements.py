# Zadanie: wygenerować 10 pseudolosowych liczb, umieścić w liście i wyświetlić.
import random # zaimportowanie modułu "random"

numbers = [] # wylosowane numery będą zapisywane w liście

for i in range(10): # w pętli for będzie losowane w sumie 10 liczb
    number = random.randint(1, 100) # losowanie liczb od 1 do 100
    numbers.append(number) # każda liczba będzie zapisywana do zmiennej number (metoda append)

print(numbers)
