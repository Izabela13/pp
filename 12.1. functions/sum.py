# Funkcja będzie sumowała i przyjmowała dwie wartości

def sum(a, b): # funkcja jest parametryzowana - będzie miała dwie wartości - "a" i "b"
    return a + b # funkcja zwraca wyrażenie (sumę argumentów) za pomocą funkcji return

result = sum(1, 6) # do zmiennej result podstawiamy dwie liczby, które zwróci funkcja "sum"

print(result) #7 - wyświetlenie tego, co zwróci funkcja "result"

# Brak podania któregokolwiek argumentu wyświetli wyjątek - zawsze trzeba podać tyle argumentów, ile jest wymagane w funkcji
# Żeby użyć funkcji musi ona być wcześniej zdefiniowana. W momencie użycia funkcji, funkcja musi być znana.