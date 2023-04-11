"""
2. Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
• stwórz modułu o dowolnej nazwie,
• dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
• dodaj funkcję sumującą wszystkie liczby z listy,
• dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
• dodaj testy weryfikujące poprawne działanie napisanych funkcji,
• zaimportuj utworzony moduł i skorzystaj z jego funkcji.
"""

import int_numb_list_handling

# print(dir(int_numb_list_handling))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'check_numbers', 'multplying_lits', 'summing_list']


print("Czy lista zawiera liczby?", int_numb_list_handling.check_numbers([1, 2, 3]))  # True
print("Suma elementów listy:", int_numb_list_handling.summing_list([3, 4, 2, 1, 2, 3, 5]))  # 20
print("Iloczyn elementów listy:", int_numb_list_handling.multplying_lits([3, 4, 2, 1, 2, 3, 5]))  # 720