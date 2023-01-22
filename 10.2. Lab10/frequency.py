"""
Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
występuje 3 razy.
"""

ditgits = [1, 2, 4, 6, 6, 2, 6, 6]

frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in ditgits:
    frequency[digit] += 1

print(frequency)

most_common = -1 # bo indeksuje się od 0

for i in range(len(frequency)):
    if frequency[i] > most_common:
        most_common = i

print("Najczęściej występującą cyfrą jest " + str(most_common) + ",", "występuje", frequency[most_common], "razy.")


##################################################
#Wyjaśnienie

digits_test = [1, 2, 1, 5] #zakładamy, że są to cyfry
# policzenie, która cyfra występuje najwięcej razy i ile razy występuje
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(digits_test)
for digit in digits_test:
    frequency[digit] += 1
print(frequency)

