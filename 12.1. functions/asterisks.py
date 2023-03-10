# Parametryzowanie funkcji.

def show_asterisks(how_many): # metoda, która będzie posiadać parameter "how_many"
    print("*" * how_many) # za pomocą parametru "how_many" znak "*" zostanie wyświetlony tyle razy, ile zostanie podane do funkcji

# Podawanie wartości argumentu
show_asterisks(10) # wartość "how_many"
show_asterisks(0)
show_asterisks(10000)
# Podczas wywołania funkcji sterowanie programem przerzucane jest do funkcji.
# Po wykonaniu funkcji program wraca do miejsca, w którym przerwał.