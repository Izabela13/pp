import numli

list = [1, 2, 3, 4, 5]

print("Czy lista zawiera tylko liczby całkowite?", numli.is_list_of_integers(list))  # True
print("Suma elementów listy:", numli.sum_list(list))  # 15
print("Iloczyn elementów listy:", numli.product_list(list))  # 120