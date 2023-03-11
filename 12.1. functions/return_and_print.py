# # Czym się różni wprowadzenie do funkcji print() a return.
def my_name():
    return "Marcin" # Ta funkcja zwraca jakąś wartość i nie drukuje nic

def show_my_name():
    print("Marcin") # Ta funkcja też zwraca jakąś wartość i wcześniej jeszcze coś drukuje
    return None # Każda funkcja zwraca jakąś wartość. "return None" jest opcjonalne.

# Jaka jest różnica między funkcją "my_name" a "show_my_name"?
# Funkcja "show_my_name" jeszcze coś drukuje.


# Wywołanie funkcji:
my_name() # nic się nie pojawiło.
# Nie ma znaczenia, czy funkcja coś zwróci. Jeżeli ta funkcja coś zwróci, to ignorujemy to.
# Po wywołaniu nic się nie wydarzyło, bo nie ma komendy print()

# Nie trzeba ingnorować tego, co zwraca ta funkcja.
result = my_name() # jednak chcę wydrukować, to co zawiera funkcja "my_name", więc podstawiam ją do jakiejś zmiennej.
print(result) # drukowanie jawne
# Zadaniem funkcji "my_name" jest tylko zwrócić jakiś ciąg znaków (ale go nie wyświetlać).
# Po wywołaniu tej funkcji na konsoli nie pojawi się nic, ponieważ nikt nie podał komendy "wydrukuj".
# Jeżeli podstawimy funkcję "my_name" do zmiennej "result", to samo podstawienie nie spowoduje wydrukowania wartości.
# Dopiero wydanie polecenia print(result) spowoduje wydrukowanie jakiejś wartości na konsoli.


# Podejście nr 2
# Funkcja "show_my_name" podczas wykonania ma wbite "print". Mimo tego, że wynik zostanie zapisany do zmiennej "result",
# to oprócz tego, że jakiś rezultat zapisze się w zmiennej "result" to w międzyczasie, podczas wywoływania funkcji
# "show_my_name" wywoła się akcja "print" i pojawi się wartość, która była przechowywana w funkcji print().
result = show_my_name()
print(result) # Wynik w pierwszej linijce: Marcin
              # Wynik w drugiej linijce: None
# Skąd się wzięło "Marcin" i skąd się wzięło "None"?
# "Marcin" wzięło się stąd, że podczas tego podstawiania wydrukowało się "Marcin".
# "None" wzięło się stąd, że funkcja "show_my_name" zwraca (return) wartość "None" i jeszcze drukuje tę wartość.
# Pod return można podstawić coś innego, np. 1234565433. Wówczas w miejsce "None" wydrukuje się wartość "1234565433".

# Podczas działania programu najczęściej nie wyświetla się funkcji. Zwykle dopiero, gdy wykorzystuje się funkcję,
# wówczas przekazuje się ją do jakiegoś innego miejsca, np. do wyświetlenia na stronie, przekazania mailowe, etc.