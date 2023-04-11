"""
This is my first own module
"""

def is_string(val):
    """ Simple string value validator """
    return isinstance(val, str)


def sum_list_element(list):
    sum = 0

    for i in list:
        sum += i
    return sum


print(__name__)

###########################################
if __name__ == "__main__":
    print(is_string("haha") == True)
    print(is_string(123) == False)
    print(sum_list_element([1, 1, 1]) == 3)
    print(sum_list_element([]) == 0)