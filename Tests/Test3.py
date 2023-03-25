"""
Napisz funkcję zliczającą ilość wystąpień poszczególnych elementów listy w formie słownika.

Przykład:

print(frequency_occurrences(["Ala", "Tomek", "Ala"]))

{'Ala': 2, 'Tomek': 1}
"""

list = ["Ala", "Tomek", "Ala"]


def counting_dict_elements(list):

    uniq_list = []

    for i in list:
        if i not in list:
            uniq_list.append(list)

    return {uniq_list[i]: [0]}

print(counting_dict_elements(list))