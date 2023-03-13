# Funkcja losująca liczby od 1 do 99

import random # losowanie liczb pseudolosowych - importowanie bibliotek na początku

def generate_numbers(total_numbers): # paramterem naszej funkcji będzie ilość liczb do wylosowania
    numbers = [] # losowanie do listy - utworzenie zmiennej lokalnej, która na początku będzie pustą listą
    for i in range(total_numbers): # zakres listy to podana wartość w parametrze "total_numbers"
        numbers.append(random.randint(1, 99))  # do listy "numbers" za każdym razem dodamy wylosowaną wartość
    return numbers # zwrócenie listy "numbers"

# Żeby zobaczyć coś na ekranie trzeba użyć instrukcji print()
print(generate_numbers(10)) # wylosuj 10 liczb i pokaż je na ekranie
print(generate_numbers(100))
print(generate_numbers(23423))