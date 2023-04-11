"""INTEGER NUMBERS LISTS HANDLING MODULE"""

"""Funkcja weryfikującą czy podana lista zawiera wyłącznie liczby całkowite"""
def check_numbers(list):

    only_numb = []

    for i in list:
        if isinstance(i, int):
            only_numb.append(i)

    if len(list) != len(only_numb):
        return False
    else:
        return True


"""Funkcja sumującą wszystkie liczby z listy"""
def summing_list(list):

    sum_list = 0

    for i in list:
        sum_list += i
    return sum_list


""" Funkcja zwracającą iloczyn wszystkich liczb z listy"""
def multplying_lits(list):

    mult_list = 1

    for i in list:
        mult_list *= i
    return mult_list


"""Testy weryfikujące poprawne działanie napisanych funkcji"""
if __name__ == "__main__":
    print(check_numbers([1, 2, 3]) == True)        # True
    print(check_numbers([1, 2, "trzy"]) == False)  # True

    print(summing_list([1, 2, 3]) == 6)            # True

    print(multplying_lits([1, 2, 3]) == 6)         # True