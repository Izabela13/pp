import module

# print(dir(module))
#
# """
# module
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '
# __package__', '__spec__', 'is_string', 'sum_list_element']
# """
#
# help(module) # Fragment, który sami zapisaliśmy w module jako wielolinijkowy komentarz


print("Czy to jest ciąg znaków?", module.is_string("test"))
print("Suma elementów listy:", module.sum_list_element([3, 4, 2, 1, 2, 3, 5]))