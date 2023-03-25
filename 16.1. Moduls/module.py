"""
This is my first own module
"""

# Funkcja sprawdzająca, czy coś jest napisem czy nie
def is_string(val):
    """ Simple string value validator """
    return isinstance(val, str)


# Sumator elementów listy
def sum_list_element(list):
    sum = 0

    for i in list:
        sum += i
    return sum


print(__name__) # __main__ (wywołanie modułu samodzielnie)

# Ten fragment zostanie wykonany tylko w momencie, kiedy będzie wykonywany moduł
if __name__ == "__main__": # pisanie oprogramowania do momentu, w którym wszystkie testy nie zostaną spełnione
    print(is_string("haha") == True)
    print(is_string(123) == False)
    print(sum_list_element([1, 1, 1]) == 3)
    print(sum_list_element([]) == 0)

"""
__main__
True
True
True
True
"""