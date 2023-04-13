"""
2. Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
liczbę wystąpień każdego znaku w ciągu.
Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
2, 'r': 2, 'c': 1, 'd': 1 }.
"""


def get_string(string):

    signs_occuring = {}

    for c in string:
        if c in signs_occuring:
            signs_occuring[c] += 1
        else:
            signs_occuring[c] = 1

    return signs_occuring


def show_result():

    signs_count = get_string(string)

    print("Wprowadzony ciąg znaków:", string)
    print("Liczba wystąpień znaków w ciągu znaków: ")

    for sign in signs_count:
        print(sign + ":", signs_count[sign])

    print()


string = "abracadabra"
show_result()

string = "mamma mia"
show_result()

string = "Ala ma kota, a kot ma Alę..."
show_result()

string = "Król Karol kupił królowej Karolinie korale koloru koralowego."
show_result()