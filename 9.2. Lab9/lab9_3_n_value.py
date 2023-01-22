"""
Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.
"""

number = int(input("Wprowadź dowolną liczbę całkowitą z zakresu od -255 do 255: "))
position = int(input("Wprowadź numer bitu, który chcesz zobaczyć: "))

print("Liczba, którą podałeś, przyjmuje następującą postać bitową: ", "{:08b}".format(number))
print("Pozycja, którą podałeś, to ", "{:08b}".format(number)[-position])

print()

# rozwiązanie z wykorzystaniem maski --> koniunkcja bitowa

mask = 1 << position
result = number & mask
bit = int(bool(result))
print(bit)

#liczba nie może być większa niż 255 (-255)