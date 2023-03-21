"""
2. Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)
"""

def change_3lists_to_tuple_without_duplicates(list1, list2, list3):
    all_elem = list1 + list2 + list3
    main_list = []

    for element in all_elem:
        if element not in main_list:
            main_list.append(element)

    return tuple(main_list)


list1 = [1, 2]
list2 = [1, 1]
list3 = [4, 4, 4]

print(change_3lists_to_tuple_without_duplicates(list1, list2, list3))
print(change_3lists_to_tuple_without_duplicates(["1", "1", "2", "3"], [1, 1, 2, 3], [4, "4", 3, "3"]))
print(change_3lists_to_tuple_without_duplicates(["do", "mi", "sol", "mi"], ["do", "fa", "la", "fa"], ["do", "mi", "sol", "mi", "do"]))