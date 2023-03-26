"""
Napisz funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.

Przykład:

print(frequency_occurrences(["Ala", "Tomek", "Ala"]))

{'Ala': 2, 'Tomek': 1}
"""
# 1. Funkcja, która przyjmuje jako argument listę
# 2. Lista --> słownik

lista = ["Ala", "Tomek", "Ala"]


def frequency_occurrences(source_list):
    target_dict = {}

    for e in source_list:
        if e in target_dict:
            target_dict[e] += 1
        else:
            target_dict[e] = 1

    return target_dict


print(frequency_occurrences(["Ala", "Tomek", "Ala"]))
print(frequency_occurrences([1, 1, 1]))
print(frequency_occurrences([1, 111, 222, 3, 5, 6, 7, 8, 99, 99, 99, 99, 99, 99, 99]))


def frequency_occurrences(source_list):
    target_dict = {}

    for e in source_list:
        target_dict[e] = source_list.count(e)
    return target_dict

print(frequency_occurrences(["Ala", "Tomek", "Ala"]))