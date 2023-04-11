# PROGRAM DO GRY W LOTTO Z MOŻLIWOŚCIĄ GRANIA SYSTEMEM


from lotto_betting_max_12_numb import get_user_numbers, check_numbers, draw_numbers


# IMPLEMENTACJA GRY.
print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb! \n")
input()

lucky_numbers = draw_numbers()
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