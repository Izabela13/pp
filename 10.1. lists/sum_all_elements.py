# Polecenie: zsumuj wszystkie elementy.

sum = 0 # na początku suma równa jest 0

numbers = [1, 2, 5, 77, 85, 2, 2, 2, 2, 3234, 2323, 23] # lista liczb do zsumowania

for e in numbers: # sumowanie elementów w pętli for - nie potrzebujęt tutaj indeksów
    sum += e # polecenie - dodawaj element do sumy
print("Suma wszystkich elementów listy", numbers, "to", str(sum) + ".")

# Można też było po prostu zsumować:
# print(sum(numbers)) # tylko uwaga na konflikt nazw
