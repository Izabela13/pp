# PROGRAM DO GRY W LOTTO


# Gra w lotto będzie korzystała z wczesniej przygotowanego modułu.
# Import funkcji, które wiemy, że istnieją i będziemy z nich korzystać.
from lotto import get_user_numbers, check_numbers, draw_numbers


# IMPLEMENTACJA GRY.
print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()  # Wylosowane przez użytkownika liczby zostaną zapisane do zmiennej "user_numbers".
print("Podane liczby to: ", user_numbers) # Wyświetlenie liczb podanych przez użytkownika.

print("\nNaciśnij ENTER, aby dokonać losowania liczb! \n")  # elegancka wizualizacja
input()

lucky_numbers = draw_numbers()  # do zmiennej "lucky_numbers" zapisywane będą liczby wylosowane przez komputer.
print("Wylosowane liczby to:", lucky_numbers)


# Wyświetlanie wyników - odwołanie się do funkcji "check_numbers" z argumentami "user_numbers" i "lucky_numbers".
result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("GRATULACJE!!!", "Jesteś milionerem!")
elif result == 5:
    print("BRAWO!", "Trafiono piątkę!", "Zgarniesz sporą sumkę.")
elif result == 4:
    print("Hurra!", "Trafiono czwórkę!", "To całkiem niezły wynik.")
elif result == 3:
    print("Trafiono trójkę.", "Przysługuje Ci minimalna wygrana.")
elif result in (1, 2):
    print("Trafiono", result, "liczbę. Było bardzo blisko.")
else:
    print("To nie jest Twój dzień :(")


"""
Przez to, że kod do obsługi gry w lotto został podzielony w taki sposób, że główny "core" został oddzielony od obsługi 
gry, kod jest dużo bardziej przejrzysty. Jeżeli znajdzie się gdzieś błąd, dużo prościej będzie go poprawić. 
"""