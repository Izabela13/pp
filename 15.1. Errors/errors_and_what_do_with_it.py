# # SyntaxError - błędy składni

# print("sdfgdsfg")
# # to jest działający program, ale gdy nie domniemy nawiasu funkcji print(), to pojawi się wyjątek.

# print("sdfgdsfg" # SyntaxError: '(' was never closed
# # Podczas próby uruchomienia program nie uruchomi się. Nie wydrukuje się nawet to print(), które było poprawne.
# # Przy pojawieniu się "SyntaxError" pojawia się również informacja, że nawias, który został otwarty, nie został zamknięty.

# # NIE DA SIĘ OBSŁUGIWAĆ BŁĘDÓW SKŁADNIOWYCH, TRZEBA JE POPRAWIĆ



# # ZeroDivisionError: division by zero
# print(1/0) # program jest syntaktycznie poprawny

try:
    print(1 / 0) # jeżeli w tej linijce wystąpi wyjątek
except:
    print("Coś poszło nie tak... ") # program zostanie obsłużony