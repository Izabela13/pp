"""INTEGER NUMBERS"""

"""Funkcja weryfikującą czy podana lista zawiera wyłącznie liczby całkowite"""
def check_numbers(list):

    for i in list:
        if i == int(i):
            return True
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
    print(check_numbers([1, 2, 3]) == True)
    print(summing_list([1, 2, 3]) == 6)
    print(multplying_lits([1, 2, 3]) == 6)
"""
True
True
True
"""