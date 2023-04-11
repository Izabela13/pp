import module  # importowanie naszego modułu

print(dir(module))  # za pomocą funkcji "dir()" sprawdzamy, co nasz moduł nam oferuje.

"""
Oto zestaw funkcjonalności naszego modułu o nazwie "module": 
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '
__package__', '__spec__', 'is_string', 'sum_list_element']

Oprócz funkcji wbudowanych (oznaczonych podwójnym podkreślnikiem), mamy funkcję napisane przez nas, czyli:
- is_string
- sum_list_element
"""

# Co funkcja "help()" mówi o naszym module?
help(module)
"""
Help on module module:  --> informacja, że jest to "help" na module "module"

NAME  --> nazwa modułu to "module"
    module - This is my first own module  --> "Fragment, który sami zapisaliśmy w module, jako wielolinijkowy komentarz.

FUNCTIONS  --> funkcjonalności, które zawiera moduł "module".
    is_string(val)
        Simple string value validator  --> dokumentacja - opis funkcji w wielolinijkowym komentarzu.
    
    sum_list_element(list)

FILE
    c:\kursy\python\podstprogrampy\16.1.2. module\module.py  --> nazwa pliku, skąd ten moduł został zaimportowany.
"""


print("Czy to jest ciąg znaków?", module.is_string("test"))
print("Suma elementów listy:", module.sum_list_element([3, 4, 2, 1, 2, 3, 5]))