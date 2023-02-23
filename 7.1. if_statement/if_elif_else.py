## WYRAŻENIA RELACJI

# print(7 > 11) # Zastosowanie prostego operatora logicznego - wyświetli się "False"
# wyrażenie ewaluuje, czyli zostanie, czyli zostanie rozwiązane do jakiejś wartosci - w tym wypadku do wartości "False".
# #wyrażenie to elementy w nawiasie (7 > 11). Print to instrukcja - co ma zostać wykonane, np. (print(7 > 11))
#
# a, b = 11, 9 # zapis możliwy, ale mniej czytelny
# print(a>=b)    # Wynik = True
# print(2 == 2)  # Wynik = True
# print(2 == 2.) # Wynik = True

## Uwaga, poniższy zapis wygeneruje błąd składniowy - syntaks error
# print(2 = 2.)
# SyntaxError: wyrażenie logiczne nie może zawierać operatora przypisania.
#######################################################################################################################



## INSTRUKCJE WARUNKOWE/ ZŁOŻONE INSTRUKCJE WARUNKOWE "IF"

# number = 2
#
# if number > 3:
#     print("Liczba jest większa niż 3") #jeżeli wartość nie spełnia warunku, wówczas program przechodzi dalej
#     print("Hurra!")
# print("Koniec") # ten print nie należy do powyższego bloku kodu

#PyCharm ma zdefiniowane ustawienia - tabulator to 4 spacje. Pisanie w notatniku spowoduje, że kod wypadnie z bloku
#Liczba spacji musi być jednorodna w całym programie.


# number = 0
#
# if number > 0:
#     print("Liczba większa od zero")
# else:
#     print("Liczba mniejsza lub równa zero")


# number = -2
#
# if number > 0:
#     print("Liczba większa od zero")
# elif number < 0:
#     print("Liczba mniejsza od zero")
# else:
#     print("Liczba jest zerem")