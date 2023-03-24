"""
1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.
"""

def delete_duplicates(original_list):

    uniqes_list = []

    for element in original_list:
        if element not in uniqes_list:
            uniqes_list.append(element)

    return uniqes_list


print(delete_duplicates([1, 2, 3, 1, 2, 3, 1, 1, 2]))
print(delete_duplicates(["do", "mi", "sol", "mi", "do", "fa", "la", "fa", "do", "mi", "sol", "mi", "do"]))