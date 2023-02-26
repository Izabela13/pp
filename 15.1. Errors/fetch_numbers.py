# Sworzymy tablicę numbers

numbers = []

# for i in range(5):
#     n = int(input("Podaj liczbę całkowitą: "))
#     numbers.append(n)
# print(numbers) #ValueError: invalid literal for int() with base 10: 'd'


# Wprowadzenie obsługi błędów. Program będzie prosił użytkownika o podanie liczby, dopóki nie poda jej poprawnie
# Teraz będzie potrzebny counter

counter = 0

while True:
    if counter > 4:
        break
    try:
        n = int(input("Podaj liczbę całkowitą: "))
        numbers.append(n)
        counter += 1
    except:
        print("To nie jest liczba całkowita! Spróbuj ponownie")

print(numbers)