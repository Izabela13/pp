def is_list_of_integers(list):
    for i in list:
        if not isinstance(i, int):
            return False
    return True


def sum_list():
    sum = 0

    for i in list:
        sum += i
    return sum


def product_list(list):
    product = 1

    for i in list:
        product *= i
    return product


if __name__ == "__main__": # ktoś uruchamia moduł sam w sobie

    list = [1, 2, 3]
    print(is_list_of_integers(list) == True)
    print(is_list_of_integers(["a", "b", "c"]) == False)

    print(sum_list(list) == 6)
    print(sum_list(list) != 7)

    print(product_list(list) == 6)
    print(product_list(list) != 99)