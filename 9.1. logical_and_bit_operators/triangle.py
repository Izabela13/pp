# Pytamy użytkownika o 3 odcinki. Na tej podstawie będziemy oceniać, czy da się zbudować z nich trójkąt.
# Jeżeli z trzech podanych długości odcinków można zbudować trójkąt, to ocenimy, jaki to będzie trójkąt.
# Będziemy oceniać trójkąt pod względem następujących charakterystyk:
# 1) czy ze względu na boki będzie to trójkąt równoboczny, różnoboczny czy równoramienny
# 2) czy ze względu na kąty będzie to trójkąt prostokątny, ostrokątny czy rozwartokątny

print("Podaj długości 3 odcinków (liczby całkowite): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


# Weryfikacja, czy z tych trzech odcinków można zbudować trójkąt.
# Aby z trzech odcinków dało się zbudować trójkąt, suma każdego z dwóch odcinków musi być większa od długości trzeciego.
if (a + b > c and b + c > a and c + a > b): # musi być spełniona każda wariacja sumy dwóch odcinków względem trzeciego.
    print("Z tych odcinków można zbudować trójkąt", end = " ") # nie przechodzimy do nowej linii, tutaj podamy, jaki trójkąt można zbudować

    if a == b and a == c and c == b:
        print("równoboczny", end = " ")
    elif a == b or b == c or c == a:
        print("równoramienny", end = " ")
    else:
        print("różnoramienny", end = " ")

    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (c ** 2 + a ** 2 == b ** 2):
        print("prostokątny.")
    elif (a ** 2 + b ** 2 < c ** 2) or (b ** 2 + c ** 2 < a ** 2) or (c ** 2 + a ** 2 < b ** 2):
        print("rozwartokątny.")
    else:
        print("ostrokątny.")

else:
    print("Niestety z tych odcinków nie postawnie trójkąt.")
