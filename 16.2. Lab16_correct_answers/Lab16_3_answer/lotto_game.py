# Zadanie 3: PROGRAM DO GRY W LOTTO Z MOŻLIWOŚCIĄ GRANIA SYSTEMAMI

from lotto import get_user_numbers, check_numbers, draw_numbers

print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb! \n")
input()

lucky_numbers = draw_numbers()
print("Wylosowane liczby to:", lucky_numbers)


result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("GRATULACJE!!! Jesteś milionerem!")
elif result == 5:
    print("BRAWO! Trafiono piątkę! Zgarniesz sporą sumkę.")
elif result == 4:
    print("Hurra! Trafiono czwórkę! To całkiem niezły wynik.")
elif result == 3:
    print("Trafiono trójkę. Przysługuje Ci minimalna wygrana.")
elif result in (1, 2):
    print("Trafiono", result, "liczbę. Było bardzo blisko.")
else:
    print("To nie jest Twój dzień :(")