def my_name():
    return "Marcin" # Ta funkcja zwraca jakąś wartość i nie drukuje nic

def show_my_name():
    print("Marcin") # Ta funkcja też zwraca jakąś wartość i ją drukuje
    return None


# Wywołanie funkcji:
my_name() # nie ma znaczenia, czy funkcja coś zwróci
# po wywołaniu nic się nie wydarzyło, bo nie ma komendy print()

result = my_name() # jednak chcę wydrukować
print(result)


# Podejście nr 2
# show_my_name ma wbite "print"
result = show_my_name()
print(result)
# Zawsze będzie się wyświetlać "Marcin", bo wbita jest funkcja "print". Ale ta funkcja zwróci "None".