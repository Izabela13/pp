"""
2. Chcemy ułożyć wieżę z puszek.
Wieża składa się z poziomów, gdzie każdy wyższy poziom wymaga jednej puszki mniej niż poziom na którym go zbudowano.

Korzystając z rekurencji napisz program, który pozwoli:
1) wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym poziomie oraz
2) ilość poziomów wieży jakie jesteśmy w stanie ułożyć z dostępnej liczby puszek.

Przykład: jeżeli chcemy ułożyć 3 poziomową wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4 poziomową wieżę.

      []
    [] []
  [] [] []
[] [] [] []
"""


print("BUDOWANIE WIEŻY Z PUSZEK \n")

def check_and_return_message(standard_msg, error_msg = "Podana wartość nie jest liczbą całkowitą. \n"):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


# 1. Wyliczanie ilość potrzebnych puszek do wybudowania wieży o zadanym poziomie.

cans_levels = check_and_return_message("Podaj liczbę poziomów, z jakich ma składać się wieża: ")

def counting_cans_in_levels(cans_levels):
    if cans_levels > 0:
        cans = cans_levels + counting_cans_in_levels(cans_levels - 1)
    else:
        cans = 0
    return cans


print("Liczba puszek potrzebna do wybudowania wieży o " + str(cans_levels) + " poziomach: "
      + str(counting_cans_in_levels(cans_levels)))

print()



# 2. Wyliczenie ilości poziomów wieży jakie można ułożyć z dostępnej liczby puszek.

cans = check_and_return_message("Podaj liczbę puszek, z jakich ma składać się wieża: ")

def counting_levels_for_cans(cans, row):

    if cans >= row:
        cans -= row
        row += 1
        if cans == 0 or cans < row:
            print(row - 1)
        counting_levels_for_cans(cans, row)


print("Puszki w ilości " + str(cans) + " wystarczą do wybudowania wieży o poziomach: ", end="")
counting_levels_for_cans(cans, 1)


# Obliczanie, ile puszek zostanie niewykorzystanych przy budowie wieży z dostępnej liczby puszek
def counting_levels_for_cans_without_rec(cans):
    row = 0
    while True:
        if cans >= row:
            cans -= row
            row += 1
        if cans < row:
            return row - 1


if cans != counting_levels_for_cans_without_rec(cans):
    cans_levels = counting_levels_for_cans_without_rec(cans)
    print("Puszki, które zostaną niewykorzystane: " + str(cans - counting_cans_in_levels(cans_levels)))