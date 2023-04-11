""" Moduł num_li ("num" od "numbers) i "li" od "lists". """

def is_list_of_integers(list):     # Funkcja przyjmuje jako argument listę
    for i in list:                 # dla każdego "i" w naszej liście sprawdzenie...
        if not isinstance(i, int): # ... czy dany element nie jest instancją klasy typu "int"
            return False           # Jeśli nie jest, to automatycznie zwracane jest "False"
    return True


def sum_list(list): # argumentem jest lista
    sum = 0  # zmienna lokalna na początku równa 0

    for i in list:
        sum += i  # do sumy dodawane będą kolejno wartości
    return sum


def product_list(list):
    product = 1  # ustawienie na 1, ponieważ ustawienie na 0 zwróci wartość mnożenia równą 0

    for i in list:
        product *= i
    return product


if __name__ == "__main__": # ktoś uruchamia moduł sam w sobie

    list = [1, 2, 3]
    print(is_list_of_integers(list) == True)
    print(is_list_of_integers(["a", "b", "c"]) == False)
    print(is_list_of_integers([True, False]) == False) # wartości bool będą rzutowane jako integer

    print(sum_list(list) == 6)
    print(sum_list(list) != 7)

    print(product_list(list) == 6)
    print(product_list(list) != 99)

"""
Jeżeli ktoś wstawi wartości Boolowskie do listy, to musimy pamiętać o tym, że będą one w naturalny sposób rzutowane
do wartości 0 i 1. 
"""