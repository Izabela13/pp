# stack = stos; pop = procedural orientated programming (programowanie zorientowane na procedury)

stack = []  # dla stosu najlepszym sposobem dla przechowywania elementów będzie lista

# Sposób na układanie elementów w stosie
def push(val):  # będziemy brać element o wartości "val" i dokładać do stosu
    stack.append(val)  # na stosie układane będą kolejne elementy (dokładnanie elementów)


def pop():  # przy ściąganiu elementów nie trzeba parametryzować funkcji - ściągamy elementy od końca
    val = stack[-1]  # do zmiennej lokalnej "val" przypisujemy to, co znajduje się na samej górze stosu
    del stack[-1]  # usuwamy element, ponieważ ściągamy go ze stosu
    return val  # zwracanie elementu


# Wrzucanie elementów do stosu:
push(3)
push(2)
push(1)

print(stack)  # [3, 2, 1] --> po wrzuceniu trzech elementów

# Ściąganie elementów ze stosu
print(pop())  # 1
print(pop())  # 2
print(pop())  # 3
# Zwracanie od końca. Ostatnia dodana była wartość 1. Jako pierwsza wyszła wartość 1.

# Sytuacja zacznie się komplikować, gdy będzie trzeba dodać kolejne stosy i przekładać między nimi elementy.
# Prosty program przez rozbudowę stanie się mniej czytelny, nieodporny na błędy.