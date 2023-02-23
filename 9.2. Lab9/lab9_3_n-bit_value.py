"""
Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.
"""

number = int(input("Wprowadź dowolną liczbę całkowitą: "))
position = int(input("Wprowadź pozycję bitu, który chcesz zobaczyć, gdzie 0 to pierwsza pozycja: "))

print("")

# wykorzystanie maski dla sprawdzenia wskazanego bitu
mask = 1 << position # jeżeli bity liczone byłyby od 1, a nie od 0, wówczas byłoby to: "mask = 1 << position - 1"
outcome = number & mask
bit = int(bool(outcome))

# rozwiązanie z obejściem wykorzystania maski
# print("Dla liczby", number, "wartość bitu na pozycji", position, "przyjmuje wartość", "{:08b}".format(number)[-position-1] + ".")

# rozwiązanie z zastosowaniem maski
print("Dla liczby", number, "wartość bitu na pozycji", position, "przyjmuje wartość", str(bit) + ".")

print("Podana liczba przyjmuje następującą postać bitową:", bin(number) + ".")
