# Operatory porównania w sposób łańcuchowy - chaning comparison operator

a = 3
b = 4
c = 7

# Opratory można łączyć łańcuchowo, przy czym trzeba znać reguły
print(a < b < c) #True --> równorzędne z zapisem:
print(a < b and b < c)
# jest jednak haczyk w przypadku takiego zapisu: a < b < c. Ewaluacja "b" będzie pojedyncza.
# Jeżeli "b" byłoby jakimś wyrażeniem, w którym coś by było liczone, to "b" będzie liczone raz.
# W przypadku zapisu: a < b and b < c "b" będzie ewaluowane dwa razy.
print()

# W przypadku tego zapisu ewaluacja "b" będzie liczona tylko raz a < b < c

def get(a): #funkcja pobiera jakąś wartość i zwraca jakąś wartość, czyli nic takiego ta funkcja nie będzie robiła
    print("!!!") # oprócz tego, że poinformuje nas, że jakąś wartość pobrała, np. jakimiś wykrzyknikami.
    return a

# wykorzystanie funkcji
print("zapis a < b < c:")
print(a < get(b) < c)
# Wynik: program raz wyświetlił wykrzykniki i wypisał "True"
# !!!
# True

print("")
print("zapis a < b and b < c:")
print(a < get(b) and get(b) < c)
# Wynik: program dwa razy wyświetlił wykrzykniki i wypisał "True"
# !!!
# !!!
# True
