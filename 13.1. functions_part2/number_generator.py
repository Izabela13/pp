# Funkcja losująca liczby od 1 do 99

import random # losowanie liczb pseudolosowych - importowanie bibliotek na początku

def generate_numbers(total_numbers): # paramterem naszej funkcji będzie ilość liczb
    numbers = [] # losowanie do listy
    for i in range(total_numbers): # do listy dodamy wylosowaną wartość
        numbers.append(random.randint(1, 99))
    return numbers # zwrócenie listy numbers

print(generate_numbers(10)) # wylosuj 10 liczb i pokaż je na ekranie
print(generate_numbers(100))
print(generate_numbers(23423))