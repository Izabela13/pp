"""
1. Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
powinna zwrócić None.
"""

# 1
def safe_int():
    try:
        arg = int(input("Podaj wartość: "))
        return arg
    except ValueError:
        return None

print(safe_int())